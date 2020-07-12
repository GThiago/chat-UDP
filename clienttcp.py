import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #tipo ipv4

client.settimeout(5)

site = input()

try:
	client.connect((site, 80))

	client.send("GET / HTTP/1.1\nHost: google.com\n\n\n")

	recebido = client.recv(1024)

	print recebido

except:
	print "Conexao falhou"