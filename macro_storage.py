#!/usr/bin/python2.7

import sys
import time
import libiopc_rest as rst

#g_storage_list = '["/dev/vda", "/dev/vdb"]'
g_storage_list = '["/dev/sda", "/dev/sdb"]'
g_storage_list_attach = '["/dev/vdc"]'
#g_storage_mount = '"/dev/vda"'
g_storage_mount = '"/dev/sda"'
g_storage_mount_dir = '"/hdd/data"'
g_storage_subvol_name = '"test"'

def format_storage_btrfs_raid1(out_format, hostname):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_raid1",'
    payload += '"label":"raid1_000",'
    payload += '"devices":%s' % g_storage_list
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def attach_storage_btrfs_raid1(out_format, hostname):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_raid1_attach_hdd",'
    payload += '"label":"raid1_000",'
    payload += '"mount_dir":%s,' % g_storage_mount_dir
    payload += '"devices":%s' % g_storage_list_attach
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def detach_storage_btrfs_raid1(out_format, hostname):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_raid1_detach_hdd",'
    payload += '"label":"raid1_000",'
    payload += '"mount_dir":%s,' % g_storage_mount_dir
    payload += '"devices":%s' % g_storage_list_attach
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def balance_storage_btrfs_raid1(out_format, hostname):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_raid1_balance_hdd",'
    payload += '"label":"raid1_000",'
    payload += '"mount_dir":%s,' % g_storage_mount_dir
    #payload += '"devices":[]'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def mount_storage_btrfs_raid1(out_format, hostname):
    payload = '{'
    payload += '"ops":"mount_storage_ex",'
    payload += '"enable":1,'
    payload += '"type":"btrfs_raid1",'
    payload += '"label":"raid1_000",'
    payload += '"src":%s,' % g_storage_mount
    payload += '"dst":%s,' % g_storage_mount_dir
    payload += '"devices":[]'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def create_subvolume(out_format, hostname):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_subvolume_create",'
    payload += '"label":"raid1_000",'
    payload += '"mount_dir":%s,' % g_storage_mount_dir
    payload += '"subvolume":%s,' % g_storage_subvol_name
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def delete_subvolume(out_format, hostname):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_subvolume_delete",'
    payload += '"label":"raid1_000",'
    payload += '"mount_dir":%s,' % g_storage_mount_dir
    payload += '"subvolume":%s,' % g_storage_subvol_name
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def snapshot_subvolume(out_format, hostname):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_subvolume_snapshot",'
    payload += '"label":"raid1_000",'
    payload += '"mount_dir":%s,' % g_storage_mount_dir
    payload += '"subvolume":%s,' % g_storage_subvol_name
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

action_list=[
{"NAME":"format_btrfs_raid1",   "FUNCTION":format_storage_btrfs_raid1},
{"NAME":"mount_btrfs_raid1",    "FUNCTION":mount_storage_btrfs_raid1},
{"NAME":"attach_btrfs_raid1",   "FUNCTION":attach_storage_btrfs_raid1},
{"NAME":"detach_btrfs_raid1",   "FUNCTION":detach_storage_btrfs_raid1},
{"NAME":"balance_storage_btrfs_raid1", "FUNCTION":balance_storage_btrfs_raid1},
{"NAME":"create_subvolume",     "FUNCTION":create_subvolume},
{"NAME":"delete_subvolume",     "FUNCTION":delete_subvolume},
{"NAME":"snapshot_subvolume",   "FUNCTION":snapshot_subvolume},
]

def request_list(hostname, out_format, action):
    for act in action_list:
        if action == act["NAME"] and act["FUNCTION"]:
            act["FUNCTION"](out_format, hostname)

def help_usage():
    rst.out("rest_cli.py <hostname> <action>")
    rst.out("action:")
    for act in action_list:
        rst.out("    %s," % act["NAME"])
    #rst.out("  action: format_btrfs_raid1, mount_btrfs_raid1, attach_btrfs_raid1")
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    action=sys.argv[2]

    request_list(hostname, 'json', action)

