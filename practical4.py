from datetime import datetime

class Users:
    # user class
    def __init__(self, name, age, dateJoined):
        self.name = name
        self.age = age
        self.dateJoined = dateJoined
    
    def __str__(self) -> str:
        return self.name


# test user list 
userList = [
    Users("Daniel", 19, datetime.now()),
    Users("Dan", 15, datetime.now()),
    Users("Mike", 19, datetime.now()),
    Users("Fem", 16, datetime.now()),
    Users("Susan", 20, datetime.now()),
    Users("Yasmeen", 29, datetime.now()),
    Users("Rebecca", 23, datetime.now()),
    Users("Maya", 18, datetime.now()),
]

def paginateUsers(userList, pageNumber, pageSize):
    # this function returns the paginated result of the list passed,
    # depending on the pageNumber and pageSize
    paginatedResult = []
    length = len(userList)
    start = (pageNumber - 1) * pageSize
    pageEnd = pageSize * pageNumber
    end = length if  pageEnd > length else pageEnd
    paginatedResult = [str(userList[i]) for i in range(start, end)]
    return paginatedResult


print(paginateUsers(userList, 2, 2))