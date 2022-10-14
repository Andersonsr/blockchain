from os import listdir
from random import randint
from user import User


class Manager:
    def __init__(self):
        self.usersAddr = listdir('users/')
        self.users = [User('users/{}/'.format(e)) for e in self.usersAddr]
        print(self.users)

    def randomUser(self):
        return self.users[randint(0, len(self.users))]


if __name__ == '__main__':
    man = Manager()
