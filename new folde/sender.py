import socket
S = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #UDP - user data garam protocol

target_ip = "192.168.1.64"
#target_ip= "127.0.0.1"
target_port=2525

while True:
   message = input("plz inter message")
   message = message.encode('ascii')
   S.sendto(message,(target_ip,target_port))
   print("your message has been sucessfully sent")