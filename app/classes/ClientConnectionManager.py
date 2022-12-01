import socket
import pickle

class ClientConnectionManager:
    def __init__(self,message):
        self.pickle_message = pickle.dumps(message) #dumps, from message serialised to binary streams


    def send_message(self):
        HOST = '127.0.0.1'
        PORT = 5000
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST,PORT))
            s.send(self.pickle_message)
            data = s.recv(1024)
        return pickle.loads(data)



'''
if __name__ == '__main__':

   
    message_to_send = ['Log_Book_Login','entered_fullname}','{entered_username}'] # message is a list of strings 
    manager = ClientConnectionManager(message_to_send)
    manager.send_message()

'''