from sys import path
path.append('C:\\Users\\Owen\\Documents\\q-bot\\qbot modules')
import socket

server = 'irc.synirc.net'
channel = '#cycloneblaze'
nick = 'Cycloneblaze'
port = 6667

ircsocket = socket.socket()
ircsocket.connect((server, port))

handle = ircsocket.makefile(mode='rw', buffering=1, encoding='utf-8', newline='\r\n')

print('NICK', nick, file = handle)
print('USER', nick, nick, nick, ':'+nick, file = handle)

for line in handle:
    line = line.strip()
    try:
        print(line)
    except UnicodeEncodeError:
        print('DEBUG: unicode encoding error encountered, not printing line')
        pass

    if "PING" in line:
        print("PONG :" + line.split(':')[1], file=handle)

    if 'MODE' in line:
        print('PRIVMSG NickServ IDENTIFY kbYBxzfD4D', file = handle, sep = '')
        # this password was randomly generated, is not shared (_obviously_)
        # and has long since deregistered; don't bother

    if ':services.synirc.net MODE Cycloneblaze :+r' in line:
        print('JOIN', channel, file = handle)

    if 'KICK ' in line:
        print('JOIN', channel, file = handle)

    if 'Wingcap!~Wingcap@rune.scape PRIVMSG #cycloneblaze :Cycloneblaze' in line:
        print('PRIVMSG ', channel, ' :', 'I am a robot bzzt', file = handle, sep = '')

##    if 'Q!generic@botserv.synirc.net PRIVMSG #cycloneblaze' in line:
##        print('PRIVMSG ', channel, ' :', 'q is my overlord and progammer', file = handle, sep = '')
##        print('PRIVMSG ', channel, ' :', 'hello master', file = handle, sep = '')

##    if 'Galaxy!~Galaxy@center.of.universe PRIVMSG #testingscript' in line:
##        print('PRIVMSG ', channel, ' :', 'hello space object', file = handle, sep = '')
