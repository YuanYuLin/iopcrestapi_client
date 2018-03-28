#!/usr/bin/python2.7

import requests
import pprint
import sys
import json

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

def request_list(hostname, out_format, is_master):
    start_drbd = '{'
    start_drbd += '"ops":"start_drbd",'
    start_drbd += '"is_master":' + is_master +','
    start_drbd += '"mounted_dir":"/hdd/drbd"'
    start_drbd += '}'
    response_output(out_format, http_request(hostname, start_drbd))

def help_usage():
    print "rest_cli.py <hostname> <is_master>"
    print "  is_master:"
    print "    0: slave"
    print "    1: master"
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    is_master=sys.argv[2]

    request_list(hostname, 'json', is_master)

