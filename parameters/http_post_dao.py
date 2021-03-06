#!/usr/bin/python2.7

import libiopc_rest as rst

def func_set_qemu_cfg1(hostname, options):
    idx = 1
    key="qemu_%d" % idx
    json = '{'
    json += '"enable":1, '
    json += '"name":"qemu%03d", ' % idx
    json += '"use_kvm":1,'
    json += '"use_host_cpu:0",'
    json += '"rootfs":["/hdd/data/SystemDebian9.qcow2", "/hdd/data/DataBuildIOPC.qcow2", "/hdd/data/DataBuildIOPC2.qcow2"], '
    json += '"netifcs":[{"hwaddr":"00:20:18:08:19:%02d", "gwifc":"br2"}, {"hwaddr":"00:20:18:08:19:%02d", "gwifc":"br0"}],' % (idx, (idx + 80))
    json += '"memory":10000, '
    json += '"smp":4,'
    json += '}'

    return rst.http_post_dao_by_key(hostname, key, json)

def func_set_qemu_cfg2(hostname, options):
    idx = 2
    key="qemu_%d" % idx
    json = '{'
    json += '"enable":1, '
    json += '"name":"qemu%03d", ' % idx
    json += '"use_kvm":1,'
    json += '"use_host_cpu:0",'
    json += '"rootfs":["/hdd/data/00_Daily/SystemDebian9.qcow2", "/hdd/data/00_Daily/Data002.qcow2"], '
    json += '"netifcs":[{"hwaddr":"00:20:18:08:19:%02d", "gwifc":"br2"}, {"hwaddr":"00:20:18:08:19:%02d", "gwifc":"br0"}],' % (idx, (idx + 80))
    json += '"memory":10000, '
    json += '"smp":4,'
    json += '}'

    return rst.http_post_dao_by_key(hostname, key, json)

def func_set_netifc_count(hostname, options):
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

def func_set_netifc_5(hostname, options):
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

def func_set_netifc_6(hostname, options):
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

def func_set_storage_2(hostname, options):
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

