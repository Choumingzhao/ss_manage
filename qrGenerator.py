"""Generate a qrcode from given informaton and save it as a PNG image file.

"""

import qrcode
import base64

server = ""
method = ""
password = ""
port = ""
config = method + ':' + password + '@' + server + ':' + port
s = base64.encodebytes(config.encode())
ss = "ss://" + s.decode()
arr = qrcode.make(ss)
arr.save("{}_{}.png".format(server, port))