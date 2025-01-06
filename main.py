# socket is bridge between client and server

# client sends a request, server sends back a response

import socket

server_socket = socket.socket( #establishes connection through 4 module things. Family, type, proto, fileno
  socket.AF_INET,#sends my ip address through IPv4. IPv4 supports much less ip addresses through 32 bit, IPv6 supports 43 bajillion decillion
  socket.SOCK_STREAM #TCP type - helps connection by making sure its error free through SYN->SYN|ACK->ACK handshake thing. Someone knocks on your door-SYN, you open the door SYN-ACK, they say Hi! -ACK
  # can also use SOCK_DGRAM which is a UDP connection. sends packets in random order without checking if its fully connected. TCP is more reliable and UDP yeets it. livestreaming, videogames, broadcast, etc
  ) 

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #integer shows its on, reuse address as soon as socket closes instead of waiting for default timer.
# port 80 is HTTP, 443 is HTTPS
server_socket.bind(("0.0.0.0", 8080)) #host, port. establishes a socket we can connect to through opening a port on our host ip addy i believe. ports 0-1023 are reserved by operating system