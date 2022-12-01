import socket
import pickle

from classes.CreateUserApp import CreateUserApp
from classes.UserLog import UserLog
from classes.GridLoginApp import GridLoginApp

class ServerConnectionManager:
    def __init__(self):
        HOST = '127.0.0.1'
        PORT = 5000                 # An integer from 1 to 65535

        user_info = UserLog()
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
                        message = pickle.loads(data)
                        if message[0] == 'Log_Book_Login':
                            if  message[2]==user_info.check_user(username=message[1]):  
                                conn.sendall(pickle.dumps(True))
                                break
                            else:
                                conn.sendall(pickle.dumps(False))
                                break
                        elif message[0] == 'Log_Book_Register':
                            # do register stuff
                            flag = user_info.add_user_info(message[1], message[2], message[3], message[4], message[5])
                            if flag == True:
                                conn.sendall(pickle.dumps(True))
                            elif flag == False:
                                conn.sendall(pickle.dumps(False))
                            else:
                                print('it didnt work')

                            break
                        
                        elif message[0] == 'Buy_Ticket':
                            # do buy ticket stuff


                            pass
                        else:
                            print('How did you end up here?! Did you divide by 0?')
                        # No s.close is needed

if __name__ == '__main__':
    ServerConnectionManager()