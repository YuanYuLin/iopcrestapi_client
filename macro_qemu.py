#!/usr/bin/python2.7

import requests
import pprint
import sys
import json
import time

def http_request(hostname, payload):
    url='http://' + hostname + '/api/v1/ops'
    print url
    headers = {'content-type':'application/json; charset=utf-8', 'user-agent':'iopc-app'}
    rsp=requests.post(url, headers=headers, data=payload)
    return rsp

def http_request_by_key(hostname, key, payload):
    url='http://' + hostname + '/api/v1/dao/?key=' + key
    print url
    headers = {'content-type':'application/json; charset=utf-8', 'user-agent':'iopc-app'}
    rsp=requests.post(url, headers=headers, data=payload)
    return rsp

def response_output(out_format, rsp):
    print "response status code"
    print rsp.status_code
    pprint.pprint(rsp.json())

def post_qemu_cfg(hostname, idx, enable):
    key="qemu_%d" % idx
    json = '{'
    json += '"enable":%d, ' % enable
    json += '"name":"qemu%03d", ' % idx
    json += '"rootfs":"/hdd/sdb/qemu%03d.sys.qcow2", ' % idx
    json += '"nethwaddr":"01:19:82:03:21:%02d", ' % idx
    json += '"memory":1024'
    json += '}'
    return http_request_by_key(hostname, 'key', json)

def gen_lxc_cfg(hostname):
    payload = '{'
    payload += '"ops":"gen_lxc_cfg",'
    payload += '"index":1'
    payload += '}'
    return http_request(hostname, payload)

def start_qemu(hostname, idx):
    payload = '{'
    payload += '"ops":"start_qemu",'
    payload += '"index":%d' % idx
    payload += '}'
    return http_request(hostname, payload)

def request_list(hostname, out_format, action):
    idx = 1
    enable = 1
    if action == "start" :
        response_output(out_format, post_qemu_cfg(hostname, idx, enable))
        #response_output(out_format, gen_lxc_cfg(hostname))
        time.sleep(1)
        response_output(out_format, start_qemu(hostname, idx))
    if action == "stop" :
        print "Not supported, now..."

def help_usage():
    print "rest_cli.py <hostname> <action>"
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    action=sys.argv[2]

    request_list(hostname, 'json', action)

