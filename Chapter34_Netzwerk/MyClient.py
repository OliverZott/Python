import socket


# socket instance; parameter: address-type, network-protocol
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# input data and address
ip = input("IP-Address: ")  # if left empty --> localhost (127.0.0.1)
message = input("Message: ")

# send
s.sendto(message.encode(), (ip, 50000))

# close communication-socket
s.close()
