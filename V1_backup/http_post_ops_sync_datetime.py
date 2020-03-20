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

def request_list(hostname, out_format, ntp_server):
    payload = '{'
    payload += '"ops":"sync_datetime",'
    payload += '"ntp_server":' + ntp_server +','
    payload += '}'
    response_output(out_format, http_request(hostname, payload))

def help_usage():
    print "rest_cli.py <hostname> <ntp_server>"
    print "  ntp_server:"
    print "    tock.stdtime.gov.tw"
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    ntp_server=sys.argv[2]

    request_list(hostname, 'json', ntp_server)

