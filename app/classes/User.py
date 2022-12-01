class User:
    def __init__(self, user_id, fullname, username, e_mail, phone, password):
        self.user_id = user_id
        self.fullname = fullname
 
        self.username = username
        self.e_mail = e_mail
        self.phone = phone    
        self.password = password    
    def __repr__(self):
      return "Name: {}, Email: {}, Phone: {}".format(
        self.username,
        self.e_mail,
        self.phone)  
    def reset_password(self):
        old_pwd = input("Please Enter the password you want to reset: ") #password need some extra security?
        if old_pwd == self.password:
            new_pwd = input("Please enter your new password: ")
            self.password = new_pwd
        else:
            raise ValueError
        #enter the old password to reset password