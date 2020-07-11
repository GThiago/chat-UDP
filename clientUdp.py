#127.0.0.1 -> local
#Porta -> 666
#Tipo ipv4

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  			

try:
	while True:
		client.sendto(raw_input("You: ") + "\n", ("127.0.0.1", 666))
		msg, friend = client.recvfrom(1024)
		print str(friend[0]) + ': ' + str(msg)

	client.close()
except Exception as E:
	print "Erro: " + E + "\nDisconnecting!"
	client.close()
