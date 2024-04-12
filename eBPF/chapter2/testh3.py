#!/usr/bin/python
from bcc import BPF
from time import sleep

#  The below C program creates a global data structure
#  called output that will be passeed up to the userspace
#  python script. This data structure will consist of
#  three variables. The first is ctx, this is for passing of
#  context from the calling eBPG program to the calle the second is
#  data, this is a struct that holds a pid,uid,command executed
#  and the message.  The next is the total size of the data
#  structure. 
program = r"""

BPF_PERF_OUTPUT(output);

struct data_t {
    int pid;
    int uid;
    char command[16];
    char message[12];
};

int hello(void *ctx) {

    struct data_t data = {};
    char message[12] = "Hello World";

    data.pid = bpf_get_current_pid_tgid() >> 32;

    data.uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;

    bpf_get_current_comm(&data.command, sizeof(data.command));

    bpf_probe_read_kernel(&data.message, sizeof(data.message), message);

    output.perf_submit(ctx, &data, sizeof(data));

    return 0;
}

"""

#  Loading program into the kernel
b = BPF(text=program)

# Setting the syscall we want to trigger off of. 
syscall = b.get_syscall_fnname("execve")

#  Attaching kprobe to the syscall event. When execve
#  syscall event is generated the C program will run
#  in the kernel.
b.attach_kprobe(event=syscall, fn_name="hello")

#  Function to print data sent from C program.
def print_event(cpu, data, size):
    data = b["output"].event(data)
    print(f"{data.pid} {data.uid} {data.command.decode()} " + \
    f"{data.message.decode()}")

#  Open perf ring buffer (memory) and assigns the
#  print_event function as a call back function
#  everytime data is read from the buffer.
b["output"].open_perf_buffer(print_event)

#  Reading data forever.
while True:
    b.perf_buffer_poll()