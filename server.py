import socket
import os
import json

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

conf = open('config.json','r').read()
jsconf = json.loads(conf)
HOST = jsconf["HOST"]
PORT = int(jsconf["PORT"])
NUMBER = int(jsconf["NUMBER"])
BUFFER_SIZE = int(jsconf["BUFFER"])
server_info = (HOST, PORT)
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.bind(server_info)
sock.listen(NUMBER)
try:
  logg('Server: Successfully Started')
  while True:
    connection, client_address = sock.accept()
    data = connection.recv(BUFFER_SIZE)
    data = (data.decode('utf-8')).replace('b','').replace("'",'')
    logg('Server: Got '+data)
    execo = os.popen(data).read()
    logg('Execo: '+execo)
    if execo != '':
      #print('message received: {data}'.format(data=data))
      connection.send(execo.encode())
    else:
      connection.send('Error occured'.encode())
finally:
  connection.close()