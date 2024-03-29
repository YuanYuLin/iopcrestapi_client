import requests
import json
import pprint
import imp

def debug(msg):
    print(msg)
	
def out(msg):
    print(msg)

def loadModule(module_name, module_file, module_path):
    imp_fp, imp_pathname, imp_description = imp.find_module(module_file, module_path)
    module = imp.load_module(module_name, imp_fp, imp_pathname, imp_description)
    return module

def response_output(out_format, rsp):
    debug("response status code")
    debug(rsp.status_code)
    pprint.pprint(rsp)
    pprint.pprint(rsp.json())

def http_get_dao_by_key(hostname, key):
    url='http://' + hostname + '/api/v1/dao/?key=' + key
    debug(url)
    #http://192.168.1.115/api/v1/raw/2/1
    rsp=requests.get(url)
    return rsp.status_code, rsp.json()

def http_post_dao_by_key(hostname, key, payload):
    url='http://' + hostname + '/api/v1/dao/?key=' + key
    debug("POST Begin")
    debug(url)
    debug(payload)
    try :
        json.loads(payload)
    except ValueError as ex:
        debug("Invalid JSON: %s" % ex)
        return 500, '{"msg":"%s"}' % ex
    headers = {'content-type':'application/json; charset=utf-8', 'user-agent':'iopc-app'}
    rsp=requests.post(url, headers=headers, data=payload)
    debug("POST End")
    return rsp.status_code, rsp.json()

def http_post_ops_by_pyaload(hostname, payload):
    url='http://' + hostname + '/api/v1/ops'
    debug(url)
    headers = {'content-type':'application/json; charset=utf-8', 'user-agent':'iopc-app'}
    rsp=requests.post(url, headers=headers, data=payload)
    return rsp.status_code, rsp.json()

def http_post_rfb_by_payload(hostname, payload):
    url='http://' + hostname + '/api/v1/rfb'
    debug(url)
    headers = {'content-type':'application/json; charset=utf-8', 'user-agent':'iopc-app'}
    rsp=requests.post(url, headers=headers, data=payload)
    return rsp

def http_get_status(hostname, status_id):
    url='http://' + hostname + '/api/v1/status/?id=' + str(status_id)
    rsp=requests.get(url)
    return rsp

