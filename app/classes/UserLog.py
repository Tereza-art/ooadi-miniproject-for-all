import pandas as pd
class UserLog:
    def __init__(self):
        self.log = pd.DataFrame(columns=['user_id','fullname', 'username', 'e_mail', 'phone', 'password'])
    def add_user_info(self, fullname, username, e_mail, phone, password):
        if e_mail in self.log['e_mail'].values:
            #print("Email already exists!")
            return False
        elif username in self.log['username'].values:
            #print("Username already exists!")
            return False
        else:
            new_user = pd.DataFrame({'user_id': len(self.log.index),
                             'fullname': fullname,
                             'username': username,
                             'e_mail': e_mail, 
                             'phone': phone,
                             'password': password}, index=[len(self.log.index)])
            self.log = pd.concat([self.log, new_user], ignore_index=True)
            return True
    def get_user_info(self, e_mail):
        return self.log.loc[self.log['e_mail'] == e_mail]

    def check_user(self, username):
        try:
           df =  self.log[self.log['username']==username]
           credential = df['password'].to_string(index=False)
           return credential

           crendential.as_type('string')
        except:
            return False


    #def save_file(self,log):
    #def read_user():


if __name__== "__main__":
    user_info = UserLog()
    user_info.add_user_info('john wick', 'john', 'john@gmail.com', 123, 123)
    user_info.add_user_info('cat', 'john D', 'john@gmail.com', 145,145)
    user_info.add_user_info('dog', 'dog the dog', 'dog@gmail.com', 19,19)
    

