# POS - Python Operating System #
#IMPORTS#
import turtle
from Tkinter import *
import random
import os
import time
import webbrowser
import datetime
import urllib

#VARIABLES#
version = 1.5
#FUNCTIONS#
def start_up():
	print "0000   000   0000"
	print "0   0 0  00 0    "
	print "0000  0 0 0  000 "
	print "0     00  0     0"
	print "0      000  0000 "
	print "      -----      "
	print "Developed By Takatino"
	time.sleep(2)
	menu()

def menu():
	print "\n\nPOS - Python Operating System"
	print "------------Menu-------------"
	command = raw_input("Command: ")
	command.lower()
	###COMMANDS###

	if command in ("clear", "cls"):
		clear()
	elif command in ("print", "say", "display"):
		text = raw_input("Display: ")
		print "\n\n", text
		menu()
	elif command in ("web", "webbrowser", "internet"):
		website = raw_input("Enter Url: ")
		if website in ("Youtube", "youtube"):
			webbrowser.open("http://youtube.com")
			menu()
		elif website == "google":
			webbrowser.open("http://google.com")
			menu()
		elif website in ("grms", "GRMS", "schoolloop"):
			webbrowser.open("http://grms.schoolloop.com")
			menu()
		elif website in ("google docs", "docs"):
			webbrowser.open("http://docs.google.com")
			menu()
		else:
			webbrowser.open(website)
			menu()
	elif command in ("html", "fetch"):
		try:
			url = raw_input("Enter Url: ")
			f = urllib.urlopen(url)
			html = f.read()
			print html
			menu()
		except IOError:
			print "No such file or directory."
			menu()
	elif command in ("download"):
		try:
			website = raw_input("Enter Url: ")
			download_name = raw_input("Save Name: ")
			urllib.urlretrieve(website, download_name)
			print download_name, " has been downloaded from: ", website
			menu()
		except IOError:
			print "Error: No such file or directory."
			menu()
	elif command in ("timer", "counter"):
		try:
			count = float(raw_input("Enter Counter Time (Sec): "))
			while count > 0:
				print count
				time.sleep(1)
				count = count - 1
				if count == 0:
					print "Counter Has Ended."
					menu()
			if count <= 0:
				print "Time Is Less Than 0 Seconds."
				menu()
			else:
				print "Unknown Error, Please Report as a Bug."
				menu()
		except ValueError:
			print "Error: Not A Integer."
			menu()
		except SyntaxError:
			print "Error: Invalid Syntax."
			menu()
	elif command in ("exit", "quit"):
		exit()
	elif command in ("calculator", "calculate"):
		try:
			print "Enter Equation:"
			calc = input()
			print "Answer is ", calc
			menu()
		except NameError:
			print "Error: Unsolvable Process."
			menu()
		except SyntaxError:
			print "Error: Invalid Syntax."
			menu()
	elif command == "help":
		help()
	elif command in ("date", "time"):
		now = datetime.datetime.now()
		print "Date: ", now.month, "/", now.day, "/", now.year
		print "Time: ", now.hour, ":", now.minute
		menu()
	elif command in ("info", "information"):
		info()
	elif command in ("webflood", "flood", "error 404", "error404"):
		error_404()
	else:
		print "Error: No command called ", command
		menu()

def help():
	print "\nList Of Commands:"
	print "--------------------------------+"
	print "help - Opens the Help Menu"
	print "calculate or calculator - Opens Calculator"
	print "time or date - Opens Clock"
	print "counter or timer - Starts a Counter"
	print "web or webbrowser or internet - Opens a internet website"
	print "display or say or print - Prints text"
	print "flood or error404 - Floods a specified url, a specified number of times"
	print "fetch or html - Finds the source code for specified website"
	print "download - Downloads file from specified website"
	print "exit or quit - Exits POS"
	option = raw_input("Press Any Key To Exit Help Menu: ")
	if option == "a":
		menu()
	else:
		menu()
def info():
	print "\n\nPOS"
	print "Python Operating System"
	print "Version - ", version
	print "-"*10
	print "Developed By Takatino"
	print "\nSystem Requirements: "
	print "- Mac OS X Snow Leopard/Lion/Mountain Lion"
	print "- Ubuntu 12.04 LTS/ Fedora 17/ CentOS 5"
	print "- Python 2.6.X - 2.7.X"
	menu()
def clear():
	os.system("cls")
	os.system("clear")
	menu()
def error_404():
	try:
		website = raw_input("Enter Url To Flood: ")
		flood_time = raw_input("Select Flood Times: ")
		flood_count = 0
		while flood_time > 0:
			webbrowser.open(website)
			flood_count = flood_count + 1
			print "Flooded ", flood_count, " times."
			flood_time = flood_time - 1
			if flood_time <= 0:
				print "Flood has Ended."
				menu()
		if flood_time <= 0:
			print "Flood_Time Is Less Than 0"
			menu()
	except ValueError:
		print "Error: Not A Integer."
#MAIN CODE#
start_up()


