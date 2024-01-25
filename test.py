

import time
import random
from StatusLine import StatusLine, Efficiency

def gif():
  sl = StatusLine(x_width=20, rangeEnd=131, eff= Efficiency.EFFICIENT)
  #Tutorial:  
  sl.run() #run will display the statusbar.
  sl.run() #run will display the statusbar.
  for _ in range(131): 
      sl.incrementCount() #will increment the status (count) 
      time.sleep(random.random()* 0.07) #simulates traffic
      print("hello")
  sl.reset()
 
def runCustomizable():
  sl = StatusLine(x_width=40, rangeEnd=70)
  sl.run() #run will display the statusbar.
  for _ in range(70): 
    sl.incrementCount() #will increment the status (count) 
    time.sleep(random.random()* 0.07) #simulates traffic
  
  sl = StatusLine(x_width=17, rangeEnd=70, end_char='\\', status_char='.')
  sl.run() #run will display the statusbar.
  for _ in range(70): 
    sl.incrementCount() #will increment the status (count) 
    time.sleep(random.random()* 0.07) #simulates traffic
 
  sl = StatusLine(x_width=29, rangeEnd=70, end_char='O', status_char='O')
  sl.run() #run will display the statusbar.
  for _ in range(70): 
    sl.incrementCount() #will increment the status (count) 
    time.sleep(random.random()* 0.07) #simulates traffic
 
 
  print('without percentage')
  sl = StatusLine(x_width=29, rangeEnd=70, end_char='O', status_char='O', printPercentage=False)
  sl.run() #run will display the statusbar.
  for _ in range(70): 
    sl.incrementCount() #will increment the status (count) 
    time.sleep(random.random()* 0.07) #simulates traffic
 
  
  
def demo(): 
  print ("Statusline full run: ")
  sl = StatusLine(x_width=20, rangeEnd=131, eff= Efficiency.EFFICIENT)
  #Tutorial:  
  sl.run() #run will display the statusbar.
  for _ in range(131): 
      sl.incrementCount() #will increment the status (count) 
      time.sleep(random.random()* 0.07) #simulates traffic
      
  #sl will kill itself after done. otherwise you can kill whenever you want
  #shown bellow:
  sl.reset()
  print ("Statusline killed run: ")
  sl.run()

  for _ in range(30): 
      sl.incrementCount() #will increment the status (count) 
      time.sleep(random.random()* 0.07) #simulates traffic
 
  sl.kill(); 
  print ("Alternative design full run: ")
  sl.status_char = '-'
  sl.spinWheel=False
 
  sl.reset();
  sl.run(); 
  for _ in range(131): 
      sl.incrementCount() #will increment the status (count) 
      time.sleep(random.random()* 0.07) #simulates traffic
 
  print("(demo) test run successful.")
 
 

if '__main__' == __name__:
  runCustomizable()
  #demo()
    
  """
  import random 
  sl.run()
  async def corof (f):
      #await asyncio.sleep(random.random()); 
      return f() 
  #cirif

  async def func ():
      await asyncio.sleep(random.random()); 
      return await asyncio.create_task(corof(sl.incrementCount)); 
  #sl = StatusLine(x_width=12, status_char='.', end_char='\\')
  #sl = StatusLine(x_width=12, rangeEnd=727 )
  #sl.testRun()
  loop = asyncio.get_event_loop()
  a1 = loop.create_task(func()); 
  for _ in range(131): 
      loop.run_until_complete(a1); 
  #sl.test()

  """
  