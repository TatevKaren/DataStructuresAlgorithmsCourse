
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
### 3: Update
### 4: List All
