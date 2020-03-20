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

action_list=[
{"EN": 1, "NAME":"netifc_count"},
{"EN": 0, "NAME":"storage_count"},
{"EN": 0, "NAME":"lxc_count"},
{"EN": 1, "NAME":"qemu_count"},
{"EN": 0, "NAME":"rfb_count"},
{"EN": 0, "NAME":"samba_count"},
{"EN": 1, "NAME":"sysinit_count"},
{"EN": 0, "NAME":"misc_count"},
]

def request_list(hostname, out_format):
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

def help_usage():
    print "rest_cli.py <hostname>"
    sys.exit(1)

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    request_list(hostname, 'json')

