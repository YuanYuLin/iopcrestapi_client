#!/usr/bin/python2.7

import requests
import pprint
import sys
import json

def http_request(hostname, key, payload):
    url='http://' + hostname + '/api/v1/dao/?key=' + key
    print url
    headers = {'content-type':'application/json; charset=utf-8', 'user-agent':'iopc-app'}
    rsp=requests.post(url, headers=headers, data=payload)
    return rsp

def response_output(out_format, rsp):
    print rsp.status_code
    print rsp.text
    pprint.pprint(rsp.json())

def set_qemu_cfg(hostname, out_format):
    idx = 1
    key="qemu_%d" % idx
    json = '{'
    json += '"enable":1, '
    json += '"name":"qemu%03d", ' % idx
    json += '"rootfs":["/hdd/data/00_Daily/SystemDebian10.qcow2", "/hdd/data/00_Daily/Data001.qcow2"], '
    json += '"netifcs":[{"hwaddr":"00:20:18:08:19:%02d", "gwifc":"br2"}, {"hwaddr":"00:20:18:08:19:%02d", "gwifc":"br0"}],' % idx, (idx + 0x80)
    #json += '"nethwaddr":"00:20:18:08:19:%02d", ' % idx
    #json += '"gwifc":"br2",' 
    json += '"memory":10000, '
    json += '"smp":4,'
    json += '}'

    response_output(out_format, http_request(hostname, key, json))

def set_netifc_count(hostname, out_format):
    key = 'netifc_count'
    json = '['
    json += '"netifc_1",'
    json += '"netifc_2",'
    json += '"netifc_3",'
    json += '"netifc_4",'
    json += '"netifc_5",'
    json += '"netifc_6"'
    json += ']'

    response_output(out_format, http_request(hostname, key, json))

def set_netifc_5(hostname, out_format):
    key = 'netifc_5'
    json = '{'
    json += '"devices": [],'
    json += '"editable": 0,'
    json += '"name": "eth1",'
    json += '"src": "none",'
    json += '"tag": 0,'
    json += '"type": "eth",'
    json += '"visable": 1,'
    json += '"vlan": 0'
    json += '}'

    response_output(out_format, http_request(hostname, key, json))

def set_netifc_6(hostname, out_format):
    key = 'netifc_6'
    json = '{'
    json += '"address": "192.168.70.254",'
    json += '"ctrlport": 1,'
    json += '"devices": ["eth1"],'
    json += '"editable": 1,'
    json += '"hwaddress": "00:19:82:03:21:12",'
    json += '"name": "br2",'
    json += '"netmask": "255.255.255.0",'
    json += '"src": "static",'
    json += '"tag": 0,'
    json += '"type": "bridge",'
    json += '"visable": 1,'
    json += '"vlan": 0'
    json += '}'

    response_output(out_format, http_request(hostname, key, json))

def set_storage_2(hostname, out_format):
    key = 'storage_2'
    json = '{'
    json += '"dst":"/hdd/data",'
    json += '"enable":1,'
    json += '"formatable":0,'
    json += '"label":"RAID1",'
    json += '"src":"/dev/sda",'
    json += '"type":"btrfs_raid1",'
    json += '"visable":1'
    json += '}'

    response_output(out_format, http_request(hostname, key, json))

action_list=[
{"EN": 0, "NAME":"set_qemu_cfg",	"FUNCTION":set_qemu_cfg},
{"EN": 0, "NAME":"set_netifc_count",	"FUNCTION":set_netifc_count},
{"EN": 0, "NAME":"set_netifc_5",	"FUNCTION":set_netifc_5},
{"EN": 0, "NAME":"set_netifc_6",	"FUNCTION":set_netifc_6},
{"EN": 0, "NAME":"set_storage_2",	"FUNCTION":set_storage_2}
]

def request_list(hostname, out_format):
    for act in action_list:
        if action["EN"] != 1 :
            continue

        if action == act["NAME"] and act["FUNCTION"]:
            act["FUNCTION"](out_format, hostname)

def help_usage():
def help_usage():
    rst.out("rest_cli.py <hostname> <action>")
    rst.out("action:")
    for act in action_list:
        rst.out("    %s," % act["NAME"])
    sys.exit(1)

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    request_list(hostname, 'json')
