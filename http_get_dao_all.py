#!/usr/bin/python2.7

import requests
import pprint
import sys
import json

def http_request(hostname, key):
    url='http://' + hostname + '/api/v1/dao/?key=' + key
    print url
    #http://192.168.1.115/api/v1/raw/2/1
    rsp=requests.get(url)
    return rsp.status_code, rsp.json()

def http_response(rsp):
    status_code = rsp.status_code
    json = rsp.json()
    return status_code, json

action_list=[
{"NAME":"netifc_count"},
{"NAME":"storage_count"},
{"NAME":"lxc_count"},
{"NAME":"qemu_count"},
{"NAME":"rfb_count"},
{"NAME":"samba_count"},
{"NAME":"sysinit_count"},
{"NAME":"misc_count"},
]

def request_list(hostname, out_format):
    for action in action_list:
        status_code, json_objs = http_request(hostname, action["NAME"])
        if status_code == 200 :
            for obj in json_objs:
               status_code, json_objs = http_request(hostname, obj)
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

