#!/usr/bin/python2.7

import requests
import pprint
import sys
import json
import time
import libiopc_rest as rst

def http_request_rfb(hostname, payload):
    url='http://' + hostname + '/api/v1/rfb'
    rst.debug(url)
    headers = {'content-type':'application/json; charset=utf-8', 'user-agent':'iopc-app'}
    rsp=requests.post(url, headers=headers, data=payload)
    return rsp

def http_request(hostname, payload):
    url='http://' + hostname + '/api/v1/ops'
    rst.debug(url)
    headers = {'content-type':'application/json; charset=utf-8', 'user-agent':'iopc-app'}
    rsp=requests.post(url, headers=headers, data=payload)
    return rsp

def http_request_by_key(hostname, key, payload):
    url='http://' + hostname + '/api/v1/dao/?key=' + key
    rst.debug(url)
    headers = {'content-type':'application/json; charset=utf-8', 'user-agent':'iopc-app'}
    rsp=requests.post(url, headers=headers, data=payload)
    return rsp

def response_output(out_format, rsp):
    rst.debug("response status code")
    rst.debug(rsp.status_code)
    pprint.pprint(rsp.json())

def post_qemu_cfg(hostname, idx, enable):
    key="qemu_%d" % idx
    json = '{'
    json += '"enable":%d, ' % enable
    json += '"name":"qemu%03d", ' % idx
    json += '"rootfs":"/hdd/sdb/SystemDebian9.qcow2", '
    json += '"nethwaddr":"00:20:18:08:19:%02d", ' % idx
    json += '"memory":4096'
    json += '}'
    return http_request_by_key(hostname, key, json)

def start_qemu(hostname, idx):
    payload = '{'
    payload += '"ops":"start_qemu",'
    payload += '"index":%d' % idx
    payload += '}'
    return http_request(hostname, payload)

def stop_qemu(hostname, idx):
    payload = '{'
    payload += '"ops":"qmp"'
    payload += ', '
    payload += '"index":%d' % idx
    payload += ', '
    payload += '"action":128'
    payload += '}'
    return http_request_rfb(hostname, payload)

def query_version(hostname, idx):
    payload = '{'
    payload += '"ops":"qmp"'
    payload += ', '
    payload += '"index":%d' % idx
    payload += ', '
    payload += '"action":0'
    payload += '}'
    return http_request_rfb(hostname, payload)

def request_list(hostname, out_format, action):
    idx = 1
    enable = 1
    response_output(out_format, post_qemu_cfg(hostname, idx, enable))
    if action == "start" :
        time.sleep(1)
        response_output(out_format, start_qemu(hostname, idx))
    if action == "stop" :
        response_output(out_format, stop_qemu(hostname, idx))
    if action == "query-version" :
        response_output(out_format, query_version(hostname, idx - 1))

def help_usage():
    rst.out("rest_cli.py <hostname> <action>")
    rst.out("  action: start, stop, query-version")
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    action=sys.argv[2]

    request_list(hostname, 'json', action)

