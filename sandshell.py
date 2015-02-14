#sandshell v1.0

import subprocess

#idleorcommandline is from the project https://github.com/ilovecode1/PylaunchAPI

def idleorcommandline():
   'If idleorcommandline returns True its IDLE if False its command line!'
   a = sys.executable
   m = '\\\\'
   m = m[0]
   while True:
       b = len(a)
       c = a[(b - 1)]
       if c == m:
           break
       a = a[:(b - 1)]
   if sys.executable == a + 'pythonw.exe':
       return True
   else:
       return False

class sandshell:

  def runsingle(command):
    
    ioc = idleorcommandline()
    
    if ioc == False:
      subprocess.call(command, shell=True)
      
    else:
      
      print(null)
    
  def runmultiple(commands):
   
    if ioc == False: 
    
      e = 0
      
      for i in e:
        
        subprocess.call(commands[e], shell=True)
        e += 1
        
    else:
    
      print(null)
