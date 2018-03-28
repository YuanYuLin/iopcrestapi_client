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

def get_status(hostname, status_id):
    url='http://' + hostname + '/api/v1/status/?id=' + str(status_id)
    rsp=requests.get(url)
    return rsp

def response_output(out_format, rsp):
    print "response status code"
    print rsp.status_code
    pprint.pprint(rsp.json())

def gen_ssh_key(hostname):
    payload = '{'
    payload += '"ops":"gen_ssh_key"'
    payload += '}'
    return http_request(hostname, payload)

def get_status_until_key_generated(hostname):
    ssh_status_id = 2
    while True :
        rsp = get_status(hostname, ssh_status_id)
        if int(rsp.status_code) == 200 :
            obj = rsp.json()
            if (obj['status'] | 0x01) == 0x01:
                print obj['status']
                return rsp
        time.sleep(2)

def start_ssh(hostname):
    payload = '{'
    payload += '"ops":"start_ssh"'
    payload += '}'
    return http_request(hostname, payload)

def request_list(hostname, out_format):
    response_output(out_format, gen_ssh_key(hostname))
    response_output(out_format, get_status_until_key_generated(hostname))
    response_output(out_format, start_ssh(hostname))

def help_usage():
    print "rest_cli.py <hostname>"
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    request_list(hostname, 'json')

