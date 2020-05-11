#!/usr/bin/python2.7

import requests
import pprint
import sys
import json

def http_request(url_prefix):
    url=url_prefix + '/v1/raw/2/1'
    payload='{"ops":"up_netifc", "ifc":"br0", "ip_src":"dhcp"}'
    print url
    #http://192.168.1.115/api/v1/raw/2/1
    rsp=requests.post(url, data=payload)
    return rsp

def help_usage():
    print "rest_cli.py <hostname>"
    sys.exit(1)

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 2:
        help_usage()

    hostname=sys.argv[1]

    url="http://" + hostname + "/api"
    rsp=http_request(url)

    if rsp.status_code == requests.codes.ok :
        pprint.pprint(rsp.json())
    else :
        print "error" + str(rsp.status_code)
    
