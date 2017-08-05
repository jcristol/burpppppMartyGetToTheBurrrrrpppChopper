import gevent, urllib2, os, errno
from gevent import monkey

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()
