from sys import path
path.append('C:\\Users\\Owen\\Documents\\q-bot\\qbot modules')
import socket

server = 'irc.synirc.net'
channel = '#testingscript'
nick = 'Q-bot'
port = 6667

ircsocket = socket.socket()
ircsocket.connect((server, port))

handle = ircsocket.makefile(mode='rw', buffering=1, encoding='utf-8',
                            newline='\r\n')

print('NICK', nick, file = handle)
print('USER', nick, nick, nick, ':'+nick, file = handle)

for line in handle:
    line = line.strip()
    print(line)

    if "PING" in line:
        print("PONG :" + line.split(':')[1], file=handle)

    if 'MODE' in line:
        print('JOIN', channel, file = handle)

    if 'KICK' in line:
        print('JOIN', channel, file = handle)

    if 'Q!generic@botserv.synirc.net PRIVMSG #cycloneblaze' in line:
        print('PRIVMSG ', channel, ' :', 'q is my overlord and progammer',
              file = handle, sep = '')
        print('PRIVMSG ', channel, ' :', 'hello master',
              file = handle, sep = '')

    if 'Galaxy!~Galaxy@center.of.universe PRIVMSG #testingscript' in line:
        print('PRIVMSG ', channel, ' :', 'hello space object',
              file = handle, sep = '')
