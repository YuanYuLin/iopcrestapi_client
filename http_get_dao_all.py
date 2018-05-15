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
    print rsp.status_code
    pprint.pprint(rsp.json())

def request_list(hostname, out_format):
    response_output(out_format, http_request(hostname, 'config_version'))
    response_output(out_format, http_request(hostname, 'netifc_count'))
    response_output(out_format, http_request(hostname, 'netifc_1'))
    response_output(out_format, http_request(hostname, 'netifc_2'))
    response_output(out_format, http_request(hostname, 'netifc_3'))
    response_output(out_format, http_request(hostname, 'netifc_4'))
    response_output(out_format, http_request(hostname, 'storage_count'))
    response_output(out_format, http_request(hostname, 'storage_1'))
    response_output(out_format, http_request(hostname, 'storage_2'))
    response_output(out_format, http_request(hostname, 'lxc_count'))
    response_output(out_format, http_request(hostname, 'lxc_1'))
    response_output(out_format, http_request(hostname, 'lxc_2'))
    response_output(out_format, http_request(hostname, 'lxc_3'))
    response_output(out_format, http_request(hostname, 'lxc_4'))
    response_output(out_format, http_request(hostname, 'hostname_cfg'))
    response_output(out_format, http_request(hostname, 'drbd_cfg'))

def help_usage():
    print "rest_cli.py <hostname>"
    sys.exit(1)

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    request_list(hostname, 'json')

