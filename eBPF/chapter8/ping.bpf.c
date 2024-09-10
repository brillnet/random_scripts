#include "network.h"
#include <bcc/proto.h>
#include <linux/pkt_cls.h>


int xdp(struct xdp_md *ctx) {
  void *data = (void *)(long)ctx->data;
  void *data_end = (void *)(long)ctx->data_end;

  if (is_icmp_ping_request(data, data_end)) {
        bpf_trace_printk("Got ping packet");
        return XDP_PASS;
  }

  // unsigned short a is_https_traffic(data, data_end);
  bpf_trace_printk("Port: %u\n", is_https_traffic(data, data_end));

  if (is_https_traffic(data, data_end)) {
        bpf_trace_printk("Got https packet!");
        return XDP_PASS;
  }

  

  return XDP_PASS;
}