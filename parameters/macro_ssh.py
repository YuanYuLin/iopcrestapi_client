#!/usr/bin/python2.7

import libiopc_rest as rst

def func_gen_ssh_key(hostname, options):
    payload = '{'
    payload += '"ops":"gen_ssh_key"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_set_env(hostname, options):
    payload = '{'
    payload += '"ops":"setenv",'
    payload += '"env":"SSH_AUTH_NAME=mehlow"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_start_ssh(hostname, options):
    #
    # curl -d '{"ops":"start_ssh"}' -H "Content-Type: application/json; charset=utf-8" -A 'iopc-app' -X POST http://<IP_ADDRESS>/api/v1/ops
    #
    payload = '{'
    payload += '"ops":"start_ssh"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_stop_ssh(hostname, options):
    payload = '{'
    payload += '"ops":"stop_ssh"'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

