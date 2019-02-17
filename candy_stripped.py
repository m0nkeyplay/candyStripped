#!/usr/bin/python3
#
#  author:		https://github.com/m0nkeyplay
#               Use as you wish, this is cobbled together from bits of code I saw trying to work out root-me.org
#
#  Feb 16, 2019
#
#  purpose:     Shell of a script to talk to Candy
#               Candy is from root-me.org  She's a nice bot in the Programming section
#
#
#  Answers are not provided, but I didn't take out all the imports I needed to solve !ep1-4
#  REMOVED can be replaced with info to solve the puzzles - or the whole solve_puzzle function can be removed if you wish
#
#  You should
#       ! Fill in a NICKNAME below

from sys import argv
import math
import socket
import string
import time
import re
import base64
import codecs
import zlib
import binascii

if len(argv) == 1:
    print('We need something to tell Candy what puzzle to give us.')
    print('')
    print('Usage:  ./candy.py \'!ep#\'')
    print('We need the quotes around the puzzle because of the !')
    exit()
else:
    puzzle = argv[1]
    
argCheck = re.search('!ep[1-4]',puzzle)
if not argCheck:
    print('Okay, we are working with a limited set of arguments here.  Please pass argument as \'!ep[1-4]\'')
    exit()
          

SERVER = 'irc.root-me.org'
PORT = 6667
NICKNAME = ''
CHANNEL = '#root-m_challenge'
BOT = 'Candy'

IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def irc_conn():
    IRC.connect((SERVER, PORT))
    print("Connected to %s %s" % (SERVER, PORT))

def send_data(command):
    IRC.send(bytes(command + '\n', 'utf-8'))

def join(channel):
    send_data('JOIN %s' %channel)
    print('Joined %s' % channel)

def login(nickname, username='user', password = None, realname='WhyAsking', hostname='dsotm', servername='Server'):
    send_data('USER %s %s %s %s' %(username, hostname, servername, realname))
    send_data("NICK " + nickname)
    print("Logged in as %s" % NICKNAME)

def primsg(usr,msg):
    send_data('PRIVMSG %s %s' %(usr, msg))

def correct_response(msg):
	match = re.search(r'You dit it', msg)
	if match:
		print('Good work. Try another?')
		exit()

def bad_response(msg):
	match = re.search(r'Bad reponse', msg)
	if match:
		print('Candy didn\'t like that.  Check your puzzlefu!')
		exit()
        
def solve_puzzle(ep,txt):
    correct_response(txt)
    bad_response(txt)
    
    if(ep) == '!ep1':
        match = re.search(r'REMOVED',text)
        if match:
            #REMOVED
            print('Sending: '+str(answer)+ ' to Candy.')
            primsg(BOT, ep+' -rep '+str(answer)+'\n')
            
    if(ep) == '!ep2':
        myregex =  'REMOVED'
        match = re.search(myregex,text)
        if match:
            #REMOVED
            print('Sending: '+str(answer)+ ' to Candy.')
            primsg(BOT, ep+' -rep '+str(answer)+'\n')
   
    if(ep) == '!ep3':
        myregex = 'REMOVED'
        match = re.search(myregex,text)
        if match:
            #REMOVED
            print('Sending: '+str(answer)+ ' to Candy.')
            primsg(BOT, ep+' -rep '+str(answer)+'\n')
     
    if(ep == '!ep4'):
        myregex = 'REMOVED'
        match = re.search(myregex,text)
        if match:
            #REMOVED
            print('Sending: '+str(answer)+ ' to Candy.')
            primsg(BOT, ep+' -rep '+str(answer)+'\n')
       

#   Connect, login, join, and announce your question        
irc_conn()
login(NICKNAME)
join(CHANNEL)
time.sleep(2)
primsg(BOT,puzzle)

#   Solve the puzzle and get out of there
while (1):
    text=IRC.recv(2040)
    text= str(text)
    if "PRIVMSG "+NICKNAME in text:
        print(text)
        solve_puzzle(puzzle,text)
            
        
