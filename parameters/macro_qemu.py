#!/usr/bin/pyth2.7

import libiopc_rest as rst

def func_add_img(hostname, options):
    payload = '{'
    payload += '"ops":"add_qemu_img",'
    payload += '"format":"qcow2",'
    payload += '"disk_path":"/hdd/data/00_Daily/SystemDebian9.qcow2",'
    payload += '"size":30,'
    #payload += '"disk_path":"/hdd/data/00_Daily/Data002.qcow2",'
    #payload += '"size":200,'
    payload += '"size_unit":"G",'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_start_qemu(hostname, options):
    idx = 0
    payload = '{'
    payload += '"ops":"start_qemu",'
    payload += '"qemu_index":%d' % idx
    payload += '}'

    return rst.http_post_ops_by_pyaload(hostname, payload)

