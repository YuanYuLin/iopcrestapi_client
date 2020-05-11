#!/usr/bin/python2.7

import libiopc_rest as rst

def func_init_mlnet(hostname, options):
    payload = '{'
    payload += '"ops":"init_mldonkey"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_start_mlnet(hostname, options):
    payload = '{'
    payload += '"ops":"start_mldonkey"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_stop_mlnet(hostname, options):
    payload = '{'
    payload += '"ops":"stop_mldonkey"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

