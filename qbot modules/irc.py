##  Note: This is a module, not a script.
##  From https://pythonspot.com/en/building-an-irc-bot/

import socket
import sys

class IRC:

    irc = socket.socket()

    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send(b"PRIVMSG " + chan + b" " + msg + b"n")

    def connect(self, server, channel, botnick):
        #defines the socket
        print("irc.py is connecting to: " + server)
        self.irc.connect((server, 6667))
        #connects to the server
        self.irc.send(b"USER " + botnick + b" " + botnick + b" " + botnick + b" :This is a fun bot!n")
        #user authentication
        self.irc.send(b"NICK " + botnick + b"n")          
        self.irc.send(b"JOIN " + channel + b"n")
        #join the chan

    def get_text(self):
        text = self.irc.recv(2040)  #receive the text

        if text.find(b'PING') != -1:                      
            self.irc.send(b'PONG ' + text.split() [1] + b'rn') 

        return text
