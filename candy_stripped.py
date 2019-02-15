#!/usr/bin/python3

# shell of a script to talk to Candy for root-me.org Challenges.

# results have been removed

#  Fill in a nickname down there.... it's helpful.  I promise.

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

def login(nickname, username='user', password = None, realname='WhyAsking', hostname='MyHost', servername='MyServerDoesHaveAName'):
    send_data('USER %s %s %s %s' %(username, hostname, servername, realname))
    send_data("NICK " + nickname)
    print("Logged in")

def primsg(usr,msg):
    send_data('PRIVMSG %s %s' %(usr, msg))
    
def puzzle_ep1(txt):
    match = re.search(r':([\d.]+) / ([\d.]+)',text)
    #removed
        primsg(BOT, puzzle+' -rep '+str(last))

def puzzle_ep2(txt):
    #removed
      primsg(BOT, puzzle+' -rep '+str(bd))
    
def puzzle_ep3(txt):
    #removed
      primsg(BOT, puzzle+' -rep '+str(rt))

def puzzle_ep4(txt):
    #removed
      primsg(BOT, puzzle+' -rep '+str(answer)+'\n')
        
irc_conn()
login(NICKNAME)
join(CHANNEL)
time.sleep(3)
primsg(BOT,puzzle)

while (1):
    text=IRC.recv(2040)
    text= str(text)
    if "PRIVMSG "+NICKNAME in text:
        print(text)
        if puzzle == '!ep1':
            puzzle_ep1(text)
        elif puzzle == '!ep2':
            puzzle_ep2(text)
        elif puzzle == '!ep3':
            puzzle_ep3(text)
        elif puzzle == '!ep4':
            puzzle_ep4(text)
            
        
