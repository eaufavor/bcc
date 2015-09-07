#!/usr/bin/python
#
# bitehist.py	Block I/O size histogram.
#		For Linux, uses BCC, eBPF. See .c file.
#
# Written as a basic example of using a histogram to show a distribution.
#
# The default interval is 5 seconds. A Ctrl-C will print the partially
# gathered histogram then exit.
#
# Copyright (c) 2015 Brendan Gregg.
# Licensed under the Apache License, Version 2.0 (the "License")
#
# 15-Aug-2015	Brendan Gregg	Created this.

from bcc import BPF
from time import sleep

# load BPF program
b = BPF(src_file = "bitehist.c")
b.attach_kprobe(event="blk_start_request", fn_name="do_request")

# header
print("Tracing... Hit Ctrl-C to end.")

# output
try:
	sleep(99999999)
except KeyboardInterrupt:
	print

b["dist"].print_log2_hist()
