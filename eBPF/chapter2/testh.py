#!/usr/bin/python
from bcc import BPF

#  The below C program will run in the kernel.
program = r"""
int hello(void *ctx) {
bpf_trace_printk("Hello World!");
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

#  Printing the output from the C code running in kernel.
print(b.trace_print())
