"""Creates an example writer."""
import tempfile
from time import sleep
from os import path
from bayeosgatewayclient import BayEOSWriter

PATH = path.join(tempfile.gettempdir(),'bayeos-device1') 
writer = BayEOSWriter(PATH)

writer.save_msg('Writer was started.', origin='Python-Writer-Example')
 
while True:
    #writer.save_msg('Writer was started.', origin='Python-Writer-Example')
    print 'adding frame\n'
    writer.save(values=[1,2,3], value_type=0x41, origin='Python-Writer-Example',routed=True)
    writer.save(values=[2.1, 3, 20.5], value_type=0x02, offset=2)
    
    writer.save(values={"c1":1.2,"xx":1.7},value_type=0x61) 
    # Channel Offset, Integer values:
    #writer.save(values=[2.1, 3, 20.5], value_type=0x02, offset=2, origin='Python-Writer-Example')
     
    # Channel Indices:
    #writer.save(values=[[1,2.1], [2,3], [3,20.5]], value_type=0x41, origin='Python-Writer-Example')
    #writer.save(values={0: 0, 1: 1, 2: 2, 3: 3, 4: 4}, value_type=0x41, origin='Python-Writer-Example')
     
    # Error Message
    #writer.save_msg("error message", error=True, origin='Python-Writer-Example')
     
    # Error Message
    #writer.save_msg("error message", error=True, origin='Python-Writer-Example')
    sleep(1)