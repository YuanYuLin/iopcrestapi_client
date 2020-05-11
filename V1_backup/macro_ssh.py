#!/usr/bin/python2.7

import sys
import time
import pprint
import libiopc_rest as rst

def gen_ssh_key(hostname, out_format):
    payload = '{'
    payload += '"ops":"gen_ssh_key"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def get_status_until_key_generated(hostname, out_format):
    ssh_status_id = 2
    while True :
        rsp = rst.http_get_status(hostname, ssh_status_id)
        if int(rsp.status_code) == 200 :
            obj = rsp.json()
            if (obj['status'] | 0x01) == 0x01:
                rst.response_output(out_format, rsp)
                return 
        time.sleep(2)

def set_env(hostname, out_format):
    payload = '{'
    payload += '"ops":"setenv",'
    payload += '"env":"SSH_AUTH_NAME=mehlow"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def set_authname(hostname, out_format):
    payload = '{'
    payload += '"ops":"set_authname",'
    payload += '"name":"helloworld"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def set_authsalt(hostname, out_format):
    payload = '{'
    payload += '"ops":"set_authsalt",'
    payload += '"salt":"$6$01234$56789"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def set_authhash(hostname, out_format):
    payload = '{'
    payload += '"ops":"set_authhash",'
    payload += '"hash":"$6$01234$40kDc/J3OMiWCRafMKQjAU5M6wAgEnKlhpsqFn8t.koNyBcRSguYQwLkIS90F2uHIc7hBPp.HSgCNgl8F955X/"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def start_ssh(hostname, out_format):
    #
    # curl -d '{"ops":"start_ssh"}' -H "Content-Type: application/json; charset=utf-8" -A 'iopc-app' -X POST http://<IP_ADDRESS>/api/v1/ops
    #
    payload = '{'
    payload += '"ops":"start_ssh"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def stop_ssh(hostname, out_format):
    payload = '{'
    payload += '"ops":"stop_ssh"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def gen_start_ssh(hostname, out_format):
    gen_ssh_key(hostname, out_format)
    get_status_until_key_generated(hostname, out_format)
    start_ssh(hostname, out_format)

action_list=[
{"NAME":"set_env",		"FUNCTION":set_env},
{"NAME":"gen_ssh_key",		"FUNCTION":gen_ssh_key},
{"NAME":"start_ssh",		"FUNCTION":start_ssh},
{"NAME":"stop_ssh",             "FUNCTION":stop_ssh},
]

def request_list(hostname, out_format, action):
    for act in action_list:
        if action == act["NAME"] and act["FUNCTION"]:
            status_code, json_objs = act["FUNCTION"](hostname, out_format)
            if status_code == 200:
                pprint.pprint(json_objs)
            else:
                print "sub request error: %s" % obj
        else:
            print ""

def help_usage():
    rst.out("rest_cli.py <hostname> <action>")
    rst.out("action:")
    for act in action_list:
        rst.out("    %s," % act["NAME"])

    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    action=sys.argv[2]

    request_list(hostname, 'json', action)

