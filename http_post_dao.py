#!/usr/bin/python2.7

import pprint
import sys
import json
import libiopc_rest as rst
def set_qemu_cfg(hostname, out_format):
    idx = 1
    key="qemu_%d" % idx
    json = '{'
    json += '"enable":1, '
    json += '"name":"qemu%03d", ' % idx
    json += '"rootfs":["/hdd/data/00_Daily/SystemDebian10.qcow2", "/hdd/data/00_Daily/Data001.qcow2"], '
    json += '"netifcs":[{"hwaddr":"00:20:18:08:19:%02d", "gwifc":"br2"}, {"hwaddr":"00:20:18:08:19:%02d", "gwifc":"br0"}],' % (idx, (idx + 80))
    #json += '"nethwaddr":"00:20:18:08:19:%02d", ' % idx
    #json += '"gwifc":"br2",' 
    json += '"memory":10000, '
    json += '"smp":4,'
    json += '}'

    return rst.http_post_dao_by_key(hostname, key, json)
    #rst.response_output(out_format, rst.http_post_dao_by_key(hostname, key, json))

def set_netifc_count(hostname, out_format):
    key = 'netifc_count'
    json = '['
    json += '"netifc_1",'
    json += '"netifc_2",'
    json += '"netifc_3",'
    json += '"netifc_4",'
    json += '"netifc_5",'
    json += '"netifc_6",'
    json += ']'

    return rst.http_post_dao_by_key(hostname, key, json)
    #rst.response_output(out_format, rst.http_post_dao_by_key(hostname, key, json))

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

    return rst.http_post_dao_by_key(hostname, key, json)
    #rst.response_output(out_format, rst.http_post_dao_by_key(hostname, key, json))

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

    return rst.http_post_dao_by_key(hostname, key, json)
    #rst.response_output(out_format, rst.http_post_dao_by_key(hostname, key, json))

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

    return rst.http_post_dao_by_key(hostname, key, json)
    #rst.response_output(out_format, rst.http_post_dao_by_key(hostname, key, json))

action_list=[
{"NAME":"set_qemu_cfg",	        "FUNCTION":set_qemu_cfg},
{"NAME":"set_netifc_count",	"FUNCTION":set_netifc_count},
{"NAME":"set_netifc_5",	        "FUNCTION":set_netifc_5},
{"NAME":"set_netifc_6",	        "FUNCTION":set_netifc_6},
{"NAME":"set_storage_2",	"FUNCTION":set_storage_2}
]

def request_list(hostname, out_format, action):
    for act in action_list:
        if action == act["NAME"] and act["FUNCTION"]:
            status_code, json_objs = act["FUNCTION"](hostname, out_format)
            if status_code == 200:
                pprint.pprint(json_objs)
            else:
                print "sub request error: %s" % obj
        else:
            print ""

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

