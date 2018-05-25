#!/usr/bin/env python

from classes import *
from config import config
import re
import sys
import urllib2
import urlparse

print(bcolors.HEADER)
config()
print(bcolors.ENDC)

url = str(raw_input(bcolors.BOLD + "YouTube URL> " + bcolors.ENDC))
if (re.search("youtube.com", url) is not None):
	try:
		urlparse.parse_qs(urlparse.urlparse(url).query)['v']
		yt_dl = yt_dl(url)
		fetch = yt_dl.fetch()

		if fetch['status'] == True:
			print(bcolors.OKBLUE + "Title: " + fetch['title'])
			print("Uploaded by: " + fetch['by'] + bcolors.ENDC + "\n")
			count = 1
			item = []
			for video in fetch['videos']:
				for key, value in video.iteritems():
					item.append(value)
					print("{}[{}]{} {}{} ({}){}".format(bcolors.BOLD, count, bcolors.ENDC, bcolors.OKGREEN, key, value['mime'], bcolors.ENDC))
					count += 1
			try:
				choose = int(raw_input(bcolors.BOLD + "Choose one> " + bcolors.ENDC))
			except ValueError:
				print(bcolors.FAIL + "[!] Error: Your selection is not available!" + bcolors.ENDC)
				sys.exit()
			try:
				item[int(choose-1)]
			except IndexError:
				print(bcolors.FAIL + "[!] Error: Your selection is not available!" + bcolors.ENDC)
				sys.exit()
			file_name = re.sub("[^a-zA-Z0-9\n\.]", "_", fetch['title'])
			file_name = file_name.replace("__", "_")
			new_name = str(raw_input(bcolors.BOLD + "File name (" + file_name + ")?> " + bcolors.ENDC))
			dl_name = file_name if new_name == "" else new_name
			try:
				download = urllib2.urlopen(item[int(choose-1)]['url'])
				yt_dl.download(download, dl_name + "." + item[int(choose-1)]['mime'].replace("video/", ""))
			except urllib2.HTTPError as err:
				print(bcolors.FAIL + "[!] Error: " + err.msg + "! Try another video." + bcolors.ENDC)
		else:
			print(bcolors.FAIL + "[!] Error: " + fetch['error'] + bcolors.ENDC)
	except KeyError:
		print(bcolors.FAIL + "[!] Error: Invalid YouTube URL!" + bcolors.ENDC)
else:
	print(bcolors.FAIL + "[!] Error: Invalid YouTube URL!" + bcolors.ENDC)
