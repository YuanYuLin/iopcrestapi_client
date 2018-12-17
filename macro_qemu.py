#!/usr/bin/python2.7

import sys
import time
import libiopc_rest as rst

def post_qemu_cfg(out_format, hostname, idx, enable):
    key="qemu_%d" % idx
    json = '{'
    json += '"enable":%d, ' % enable
    json += '"name":"qemu%03d", ' % idx
    #json += '"rootfs":["/hdd/sdd/SystemDebian9.qcow2"], '
    json += '"rootfs":["/hdd/vda/qemu001.sys.qcow2"], '
    json += '"cdroms":["/hdd/vda/debian-9.5.0-amd64-netinst.iso"], '
    json += '"nethwaddr":"01:20:99:08:19:%02d", ' % idx
    json += '"memory":512, '
    json += '"smp":2,'
    json += '}'
    rst.response_output(out_format, rst.http_post_dao_by_key(hostname, key, json))

def get_qemu_cfg(out_format, hostname, key):
    rst.response_output(out_format, rst.http_get_dao_by_key(hostname, 'qemu_count'))
    rst.response_output(out_format, rst.http_get_dao_by_key(hostname, 'qemu_1'))
    rst.response_output(out_format, rst.http_get_dao_by_key(hostname, 'qemu_2'))
    rst.response_output(out_format, rst.http_get_dao_by_key(hostname, 'qemu_3'))

def start_qemu(out_format, hostname, idx):
    payload = '{'
    payload += '"ops":"start_qemu",'
    payload += '"index":%d' % idx
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def stop_qemu(out_format, hostname, idx):
    payload = '{'
    payload += '"ops":"qmp"'
    payload += ', '
    payload += '"index":%d' % idx
    payload += ', '
    payload += '"action":128'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_payload(hostname, payload))

def add_harddisk(out_format, hostname):
    payload = '{'
    payload += '"ops":"add_qemu_img",'
    payload += '"format":"qcow2",'
    payload += '"disk_path":"/hdd/vda/qemu001.sys.qcow2",'
    payload += '"size_uint":"G",'
    payload += '"size":"2",'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def query_version(out_format, hostname, idx):
    payload = '{'
    payload += '"ops":"qmp"'
    payload += ', '
    payload += '"index":%d' % idx
    payload += ', '
    payload += '"action":0'
    payload += '}'
    rst.response_output(out_format, rst.http_post_rfb_by_payload(hostname, payload))

def request_list(hostname, out_format, action):
    idx = 1
    enable = 1
    post_qemu_cfg(out_format, hostname, idx, enable)
    if action == "start" :
        time.sleep(1)
        start_qemu(out_format, hostname, idx)
    if action == "stop" :
        stop_qemu(out_format, hostname, idx)
    if action == "add_harddisk" :
        add_harddisk(out_format, hostname)
    if action == "query-version" :
        query_version(out_format, hostname, idx - 1)
    if action == "get" :
        get_qemu_cfg(out_format, hostname, idx)

def help_usage():
    rst.out("rest_cli.py <hostname> <action>")
    rst.out("  action: start, stop, add_harddisk, query-version, get")
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    action=sys.argv[2]

    request_list(hostname, 'json', action)

