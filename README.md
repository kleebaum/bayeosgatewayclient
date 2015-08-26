# bayeosgatewayclient
A generic Python module to transfer client (sensor) data to a BayEOS Gateway.

## Installation
You can use either the setup.py script, pip or a Linux binary to install the package.

### Setup.py
Do the following steps to install the package via the setup.py script:
- git clone request ```git clone git://github.com/kleebaum/bayeos.git```
- find the right directory ```cd bayeos/bayeosgatewayclient```
- run ```python setup.py install``` as root

### PIP

### Linux Binary
#### Debian
- add the following repositories to /etc/apt/sources.list ```deb http://www.bayceer.uni-bayreuth.de/repos/apt/debian wheezy main```
- install key ```wget -O - http://www.bayceer.uni-bayreuth.de/repos/apt/conf/bayceer_repo.gpg.key | apt-key add -```
- ```apt-get update```
- ```apt-get install python-bayeosgatewayclient```

Alternatively:
- run ```dpkg -i python-bayeosgatewayclient_0.1-1_all.deb``` as root

## Example usage
- import the module ```import bayeosgatewayclient```

### Example writer
Run the method ```bayeosgatewayclient.samplewriter()``` for a demo. 

This is how to see how the BayEOSWriter class is instantiated.
```
from time import sleep
from bayeosgatewayclient import BayEOSWriter

PATH = '/tmp/bayeos-device1/'
writer = BayEOSWriter(PATH, 100)

while True:
    print 'adding frame\n'
    writer.save(values=[2.1, 3, 20.5], valueType=0x02, offset=2)
    writer.saveMessage("This is a message.")
    writer.saveErrorMessage("This is an error message.")
    sleep(1)
```

### Example sender
Run the method ```bayeosgatewayclient.samplesender()``` for a demo.

This is how how the BayEOSSender class is instantiated:
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
Run the method ```bayeosgatewayclient.sampleclient()``` for a demo.
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
