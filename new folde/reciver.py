import socket
S = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #UDP - user data garam protocol
ip_adress= "192.168.63.29"
#ip_adress = "127.0.0.1"
port_no = 2525

complete_adress= (ip_adress,port_no) 

S.bind(complete_adress)

print("HEY I AM LISTING")
while True:

    message = S.recvfrom(100)
    print(message)
