#!/usr/bin/python2.7

import sys
import time
import libiopc_rest as rst

def get_samba_cfg(out_format, hostname):
    rst.response_output(out_format, rst.http_get_dao_by_key(hostname, 'samba_count'))
    rst.response_output(out_format, rst.http_get_dao_by_key(hostname, 'samba_1'))
    rst.response_output(out_format, rst.http_get_dao_by_key(hostname, 'samba_2'))
    rst.response_output(out_format, rst.http_get_dao_by_key(hostname, 'samba_3'))

def post_samba_cfg(out_format, hostname):
    enable = 1
    idx = 1
    key="samba_%d" % idx
    json = '{'
    json += '"enable":%d, ' % enable
    json += '"type":"global", '
    json += '"name":"samba%d", ' % idx
    json += '"path":"", '
    json += '}'
    rst.response_output(out_format, rst.http_post_dao_by_key(hostname, key, json))

    idx = 2
    key="samba_%d" % idx
    json = '{'
    json += '"enable":%d, ' % enable
    json += '"type":"shrdir", '
    json += '"name":"samba%d", ' % idx
    json += '"path":"/tmp", '
    json += '}'
    rst.response_output(out_format, rst.http_post_dao_by_key(hostname, key, json))

    idx = 3
    key="samba_%d" % idx
    json = '{'
    json += '"enable":%d, ' % enable
    json += '"type":"shrdir", '
    json += '"name":"samba%d", ' % idx
    json += '"path":"/hdd", '
    json += '}'
    rst.response_output(out_format, rst.http_post_dao_by_key(hostname, key, json))

def start_samba(out_format, hostname):
    payload = '{'
    payload += '"ops":"start_samba"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def stop_samba(out_format, hostname):
    payload = '{'
    payload += '"ops":"stop_samba"'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def request_list(hostname, out_format, action):
    post_samba_cfg(out_format, hostname)
    if action == "start" :
        time.sleep(1)
        start_samba(out_format, hostname)
    if action == "stop" :
        stop_samba(out_format, hostname)
    if action == "get" :
        get_samba_cfg(out_format, hostname)

def help_usage():
    rst.out("rest_cli.py <hostname> <action>")
    rst.out("  action: start, stop, query-version")
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    action=sys.argv[2]

    request_list(hostname, 'json', action)

