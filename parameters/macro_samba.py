#!/usr/bin/python2.7

import libiopc_rest as rst

def func_start_samba(hostname, options):
    payload = '{'
    payload += '"ops":"start_samba"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_stop_samba(hostname, options):
    payload = '{'
    payload += '"ops":"stop_samba"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

