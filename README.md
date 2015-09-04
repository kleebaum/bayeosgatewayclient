# bayeosgatewayclient
A Python package to transfer client (sensor) data to a BayEOS Gateway.

## Installation
You can either use the setup.py script, the Python Package Index (PIP) or a Linux binary to install the package.

### Setup.py
Do the following steps to install the package via the setup.py script:
- git clone request ```git clone git://github.com/kleebaum/bayeosgatewayclient.git```
- find the right directory ```cd bayeosgatewayclient```
- run ```python setup.py install``` as root

### PIP
- run ```pip2.7 install bayeosgatewayclient```

### Linux Binary (for Debian)
- add the following repositories to /etc/apt/sources.list ```deb http://www.bayceer.uni-bayreuth.de/repos/apt/debian wheezy main```
- install key ```wget -O - http://www.bayceer.uni-bayreuth.de/repos/apt/conf/bayceer_repo.gpg.key | apt-key add -```
- ```apt-get update```
- ```apt-get install python-bayeosgatewayclient```

Alternatively:
- run ```dpkg -i python-bayeosgatewayclient_0.1-1_all.deb``` as root

## Example usage
- import the module ```import bayeosgatewayclient```

### Example writer
A simple writer looks like this:
```
from time import sleep
from bayeosgatewayclient import BayEOSWriter

writer = BayEOSWriter('/tmp/bayeos-device1/')
writer.saveMessage('BayEOS Writer was started.')

while True:
    print 'adding frame\n'
    writer.save([2.1, 3, 20.5])
    sleep(1)
```

A BayEOSWriter constructor could also take the following arguments:
```
PATH = '/tmp/bayeos-device1/'	# path to store .act and .rd files
MAX_CHUNK = 2000				# file size in bytes
MAX_TIME = 60					# time when a new file is started in seconds
writer = BayEOSWriter(path=PATH, max_chunk=MAX_CHUNK, max_time=MAX_TIME)
```

The following methods could also be of interest:
- save integer values: ```writer.save(values=[1,2,3], value_type=0x22)```
- save with channel indices: ```writer.save([[1,2.1], [2,3], [3,20.5]], value_type=0x41)``` or
  ```writer.save({1: 2.1, 2: 3, 3: 20.5}, value_type=0x41)
- save with channel offset: ```writer.save([2.1, 3, 20.5], value_type=0x02, offset=2)```
- save origin: ```writer.save([2.1, 3, 20.5], origin='Writer-Example')```
- save error message: ```writer.save_msg('error message', error=True)

### Example sender

This is how the BayEOSSender class is instantiated:
```
from time import sleep
from bayeosgatewayclient import BayEOSSender

PATH = '/tmp/bayeos-device1/'
NAME = 'Python-Test-Device'
URL = 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat'
sender = BayEOSSender(PATH, NAME, URL, 'bayeos', 'root')

while True:
    res = sender.send()
    if res > 0:
        print 'Successfully sent ' + str(res) + ' post requests.\n'
    sleep(5)
```

### Example client
```
from bayeosgatewayclient import BayEOSGatewayClient
from random import randint

OPTIONS = {'bayeosgateway_url' : 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat',
           'bayeosgateway_user' : 'root',
           'bayeosgateway_pw' : 'bayeos',
           'sender' : 'anja'}

NAMES = ['PythonTestDevice1', 'PythonTestDevice2', 'PythonTestDevice3']

class PythonTestDevice(BayEOSGatewayClient):
    """Creates both a writer and sender instance for every NAME. Implements BayEOSGatewayClient."""
    def readData(self):
        if self.names[self.i] == 'PythonTestDevice1':
            return (randint(-1, 1), 3, 4)
        else:
            return (2, 1.0, randint(-1, 1))
print OPTIONS

client = PythonTestDevice(NAMES, OPTIONS)

client.run()
```
