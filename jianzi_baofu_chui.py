# jianzi--0
# baofu --2
# chui  --1

import random

def name2num(name):
	if name == "jianzi":
		return 0
	elif name == "baofu":
		return 2
	elif name == "chui":
		return 1
	else:
		print "wrong name"
		exit(3)

def num2name(num):
	if num == 0:
		return "jianzi"
	elif num == 2:
		return "baofu"
	elif num == 1:
		return "chui"
	else:
		print "wrong number"
		exit(3)

def compare(user, computer):
	if user == 0 and computer == 1:
		print "computer win"
		print str("user:")+num2name(user)
		print str("computer:")+num2name(computer)
	elif user == 0 and computer ==2:
		print "user win"
		print str("user:")+num2name(user)
		print str("computer:")+num2name(computer)
	elif user == 1 and computer ==0:
		print "user win"
		print str("user:")+num2name(user)
		print str("computer:")+num2name(computer)
	elif user == 1 and computer ==2:
		print "computer win"
		print str("user:")+num2name(user)
		print str("computer:")+num2name(computer)
	elif user == 2 and computer ==0:
		print "computer win"
		print str("user:")+num2name(user)
		print str("computer:")+num2name(computer)
	elif user == 2 and computer ==1:
		print "user win"
		print str("user:")+num2name(user),
		print str("computer:")+num2name(computer)

def main():
	user = random.randint(0, 2)
	computer = random.randint(0, 2)
	if user != computer:
		compare(user, computer)

main()
