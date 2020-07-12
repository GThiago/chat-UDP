import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 777

#0.0.0.0 ouve todos que se conectarem em qualquer porta
try:
	server.bind((ip, port)) #onde -> abre
	server.listen(5) 			#numero q pode escutar
	print "Listning in: " + ip + ':'+ str(port)

	(client_socket, address) = server.accept()

	print "Received from: " + address[0]

	while True:
		data = client_socket.recv(1024)
		if 'codigo' in data:
			client_socket.send('Secreta\n')
		else:
			client_socket.send("Incorreto\n")

	server.close()
except Exception as E:
	print "Erro: " + str(E)

	server.close()
