# SSL Client
import socket
mport ssl

context = ss1. SSLContext (ssl.PROTOCOL_TLS_SERVER)

server = socket.socket()

context.load_cert_chain("server.crt", "server.key")

server.bind (("localhost", 12345))

server.listen(1)

with context.wrap_socket(server, server_side=True) as ssock:

  conn, addr = ssock.accept()

  print ("Secure connection established")

  data = conn.recv(1024).decode()

  print("Client:", data)

  conn.send (b"Hello from secure server") 
  conn.close()
