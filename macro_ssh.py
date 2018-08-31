#!/usr/bin/python2.7

import sys
import time
import libiopc_rest as rst

def gen_ssh_key(out_format, hostname):
    payload = '{'
    payload += '"ops":"gen_ssh_key"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def get_status_until_key_generated(out_format, hostname):
    ssh_status_id = 2
    while True :
        rsp = rst.http_get_status(hostname, ssh_status_id)
        if int(rsp.status_code) == 200 :
            obj = rsp.json()
            if (obj['status'] | 0x01) == 0x01:
                rst.response_output(out_format, rsp)
                return 
        time.sleep(2)

def start_ssh(out_format, hostname):
    payload = '{'
    payload += '"ops":"start_ssh"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def stop_ssh(out_format, hostname):
    payload = '{'
    payload += '"ops":"stop_ssh"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def request_list(hostname, out_format, action):
    if action == 'start':
        gen_ssh_key(out_format, hostname)
        get_status_until_key_generated(out_format, hostname)
        start_ssh(out_format, hostname)
    if action == 'stop':
        stop_ssh(out_format, hostname)

def help_usage():
    print "rest_cli.py <hostname> <action>"
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    action=sys.argv[2]

    request_list(hostname, 'json', action)

