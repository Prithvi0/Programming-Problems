"Take username as input and Replace String Template 'Hello <UserName>, How are you?'"

def username(u):
    
    # check if the user input is minimum of 3 characters   
    if len(u) >= 3:
        return "Hello " + u + ", How are you?"
    return "Enter more than 3 characters"

user= input("Enter a username (Minimum of 3 characters): ")
print(username(user))