import socket
import json
import os

confile = open('config.json','r')
conf = confile.read()
confile.close()

def logg(it):
  try:
    fcontent = open(str('log.txt')+'.txt','r').read()
    f = open(str('log.txt')+'.txt','w+')
    f.write(fcontent+'\n'+it)
    f.close()
    pass
  except:
    os.system('echo "">log.txt')
    f = open('log.txt','w+')
    f.write(it)
    f.close()

jsconf = json.loads(conf)
HOST = jsconf["HOST"]
PORT = int(jsconf["PORT"])
NUMBER = int(jsconf["NUMBER"])
BUFFER= int(jsconf["BUFFER"])

server_info = (HOST, PORT)
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect(server_info)
try:
  print("Connection established successfully")
  logg('Client: Connection established successfully')
  while True:
    msg = str(input('client@botnet:~$ ').encode())
    logg('Client: Sending "{message}"'.format(message=msg))
    sock.send(msg.encode())
    data = sock.recv(BUFFER)
    data = data.decode()
    #print('received "{data}"'.format(data=data))
    print(data)
    sock.close()
    server_info = (HOST, PORT)
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect(server_info)
except Exception as e:
  print(e)
  pass

#finally:
#  print('closing socket')
#  sock.close()