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

def http_request_dao(hostname, key, payload):
    url='http://' + hostname + '/api/v1/dao/?key=' + key
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

def start_rfb(hostname, index):
    payload = '{'
    payload += '"index":%d' % index
    payload += ', '
    payload += '"action":1'
    payload += '}'
    return http_request_rfb(hostname, payload)

def  stop_rfb(hostname, index):
    payload = '{'
    payload += '"index":%d' % index
    payload += ', '
    payload += '"action":2'
    payload += '}'
    return http_request_rfb(hostname, payload)

def set_rfb_dao(hostname, index):
    json = '{'
    json += '"type": "tcp_ip",'
    json += '"host":"192.168.1.112",'
    json += '"port":5900'
    json += '}'

    rfb = 'rfb_%d' % (index+1)
    return http_request_dao(hostname, rfb, json)

def request_list(hostname, out_format, index, action):
    response_output(out_format, set_rfb_dao(hostname, index))
    if action == 'stop':
        response_output(out_format, stop_rfb(hostname, index))
    if action == 'start':
        response_output(out_format, start_rfb(hostname, index))

def help_usage():
    print "rest_cli.py <hostname> <index> <action>"
    print "  <index> : 0 ~ N"
    print "  <action>: start, stop"
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    index=int(sys.argv[2])
    action=sys.argv[3]

    request_list(hostname, 'json', index, action)

