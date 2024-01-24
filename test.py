

import time
import random
from StatusLine import StatusLine, Efficiency
if '__main__' == __name__:
    
  sl = StatusLine(x_width=170, rangeEnd=131, eff= Efficiency.EFFICIENT)
  #Tutorial:  
  sl.run() #run will display the statusbar.
  for _ in range(131): 
      sl.incrementCount() #will increment the status (count) 
      time.sleep(random.random()* 0.07) #simulates traffic

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
  