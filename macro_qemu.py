#!/usr/bin/python2.7

import requests
import pprint
import sys
import json
import time

def http_request_rfb(hostname, payload):
    url='http://' + hostname + '/api/v1/rfb'
    print url
    headers = {'content-type':'application/json; charset=utf-8', 'user-agent':'iopc-app'}
    rsp=requests.post(url, headers=headers, data=payload)
    return rsp

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
    json += '"rootfs":"/hdd/sdd/qemu%03d.sys.qcow2", ' % idx
    json += '"nethwaddr":"00:19:82:03:22:%02d", ' % idx
    json += '"memory":512'
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
        print "AAA"
        response_output(out_format, query_version(hostname, idx - 1))

def help_usage():
    print "rest_cli.py <hostname> <action>"
    print "  action: start, stop, query-version"
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    action=sys.argv[2]

    request_list(hostname, 'json', action)

