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
    return http_request_by_key(hostname, key, json)

def gen_lxc_cfg(hostname, idx):
    payload = '{'
    payload += '"ops":"gen_lxc_cfg",'
    payload += '"index":%d' % idx
    payload += '}'
    return http_request(hostname, payload)

def start_lxc(hostname, idx):
    payload = '{'
    payload += '"ops":"start_lxc",'
    payload += '"index":%d' % idx
    payload += '}'
    return http_request(hostname, payload)

def request_list(hostname, out_format):
    idx = 1
    enable = 1
    response_output(out_format, post_lxc_cfg(hostname, idx, enable))
    response_output(out_format, gen_lxc_cfg(hostname, idx))
    time.sleep(1)
    response_output(out_format, start_lxc(hostname, idx))

def help_usage():
    print "rest_cli.py <hostname>"
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    request_list(hostname, 'json')

