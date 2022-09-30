# class for creating users
class User():
    # defining the constructor of the class
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print("User {} Created! ".format(self.name))
    # build in function that takes in the name of the user and types back the information about the user
    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}: Contact me at {} ".format(guest_name, self.name, self.email))
    # building a function to create a string representation of the object
    def __repr__(self):
        return "User(username = '{}', name = '{}',email='{}')".format(self.username, self.name, self.email)
    def __str__(self):
        return self.__repr__()



class UserDatabase:
    # constructor
    def __init__(self):
        self.users = []
    # edge cases
    # A: empty database
    # B: inserting a user with username that already exists
    # C: inserting user with username that doesn't exist
    # Solution
    # Loop through the list and add a new user at a position that keeps the list sorted
    def insert(self, user):
        i = 0
        # going through all valid positions in the database
        while i < len(self.users):
            # Finding the first username  that alhpabetically comes later than the query user
            if self.users[i].username > user.username:
                   break
            i+=1
        # once the position is found, we then insert the user
        self.users.insert(i,user)

    # edge cases
    # A: Finding a user that doesn't exist
    # B: Finding a user with the same username
    # Solution
    # Loop through the list and find the user object with the given username
    def find(self, username):
        # for all user objects in users and check whether its username is equal to given username
        for user in self.users:
            if user.username == username:
                return(user)

    # edge cases
    # A: Updating a user that doesn't exist
    # Solution
    # find the user object matching the user and replace the entries of that object
    def update(self, user):
            # using find() function to find the target user object
            target = self.find(user.username)
            print(target)
            # update the info (name and email)
            target.name, target.email = user.name, user.email

    # print the representation or list of user objects
    def list_all(self):
        return self.users


# creating database
database = UserDatabase()

t = User("TK", "tg", "tgjudx@gmail.com")
l = User("LK", "lita", "lita@gmail.com")
v = User("hag", "vih", "vih@gmail.com")
s = User("SY", "hig", "hig@gmail.com")
k = User("KK", "vpous", "sp@gmail.com")

# inserting user
database.insert(t)
database.insert(l)
database.insert(v)
database.insert(s)
database.insert(k)


# finding a user
print(database.find("TK"))


# updating a user info
database.update(User(username = "TK", name = "Tatevik", email = "tatevkarenn@gmail.com"))
print(database.find("TK"))










