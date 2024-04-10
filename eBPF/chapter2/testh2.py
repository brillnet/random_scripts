#!/usr/bin/python
from bcc import BPF
from time import sleep

#  The below C program will run in the kernel.
#  The program creates a dictionary with the
#  key being the uid and the value being the
#  the number of times that uid made a syscall
#  of type execve.
program = r"""

BPF_HASH(counter_table);

int hello(void *ctx) {
u64 uid;
u64 counter = 0;
u64 *p;
uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;
p = counter_table.lookup(&uid);

if (p != 0) {
    counter = *p;
}

counter++;
counter_table.update(&uid, &counter);

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

#  While loop to read in that is created inside
#  the C program that is running in the kernel.
#  This is a way of passing data collected in th
#  program back up to the userspace python script.
while True:
    sleep(2)
    s = ""
    for k,v in b["counter_table"].items():
        s += f"ID {k.value}: {v.value}\t"
    print(s)