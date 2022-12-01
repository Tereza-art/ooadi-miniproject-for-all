import socket

from classes.CreateUserApp import CreateUserApp
from classes.UserLog import UserLog
from classes.ClientConnectionManager import ClientConnectionManager
from classes.ServerConnectionManager import ServerConnectionManager





if __name__=="__main__":  
   ServerConnectionManager()




















'''
Log_book = CredentialLog()
Log_book.add_user('Miro', '123')
print(Log_book)
Purchased_Tickets = {}
bit_message = ''
HOST = '127.0.0.1'
PORT = 5000                 # An integer from 1 to 65535


User_Log = UserLog()
user_app = CreateUserApp()

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # AF_INET is the Internet address family for IPv4
        s.bind((HOST, PORT))
        s.listen()
        print("Server is waiting for a client ...")                                                  
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)                  # 1024 is the maximum amount of bytes to be received at once
                print("Server is receving data ...")
                if not data:
                    break
                message = data.decode('utf-8').split(',')
                if message[0] == 'Log_Book_Login':
                    if  message[2]==Log_book.check_user(username=message[1]):
                        conn.sendall(b'True')
                        break
                    else:
                        conn.sendall(b'False')
                        break
                elif message[0] == 'Log_Book_Register':
                    # do register stuff
                    print(f'{message[1]}, {message[2]}, {message[3]}, {message[4]}, {message[5]}')
                    User_Log.add_user_info(message[1], message[2], message[3], message[4], message[5])
                    Log_book.add_user(message[2], message[3])
                    conn.sendall(b'True')
                    
                    break

                elif message[0] == 'Buy_Ticket':
                    # do buy ticket stuff


                    pass
                else:
                    print('How did you end up here?! Did you divide by 0?')
                print('index 0', message[0], '1', message[1], '2', message[2])
                # No s.close is needed
'''