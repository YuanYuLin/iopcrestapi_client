#!/usr/bin/python2.7

import sys
import time
import libiopc_rest as rst

def debug_env(out_format, hostname):
    payload = '{'
    payload += '"ops":"debug_env",'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def set_env(out_format, hostname):
    payload = '{'
    payload += '"ops":"setenv",'
    payload += '"env":"PATH=/sbin:/usr/sbin:/bin:/usr/bin"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

action_list=[
        {"NAME":"debug_env",   "FUNCTION":debug_env},
        {"NAME":"set_env",   "FUNCTION":set_env},
]

def request_list(hostname, out_format, action):
    for act in action_list:
        if action == act["NAME"] :
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

