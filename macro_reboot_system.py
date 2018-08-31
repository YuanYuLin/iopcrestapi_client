#!/usr/bin/python2.7

import sys
import libiopc_rest as rst

def sys_reboot(out_format, hostname):
    payload = '{'
    payload += '"ops":"reboot_system",'
    payload += '"magic":"aa55"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def request_list(hostname, out_format, action):
    sys_reboot(out_format, hostname)

def help_usage():
    print "rest_cli.py <hostname> <action>"
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]
    action = sys.argv[2]

    request_list(hostname, 'json', action)

