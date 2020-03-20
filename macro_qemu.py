#!/usr/bin/pyth2.7

import sys
import time
import libiopc_rest as rst

def add_qemu_img(out_format, hostname):
    payload = '{'
    payload += '"ops":"add_qemu_img",'
    payload += '"format":"qcow2",'
    #payload += '"disk_path":"/hdd/data/00_Daily/SystemDebian10.qcow2",'
    payload += '"disk_path":"/hdd/data/00_Daily/Data001.qcow2",'
    payload += '"size_unit":"G",'
    #payload += '"size":30,'
    payload += '"size":200,'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def post_qemu_cfg_debian_j3455m(out_format, hostname, idx, enable):
    key="qemu_%d" % idx
    js = '{'
    js += '"enable":%d, ' % enable
    js += '"name":"qemu%03d", ' % idx
    js += '"rootfs":["/hdd/sdb/SystemDebian9.qcow2", "/hdd/sdb/DataBuildIOPC.qcow2"], '
    js += '"nethwaddr":"00:20:18:08:19:%02d", ' % idx
    js += '"memory":10000, '
    js += '"smp":4,'
    js += '}'
    rst.respse_output(out_format, rst.http_post_dao_by_key(hostname, key, js))

def post_qemu_cfg_win10(out_format, hostname, idx, enable):
    key="qemu_%d" % idx
    js = '{'
    js += '"enable":%d, ' % enable
    js += '"name":"qemu%03d", ' % idx
    js += '"rootfs":["/hdd/sdb/Win10.qcow2"], '
    js += '"nethwaddr":"00:20:18:08:19:%02d", ' % idx
    js += '"memory":4096, '
    js += '"smp":2,'
    js += '}'
    rst.respse_output(out_format, rst.http_post_dao_by_key(hostname, key, js))

def post_qemu_cfg_debian_stock(out_format, hostname, idx, enable):
    key="qemu_%d" % idx
    js = '{'
    js += '"enable":%d, ' % enable
    js += '"name":"qemu%03d", ' % idx
    js += '"rootfs":["/hdd/sdb/SystemDebian9Stock.qcow2", "/hdd/sdb/DataStock.qcow2"], '
    js += '"nethwaddr":"00:20:18:08:19:%02d", ' % idx
    js += '"memory":128, '
    js += '"smp":1,'
    js += '}'
    rst.respse_output(out_format, rst.http_post_dao_by_key(hostname, key, js))

def start_qemu(out_format, hostname):
    idx = 1
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
{"EN": 1, "NAME":"start_qemu",	"FUNCTION":start_qemu},
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

def help_usage():
    rst.out("rest_cli.py <hostname> <action>")
    rst.out("action:")
    for act in action_list:
        rst.out("    %s," % act["NAME"])
    sys.exit(1)
'''
def request_list(hostname, out_format, acti):
    if acti == "start_qemu":
        idx = 1
        status_code, json_objs = start_qemu(out_format, hostname, idx)
        if status_code == 200:
            pprint.pprint(json_objs)
        else:
            print "sub request error: %s" % obj

    if acti == "start_1" :
        idx = 1
        post_qemu_cfg_debian_j3455m(out_format, hostname, idx, 1)
        time.sleep(1)
        start_qemu(out_format, hostname, idx)
    if acti == "start_2" :
        idx = 2
        post_qemu_cfg_win10(out_format, hostname, idx, 1)
        time.sleep(1)
        start_qemu(out_format, hostname, idx)
    if acti == "start_3" :
        idx = 3
        post_qemu_cfg_debian_stock(out_format, hostname, idx, 1)
        time.sleep(1)
        start_qemu(out_format, hostname, idx)
    if acti == "stop" :
        stop_qemu(out_format, hostname, idx)
    if acti == "add_qemu_img" :
        add_qemu_img(out_format, hostname)
    if acti == "query-versi" :
        query_versi(out_format, hostname, idx - 1)

def help_usage():
    rst.out("rest_cli.py <hostname> <acti>")
    rst.out("  acti: start_<index>, stop_<index>, add_qemu_img, query-versi")
    sys.exit(1)
'''
if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    acti=sys.argv[2]

    request_list(hostname, 'js')

