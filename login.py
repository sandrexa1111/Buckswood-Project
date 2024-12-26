
class Login:
    def __init__(self):
        self.credentials = {}

    def register(self, username, password):
        self.credentials[username] = password

    def check(self, user, pas):
        print(self.credentials)
        if user in self.credentials.keys() and pas == self.credentials[user]:
            print("Login success!")
        else:
            print("Wrong Username or Password")


s = Login()

Stop = False

while Stop == False:
    tasks = input("What would you like to do? Enter [Register], [Login], or [quit]: ")

    if tasks == 'Register':
        Name = input("Please enter username: ")
        Pword = input("Please enter password: ")
        s.register(Name, Pword)

    if tasks == 'Login':
        LoginInfoUser = input("Please enter Username: ")
        LoginInfoPassword = input("Please enter Password: ")
        s.check(LoginInfoUser, LoginInfoPassword)

    if tasks == 'quit':
        print("See you later!")
        Stop = True
