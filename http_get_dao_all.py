#!/usr/bin/python2.7

import requests
import pprint
import sys
import json
import libiopc_rest as rst

def http_request(hostname, key):
    url='http://' + hostname + '/api/v1/dao/?key=' + key
    print url
    #http://192.168.1.115/api/v1/raw/2/1
    rsp=requests.get(url)
    return rsp.status_code, rsp.json()

def get_dao_by_key(hostname, key):
    return rst.http_get_dao_by_key(hostname, key)

def get_dao_by_netifc(hostname, out_format):
    key = "netifc_count"
    return get_dao_by_key(hostname, key)

def get_dao_by_storage(hostname, out_format):
    key = "storage_count"
    return get_dao_by_key(hostname, key)

def get_dao_by_lxc(hostname, out_format):
    key = "lxc_count"
    return get_dao_by_key(hostname, key)

def get_dao_by_qemu(hostname, out_format):
    key = "qemu_count"
    return get_dao_by_key(hostname, key)

def get_dao_by_rfb(hostname, out_format):
    key = "rfb_count"
    return get_dao_by_key(hostname, key)

def get_dao_by_samba(hostname, out_format):
    key = "samba_count"
    return get_dao_by_key(hostname, key)

def get_dao_by_sysinit(hostname, out_format):
    key = "sysinit_count"
    return get_dao_by_key(hostname, key)

def get_dao_by_misc(hostname, out_format):
    key = "misc_count"
    return get_dao_by_key(hostname, key)

action_list=[
{"EN": 1, "NAME":"netifc", "FUNCTION":get_dao_by_netifc},
{"EN": 0, "NAME":"storage", "FUNCTION":get_dao_by_storage},
{"EN": 0, "NAME":"lxc", "FUNCTION":get_dao_by_lxc},
{"EN": 1, "NAME":"qemu", "FUNCTION":get_dao_by_qemu},
{"EN": 0, "NAME":"rfb", "FUNCTION":get_dao_by_rfb},
{"EN": 0, "NAME":"samba", "FUNCTION":get_dao_by_samba},
{"EN": 1, "NAME":"sysinit", "FUNCTION":get_dao_by_sysinit},
{"EN": 0, "NAME":"misc", "FUNCTION":get_dao_by_misc},
]

def request_list(hostname, out_format, action):
    isFound = False
    status_code = 0
    json_objs = None
    for act in action_list:
        if action == act["NAME"] and act["FUNCTION"]:
            status_code, json_objs = act["FUNCTION"](hostname, out_format)
            isFound = True

    if isFound == False :
        status_code, json_objs = get_dao_by_key(hostname, action)

    if status_code == 200:
        pprint.pprint(json_objs)
    else:
        print "sub request error: %s" % obj
'''
    for action in action_list:
        if action["EN"] != 1 :
            continue

        status_code, json_objs = rst.http_get_dao_by_key(hostname, action["NAME"])
        if status_code == 200 :
            for obj in json_objs:
               status_code, json_objs = rst.http_get_dao_by_key(hostname, obj)
               if status_code == 200:
                   pprint.pprint(json_objs)
               else:
                   print "sub request error: %s" % obj
        else:
            print "request error: %s" % action["NAME"]
'''

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

