import random


def randomator(L):
   random.shuffle(L)
   from milestone03_NicholasShaw import randomator
   return random.choice(L)
   
def importer(T):
    with open(T, 'r') as file:
        from milestone03_NicholasShaw import importer
        return file.read().splitlines()

