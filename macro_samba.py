#!/usr/bin/python2.7

import sys
import time
import pprint
import libiopc_rest as rst

def start_samba(hostname, out_format):
    payload = '{'
    payload += '"ops":"start_samba"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def stop_samba(hostname, out_format):
    payload = '{'
    payload += '"ops":"stop_samba"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

action_list=[
{"NAME":"start_samba",   "FUNCTION":start_samba},
{"NAME":"stop_samba",   "FUNCTION":stop_samba},
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

