#!/usr/bin/python2.7

import libiopc_rest as rst

g_storage_list = '["/dev/vda", "/dev/vdb"]'
#g_storage_list = '["/dev/sda", "/dev/sdb"]'
g_storage_list_attach = '["/dev/vdc"]'
g_storage_mount = '"/dev/vda"'
#g_storage_mount = '"/dev/sda"'
g_storage_mount_dir = '"/hdd/data"'
#g_storage_subvol_name = '"00_Daily"'
#g_storage_subvol_name = '"01_Weekly"'
#g_storage_subvol_name = '"02_Monthly"'
g_storage_subvol_name = '"99_Misc"'
#g_storage_subvol_name = '"VMs"'
#g_storage_subvol_name = '"Misc"'

def func_format_storage_btrfs_raid1(hostname, options):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_raid1",'
    payload += '"label":"raid1_000",'
    payload += '"devices":%s' % g_storage_list
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_attach_storage_btrfs_raid1(hostname, options):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_raid1_attach_hdd",'
    payload += '"label":"raid1_000",'
    payload += '"mount_dir":%s,' % g_storage_mount_dir
    payload += '"devices":%s' % g_storage_list_attach
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_detach_storage_btrfs_raid1(hostname, options):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_raid1_detach_hdd",'
    payload += '"label":"raid1_000",'
    payload += '"mount_dir":%s,' % g_storage_mount_dir
    payload += '"devices":%s' % g_storage_list_attach
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_balance_storage_btrfs_raid1(hostname, options):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_raid1_balance_hdd",'
    payload += '"label":"raid1_000",'
    payload += '"mount_dir":%s,' % g_storage_mount_dir
    #payload += '"devices":[]'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_mount_storage_btrfs_raid1(hostname, options):
    payload = '{'
    payload += '"ops":"mount_storage_ex",'
    payload += '"enable":1,'
    payload += '"type":"btrfs_raid1",'
    payload += '"label":"raid1_000",'
    payload += '"src":%s,' % g_storage_mount
    payload += '"dst":%s,' % g_storage_mount_dir
    payload += '"devices":[]'
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_create_subvolume(hostname, options):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_subvolume_create",'
    payload += '"label":"raid1_000",'
    payload += '"mount_dir":%s,' % g_storage_mount_dir
    payload += '"subvolume":%s,' % g_storage_subvol_name
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_delete_subvolume(hostname, options):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_subvolume_delete",'
    payload += '"label":"raid1_000",'
    payload += '"mount_dir":%s,' % g_storage_mount_dir
    payload += '"subvolume":%s,' % g_storage_subvol_name
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

def func_snapshot_subvolume(hostname, options):
    payload = '{'
    payload += '"ops":"format_storage",'
    payload += '"type":"btrfs_subvolume_snapshot",'
    payload += '"label":"raid1_000",'
    payload += '"mount_dir":%s,' % g_storage_mount_dir
    payload += '"subvolume":%s,' % g_storage_subvol_name
    payload += '}'
    return rst.http_post_ops_by_pyaload(hostname, payload)

