
### 1: Insert
    '''
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
     '''
        
### 2: Find
    '''
    # Loop through the list and find the user object with the given username
    def find(self, username):
        # for all user objects in users and check whether its username is equal to given username
        for user in self.users:
            if user.username == username:
                return(user)
    '''

### 3: Update
    '''
    # find the user object matching the user and replace the entries of that object
    def update(self, user):
            # using find() function to find the target user object
            target = self.find(user.username)
            print(target)
            # update the info (name and email)
            target.name, target.email = user.name, user.email
    '''

### 4: List All
    '''
    # print the representation or list of user objects
    def list_all(self):
        return self.users
    '''

