from ipaddress import ip_address
import socket

def return_ip_address():
    h_name = socket.gethostname()
    IP_address = socket.gethostbyname(h_name)
    return IP_address


print(return_ip_address())

