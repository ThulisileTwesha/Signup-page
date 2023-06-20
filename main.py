
def signin():

    question = input("Already have an account? Yes or No")
    print("select operation")
    print("1.yes")
    print("2.no")

    if(question == "1"):
      login()
    if(question == "2"):
        register()

def login():
    print("login")
    user = input("username")
    password = input("password")
    lists = [['karabo', '12345'], ['dineo', '2345678'], ['solomon', '45678'], ['thabo', '12345'], ['cheif', '23456']]
    for i in range(len(lists)):
        if user == lists[i][0]:
            print('similar')
            userinfo = lists[i]
            username = userinfo[0]
            userpass = userinfo[1]
            print(username,userpass)
            if user == username and password == userpass:
                print('successfully logged in')
                options()



def register():
    print('register')
    user = input("username")
    identity = input("id_number")
    password = input("password")
    if len(password) < 6:
        print('Password should contain more than 6 digits')
        input("Enter your password again")
    elif len(password) > 6:
        print(input("Confirm password"))
        print('Account successfully created')
    login()





def options():
    print('Welcome')

signin()

