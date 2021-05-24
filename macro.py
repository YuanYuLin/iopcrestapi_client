import inspect
import sys
import imp
import libiopc_rest as rst
import pprint

def help_usage():
    rst.out("util.py <hostname> <module name> <function name>")
    sys.exit(1)

def module_usage(module):
    rst.out("utilpy <hostname> <module name> <function name> [function option]")
    rst.out("function list:")
    info_list = inspect.getmembers(module)
    for info in info_list:
        if (inspect.isfunction(info[1])) and (info[0].startswith("func_")) :
            rst.out("    %s ," % info[0])
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        help_usage()

    hostname=sys.argv[1]
    module_name=sys.argv[2]
    imp_fp, imp_pathname, imp_description = imp.find_module(module_name)
    module = imp.load_module("AA", imp_fp, imp_pathname, imp_description)
    if len(sys.argv) < 4:
        module_usage(module)

    function_name=sys.argv[3]

    options = None
    if len(sys.argv)  > 4:
        options = sys.argv[4:]

    status_code, json_objs = getattr(module, function_name)(hostname, options)

    if status_code == 200:
        pprint.pprint(json_objs)
    else:
        rst.out("sub request error: %s" % json_objs)
