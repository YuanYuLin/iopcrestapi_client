#!/usr/bin/python2.7

import requests
import pprint
import sys
import json

def http_request(hostname, key):
    url='http://' + hostname + '/api/v1/dao/?key=' + key
    print url
    #http://192.168.1.115/api/v1/raw/2/1
    rsp=requests.get(url)
    return rsp

def response_output(out_format, rsp):
    if rsp.status_code == requests.codes.ok:
        pprint.pprint(rsp.json())
    else:
        print "error" + str(rsp.status_code)

def request_list(hostname, out_format):
    response_output(out_format, http_request(hostname, 'hostname_cfg'))

def help_usage():
    print "rest_cli.py <hostname>"
    sys.exit(1)

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    request_list(hostname, 'json')

