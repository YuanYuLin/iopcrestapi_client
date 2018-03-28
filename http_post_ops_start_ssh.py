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

def get_status(hostname, status_id):
    url='http://' + hostname + '/api/v1/status/?id=' + str(status_id)
    print url
    #http://192.168.1.115/api/v1/raw/2/1
    rsp=requests.get(url)
    return rsp

def response_output(out_format, rsp):
    print "response status code"
    print rsp.status_code
    pprint.pprint(rsp.json())

def request_list(hostname, out_format):
    ssh_status_id = 2
    rsp = get_status(hostname, ssh_status_id)
    if int(rsp.status_code) == 200 :
        obj = rsp.json()
        print obj['status'] 
    '''
    payload = '{'
    payload += '"ops":"start_ssh"'
    payload += '}'
    response_output(out_format, http_request(hostname, payload))
    '''
def help_usage():
    print "rest_cli.py <hostname>"
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    request_list(hostname, 'json')

