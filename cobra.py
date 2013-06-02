#!/usr/bin/python3
#encoding: utf-8

import argparse
from sys import argv, exit
from shutil import copyfile
from datetime import date

import cobra

def main(argv):
	"""
	Parse our arguments
	"""

	parser = argparse.ArgumentParser(description="CobraPress Version 0.0.2")
	parser.add_argument("--generate", help="Generate the static html", action="store_true")
	parser.add_argument("--init", help="Initialize this installation", action="store_true")
	parser.add_argument("--new_post", help="Generate a new post", action="store_true")
	parser.add_argument("--list", help="List available arguments", action="store_true")
	args = parser.parse_args()

	if args.generate:
		generate()
	elif args.init:
		initialize()
	elif args.new_post:
		new_post(args.new_post)
	elif args.list:
		listargs()
	else:
		parser.print_help()
	
	return

def generate():
	"""
	Generate the static html
	"""

	config = readconfig()

	print(config)
	from cobra import generate
	generate.generate(config).generate_html()
	print("Done!")
	return

def initialize():
	"""
	Initialize this installtion
	"""

	copyfile("_config.py", "config.py")
	# Prepend some stuff to a new config
	f = open("_config.py", 'r')
	config = f.read()
	f.close()

	f = open("config.py", 'w')
	f.write("# Use this file to override configurations made in _config.py\n\n")
	f.write(config)
	f.close()
	print("Done!")
	return

def new_post(title):
	"""
	Generate a new post
	"""

	if title == True:
		print("What's the title?")
		title = input("Title: ")

	filename = str(date.today().year)+"-"+str(date.today().month)+"-"+str(date.today().day)+"-"+title
	post = open("posts/"+filename, 'a')
	post.write(title)
	post.close

	print(title)
	print("Done!")
	return

def listargs():
	"""
	List available arguments
	"""

	print("generate")
	print("init")
	print("new_post")
	print("list")
	print("help")
	return

def readconfig():
	"""
	Read the config
	"""

	configuration = {}

	import _config
	try:
		import config
	except ImportError:
		print("No config file found!\nDid you \"make init\"?")
		exit(5)

	# Check, whether there's a custom entry
	for argument in _config.config:
		if config.config[argument] or config.config[argument] == []:
			configuration[argument] = config.config[argument]
		else:
			configuration[argument] = _config.config[argument]

	return configuration

if __name__ == "__main__":
	main(argv[1:])
