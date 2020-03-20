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

def set_authname(out_format, hostname):
    payload = '{'
    payload += '"ops":"set_authname",'
    payload += '"name":"helloworld"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def set_authsalt(out_format, hostname):
    payload = '{'
    payload += '"ops":"set_authsalt",'
    payload += '"salt":"$6$01234$56789"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def set_authhash(out_format, hostname):
    payload = '{'
    payload += '"ops":"set_authhash",'
    payload += '"hash":"$6$01234$40kDc/J3OMiWCRafMKQjAU5M6wAgEnKlhpsqFn8t.koNyBcRSguYQwLkIS90F2uHIc7hBPp.HSgCNgl8F955X/"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def start_ssh(out_format, hostname):
    #
    # curl -d '{"ops":"start_ssh"}' -H "Content-Type: application/json; charset=utf-8" -A 'iopc-app' -X POST http://<IP_ADDRESS>/api/v1/ops
    #
    payload = '{'
    payload += '"ops":"start_ssh"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def stop_ssh(out_format, hostname):
    payload = '{'
    payload += '"ops":"stop_ssh"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def gen_start_ssh(out_format, hostname):
    gen_ssh_key(out_format, hostname)
    get_status_until_key_generated(out_format, hostname)
    start_ssh(out_format, hostname)

action_list=[
{"NAME":"genkey",       "FUNCTION":gen_ssh_key},
{"NAME":"gen_start_ssh","FUNCTION":gen_start_ssh},
{"NAME":"start",        "FUNCTION":start_ssh},
{"NAME":"stop",         "FUNCTION":stop_ssh},
{"NAME":"set_authname", "FUNCTION":set_authname},
{"NAME":"set_authsalt", "FUNCTION":set_authsalt},
{"NAME":"set_authhash", "FUNCTION":set_authhash},
]

def request_list(hostname, out_format, action):
    for act in action_list:
        if action == act["NAME"] and act["FUNCTION"]:
            act["FUNCTION"](out_format, hostname)

def help_usage():
    rst.out("rest_cli.py <hostname> <action>")
    rst.out("action:")
    for act in action_list:
        rst.out("    %s," % act["NAME"])
    #rst.out("  action: format_btrfs_raid1, mount_btrfs_raid1, attach_btrfs_raid1")
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    action=sys.argv[2]

    request_list(hostname, 'json', action)

