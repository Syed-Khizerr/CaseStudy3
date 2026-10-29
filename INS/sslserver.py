import socket
import ssl

context = ssl.create_default_context()

context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.create_connection(("localhost", 12345)) as sock:
	with context.wrap_socket(sock, server_hostname="localhost") as ssock:
		ssock.send(b"Hello from secure client")
		print("Server:", ssock.recv(1024).decode())