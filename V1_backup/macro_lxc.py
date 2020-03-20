#!/usr/bin/python2.7

import sys
import time
import libiopc_rest as rst

def post_lxc_cfg(hostname, idx, enable):
    key = 'lxc_%d' % idx
    json = '{'
    json += '"enable":%d, ' % enable
    json += '"name":"vm%03d", ' % idx
    json += '"rootfs":"/hdd/sdb/vm%03d", ' % idx
    json += '"fstab":"/hdd/sdb/vm%03d.fstab", ' % idx
    json += '"nettype":"veth", '
    json += '"nethwlink":"br0", '
    json += '"nethwaddr":"00:19:82:03:21:%02d", ' % idx
    json += '"ipaddress":"192.168.155.%d", ' % idx
    json += '"gateway":"192.168.155.254"'
    json += '}'
    rst.response_output(out_format, rst.http_post_dao_by_key(hostname, key, json))

def gen_lxc_cfg(hostname, idx):
    payload = '{'
    payload += '"ops":"gen_lxc_cfg",'
    payload += '"index":%d' % idx
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def start_lxc(out_format, hostname, idx):
    payload = '{'
    payload += '"ops":"start_lxc",'
    payload += '"index":%d' % idx
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def request_list(hostname, out_format, action):
    idx = 1
    enable = 1
    if action == "start":
        post_lxc_cfg(hostname, idx, enable)
        gen_lxc_cfg(hostname, idx)
        time.sleep(1)
        start_lxc(hostname, idx)

    if action == "stop":
        print "Not Supported, Now..."

def help_usage():
    print "rest_cli.py <hostname> <action>"
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]
    action=sys.argv[2]

    request_list(hostname, 'json', action)

