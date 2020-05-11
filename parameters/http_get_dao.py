#!/usr/bin/python2.7

import requests
import pprint
import sys
import json
import libiopc_rest as rst
def hello(hostname, options):
    return ""

def func_get_dao_by_key(hostname, options):
    if options == None :
        rst.out("keys:")
        rst.out("    netifc_count ,")
        rst.out("    storage_count ,")
        rst.out("    lxc_count ,")
        rst.out("    qemu_count ,")
        rst.out("    samba_count ,")
        rst.out("    sysinit_count ,")
        rst.out("    misc_count ,")
        rst.out("    rfb_count ,")
        sys.exit(1)

    key = options[0]
    return rst.http_get_dao_by_key(hostname, key)

