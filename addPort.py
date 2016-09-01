"""This python3 script is for linux, which is usually abest choice for building ss servers.

When run this script with python3, a new port will automatically be added to the json config file
and few lines of message about the new port will be print on the shell,Including 
the basic unique information and a QR code for Android and PC apps to scan.

"""

import json
import os
from passGenerator import generatepd
try:
    f = open("/etc/shadowsocks.json", 'r')
    f.seek(0)
    d = json.load(f)
    f.close()
    server = d["server"]
    method = d["method"]
    pp_dict = d["port_password"]
    port = str(int(max(pp_dict.keys()))+1)
    f = open("shadowsocks.json", 'w')
    passwd = generatepd()
    d["port_password"][port] = passwd
    json.dump(d, f, sort_keys=True, indent=4)

    #print the information about the new port.
    print("Success to add a new port for shadowsocks!")
    print("server: {} \nport: {}\nmethod: {}\npasswod: {}\n".format(server, port, method, passwd))
    ls = sorted(list(d["port_password"].keys()))
    print("Now we have used these {} ports: {}".format(len(ls), ls))

    #restart the service and print the QR code.
    if os.name == "posix":
        os.system(r"ssserver -c /etc/shadowsocks.json -d restart")
        os.system(r'echo -n "ss://"`echo -n {}:{}@{}:{} | base64` | qr'.format(method, passwd, server, port))
except Exception as e:
    print(e)
finally:
    f.close()