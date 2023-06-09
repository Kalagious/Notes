#!/usr/bin/env python3

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--type', type=str, required=False)

args = parser.parse_args()



if args.type:
	path = "/home/"+os.getlogin()+"/Notes/Boxes/"
	reportTemplatePath = "/home/"+os.getlogin()+"/Notes/Obsidian-Notes/Boxes/Report-Template.md"
	obsidianPath = "/home/"+os.getlogin()+"/Notes/Obsidian-Notes/"

	path += args.type+"/"+args.name+"/"


	# os.mkdir(path)
	# os.mkdir(path+"www")
	# os.mkdir(path+"files")
	# os.mkdir(path+"enum")
	# os.mkdir(path+"exploits")
	# os.system("touch "+path+"users")
	# os.system("touch "+path+"hashes")
	# os.system("touch "+path+"passwords")
	print(" \033[;1m[\033[36m*\033[36m]\033[;0m A folder for the box has been created.")
	os.system("cp "+reportTemplatePath+" "+obsidianPath+"Boxes/"+args.type+"/"+args.name+"-Report.md")
	print(" \033[;1m[\033[36m*\033[36m]\033[;0m A base report has been created at %s", obsidianPath+"Boxes/"+args.type+"/"+args.name+"-Report.md")
	os.system("ln "+obsidianPath+"Boxes/"+args.type+"/"+args.name+"-Report.md "+path+args.name+"-Report.md ")