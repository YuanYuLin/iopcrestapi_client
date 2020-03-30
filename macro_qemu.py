#!/usr/bin/pyth2.7

import sys
import time
import pprint
import libiopc_rest as rst

def add_img(hostname, out_format):
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

def start_qemu(hostname, out_format):
    idx = 0
    payload = '{'
    payload += '"ops":"start_qemu",'
    payload += '"qemu_index":%d' % idx
    payload += '}'

    return rst.http_post_ops_by_pyaload(hostname, payload)
    #rst.respse_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def stop_qemu(out_format, hostname, idx):
    payload = '{'
    payload += '"ops":"qmp"'
    payload += ', '
    payload += '"index":%d' % idx
    payload += ', '
    payload += '"acti":128'
    payload += '}'
    rst.respse_output(out_format, rst.http_post_rfb_by_payload(hostname, payload))

def query_versi(out_format, hostname, idx):
    payload = '{'
    payload += '"ops":"qmp"'
    payload += ', '
    payload += '"index":%d' % idx
    payload += ', '
    payload += '"acti":0'
    payload += '}'
    rst.respse_output(out_format, rst.http_post_rfb_by_payload(hostname, payload))

action_list=[
{"EN": 1, "NAME":"start_qemu",		"FUNCTION":start_qemu},
{"EN": 0, "NAME":"add_img",		"FUNCTION":add_img},
]

def request_list(hostname, out_format):
    for action in action_list:
        if action["EN"] != 1 :
            continue

        if action["NAME"] and action["FUNCTION"]:
            status_code, json_objs = action["FUNCTION"](hostname, out_format)
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
    acti=sys.argv[2]

    request_list(hostname, 'js')

