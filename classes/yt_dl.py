#!/usr/bin/env python

import urllib2
import json
from bcolors import bcolors
from config import config as conf

class yt_dl(object):
	def __init__(self, url):
		super(yt_dl, self).__init__()
		self.url = url

	def fetch(self):
		fetch = urllib2.urlopen(conf.API + conf.ENDPOINT + "?url=" + self.url)
		response = json.load(fetch)
		return response

	def download(self, get, name):
		file = open(name, 'wb')
		meta = get.info()
		size = int(meta.getheaders("Content-Length")[0])
		print "%s[+] Downloading: %s Bytes: %s%s" % (bcolors.OKGREEN, name, size, bcolors.ENDC)
		size_dl = 0
		block_sz = 8192

		while True:
			buffer = get.read(block_sz)
			if not buffer: break
			size_dl += len(buffer)
			file.write(buffer)
			status = r"%10d [%3.2f%%]" % (size_dl, size_dl * 100. / size)
			status = status + chr(8)*(len(status)+1)
			print status,
		file.close()