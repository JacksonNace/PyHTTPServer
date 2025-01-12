# socket is bridge between client and server

# client sends a request, server sends back a response

import socket
#import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket( #establishes connection through 4 module things. Family, type, proto, fileno
  socket.AF_INET,#sends my ip address through IPv4. IPv4 supports much less ip addresses through 32 bit, IPv6 supports 43 bajillion decillion
  socket.SOCK_STREAM #TCP type - helps connection by making sure its error free through SYN->SYN|ACK->ACK handshake thing. Someone knocks on your door-SYN, you open the door SYN-ACK, they say Hi! -ACK
  # can also use SOCK_DGRAM which is a UDP connection. sends packets in random order without checking if its fully connected. TCP is more reliable and UDP yeets it. livestreaming, videogames, broadcast, etc
  ) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #integer shows its on, reuse address as soon as socket closes instead of waiting for default timer.
# port 80 is HTTP, 443 is HTTPS
# by now i have created and initlized a socket
server_socket.bind((SERVER_HOST, SERVER_PORT)) #host, port. establishes a socket we can connect to through opening a port on our host ip addy i believe. ports 0-1023 are reserved by operating system
server_socket.listen(5) #backlog is maximum amount of connections that can be queued, the rest will be ignored (depends on OS)

print(f"Listening on port 8080 {SERVER_PORT} ...") #fstring allows for variables

while True: 
  print("ran")
  client_socket, client_address = server_socket.accept() # this will listen and recieve data. .accept blocks code until it recieves a response
  print("ran2")
  request = client_socket.recv(1500).decode() #decode makes the bytes recieved into a string
  print(request)

  headers = request.split('\n') 
  first_header_components = headers[0].split()

  http_method = first_header_components[0] # gets whatever http method is requested
  path = first_header_components[1] # takes out the path "/", "/book"

  if http_method == 'GET':
    if path == '/':
      fin = open('index.html')
    elif path == '/book':
      fin = open('book.json')
    else:
      # handle random edge cases
      pass
        
    content = fin.read() #file handling, reads all contents of file opened
    fin.close() #after this it closes the file
    response = 'HTTP/1.1 200 OK\n\n' + content
  else:
    response = 'HTTP/1.1 405 Method Not Allowed\n\nAllow: GET'

  client_socket.sendall(response.encode()) # now sends the response to a client after putting it back into bytes
  client_socket.close()

server_socket.close()

