#!/usr/bin/python2.7

import sys
import time
import libiopc_rest as rst

def start_rfb(out_format, hostname, index):
    payload = '{'
    payload += '"ops":"rfb"'
    payload += '"index":%d' % index
    payload += ', '
    payload += '"action":1'
    payload += '}'
    rst.response_output(out_format, rst.http_post_rfb_by_payload(hostname, payload))

def stop_rfb(out_format, hostname, index):
    payload = '{'
    payload += '"ops":"rfb"'
    payload += '"index":%d' % index
    payload += ', '
    payload += '"action":2'
    payload += '}'
    rst.response_output(out_format, rst.http_post_rfb_by_payload(hostname, payload))

def set_rfb_dao(out_format, hostname, index):
    json = '{'
    json += '"type": "tcp_ip",'
    json += '"host":"192.168.1.112",'
    json += '"port":5900'
    json += '}'

    rfb = 'rfb_%d' % (index+1)
    rst.response_output(out_format, rst.http_post_dao_by_key(hostname, rfb, json))

def request_list(hostname, out_format, index, action):
    set_rfb_dao(out_format, hostname, index)
    if action == 'stop':
        stop_rfb(out_format, hostname, index)
    if action == 'start':
        start_rfb(out_format, hostname, index)

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

