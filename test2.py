
import os

source = '/mnt/FORALL/PYTHON/'

#path = source.split('/')

path = os.path.abspath(os.path.join(source, os.pardir))
#path = os.path.join(path[:-1])
print(path)
print(os.pardir)