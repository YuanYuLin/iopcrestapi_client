#!/usr/bin/python2.7

import libiopc_rest as rst

def func_debug_env(hostname, options):
    payload = '{'
    payload += '"ops":"debug_env",'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_set_env(hostname, options):
    payload = '{'
    payload += '"ops":"setenv",'
    payload += '"env":"PATH=/sbin:/usr/sbin:/bin:/usr/bin"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_set_home(hostname, options):
    payload = '{'
    payload += '"ops":"setenv",'
    payload += '"env":"HOME=/tmp/lighttpd/www/htdocs"'
    pyaload += '}'
