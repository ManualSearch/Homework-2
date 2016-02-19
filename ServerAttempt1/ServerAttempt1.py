'''
Patrick Gephart
CS 374
Code taken from http://ruslanspivak.com/lsbaws-part1/ and modified
for classroom purposes only.
'''

# Imports the Socket library, to allow a socket to be opened or closed. 
import socket

# Sets a default HOST and PORT variable so we can create the correct socket.
HOST, PORT = '', 12000

# Creates a socket called 'listen_socket' for the server to listen to.
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binds listen_socket to the default HOST and PORT (localhost port 12000)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

# Prints a message allowing user to see that a port is being listened to.
print ('Serving HTTP on port %s ...' % PORT)

# When the server sees a connection, it accepts and sends the request.
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print (request)

    # Server responds by sending live HTML data that a browser can read.
    http_response = """\
HTTP/1.1 200 OK

<h1>Hello CS374!</h1>
"""
    # 'client_connection' is sent the HTML code 'http_response', encoded for network travel.
    client_connection.sendall(http_response.encode())
    
    # Closes the 'client_connection' port.
    client_connection.close()