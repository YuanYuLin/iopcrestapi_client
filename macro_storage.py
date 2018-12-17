#!/usr/bin/python2.7

import sys
import time
import libiopc_rest as rst

def format_storage_btrfs_raid10(out_format, hostname):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_raid10",'
    payload += '"label":"raid10_000",'
    payload += '"devices":["/dev/vda", "/dev/vdb", "/dev/vdc", "/dev/vdd"]'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def mount_storage_btrfs_raid10(out_format, hostname):
    payload = '{'
    payload += '"ops":"mount_storage_ex",'
    payload += '"enable":1,'
    payload += '"type":"btrfs_raid10",'
    payload += '"src":"/dev/vda",'
    payload += '"dst":"/hdd/vda",'
    payload += '"devices":["/dev/vda", "/dev/vdb", "/dev/vdc", "/dev/vdd"]'
    payload += '}'
    rst.response_output(out_format, rst.http_post_ops_by_pyaload(hostname, payload))

def request_list(hostname, out_format, action):
    if action == "format_btrfs_raid10" :
        format_storage_btrfs_raid10(out_format, hostname)
    if action == "mount_btrfs_raid10" :
        mount_storage_btrfs_raid10(out_format, hostname)

def help_usage():
    rst.out("rest_cli.py <hostname> <action>")
    rst.out("  action: format_btrfs_raid10, mount_btrfs_raid10")
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    action=sys.argv[2]

    request_list(hostname, 'json', action)

