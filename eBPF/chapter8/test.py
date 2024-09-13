#!/usr/bin/python3
from pyroute2 import IPRoute
from bcc import BPF
import socket
import os
from time import sleep

ipr = IPRoute()

# this request returns one match
# enp1s0 = ipr.link_lookup(ifname='enp1s0')
# print(len(enp1s0))  # -> 1, if exists, else 0

# but that one returns a set of
up = ipr.link_lookup(operstate='UP')
print(len(up))  # -> k, where 0 <= k <= [interface count]

# print(help(ipr.tc("modules")["bpf"]))

#################################################

# ipr.tc("add-filter",
#  "bpf", 
#  idx, 
#  ":1", 
#  fd=fi.fd, 
#  name=fi.name, 
#  parent="ffff:", 
#  action="ok", 
#  classid=1, 
#  da=True)

b = BPF(src_file="network.bpf.c")
fi = b.load_func("tc_pingpong", BPF.SCHED_CLS)

enp1s0 = ipr.get_links(ifname="enp1s0")[0]

#  Getting idx value of enp1s0
interface = "enp1s0"
links = ipr.link_lookup(ifname=interface)
idx = links[0]

ipr.tc("del", "clsact", 2)
ipr.tc("add", "clsact", 2)

# add ingress clsact
ipr.tc("add-filter", "bpf", idx, ":1", fd=fi.fd, name="fi.name",
       parent="ffff:fff2", classid=1, direct_action=True)
# ip.tc("add-filter", "bpf", idx, ":1", fd=fd, name="myprog",
#       parent="ffff:fff2", classid=1, direct_action=True)
# add egress clsact
ipr.tc("add-filter", "bpf", idx, ":1", fd=fi.fd, name="fi.name",
       parent="ffff:fff3", classid=1, direct_action=True)
# ip.tc("add-filter", "bpf", idx, ":1", fd=fd, name="myprog",
#       parent="ffff:fff3", classid=1, direct_action=True)


#################################################
