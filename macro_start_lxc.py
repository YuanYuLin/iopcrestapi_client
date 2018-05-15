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

def response_output(out_format, rsp):
    print "response status code"
    print rsp.status_code
    pprint.pprint(rsp.json())

def gen_lxc_cfg(hostname):
    payload = '{'
    payload += '"ops":"gen_lxc_cfg",'
    payload += '"index":1'
    payload += '}'
    return http_request(hostname, payload)

def request_list(hostname, out_format):
    response_output(out_format, gen_lxc_cfg(hostname))

def help_usage():
    print "rest_cli.py <hostname>"
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    request_list(hostname, 'json')

