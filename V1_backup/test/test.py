#!/usr/bin/python2.7

import requests
import pprint
import sys
import json

HOSTNAME="192.168.1.116"
URLPOST="gpio"
URL="http://" + HOSTNAME +"/api/v1/" + URLPOST

def help_usage():
    print "rest_cli.py <method> <format> <url> <payload>"
    sys.exit(1)

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 4:
        help_usage()

    method=sys.argv[1]
    fmt_type=sys.argv[2]
    url=sys.argv[3]
    rsp = None

    if method == "get":
        rsp=requests.get(url)
    if method == "post":
        payload=sys.argv[4]
        rsp=requests.post(url, data=json.dumps(payload))
    if method == "put":
        payload=sys.argv[4]
        rsp=requests.put(url, data=json.dumps(payload))
    if method == "patch":
        payload=sys.argv[4]
        rsp=requests.patch(url, data=json.dumps(payload))
    if method == "delete":
        payload=sys.argv[4]
        rsp=requests.delete(url, data=json.dumps(payload))

    if rsp == None:
        print "method Not found [" + method + "]"
    else :
        print rsp.headers
        if rsp.status_code == requests.codes.ok :
            if fmt_type == "html":
                print rsp.text
            if fmt_type == "json":
                #pprint.pprint(rsp.json())
                print rsp.json()
        else :
            print "error" + rsp.status_code
    
