from os import listdir
from random import randint
from user import User


class Manager:
    def __init__(self):
        self.usersAddr = listdir('users/')
        self.users = []

    def randomUser(self):
        return self.users[randint(0, len(self.users))]

    def loadUsers(self):
        for e in self.usersAddr:
            self.users.append(User('users/{}/'.format(e)))

    def printUsersKeys(self):
        for e in self.users:
            e.printKeysPEM()


if __name__ == '__main__':
    man = Manager()
    man.loadUsers()
    man.printUsersKeys()