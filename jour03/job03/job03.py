for i in range(101):
   if i != 26 and i != 37 and i != 88:
       print(i)
       
#Autre méthode

def print_numbers():
    for i in range(101):
        if i not in [26, 37, 88]:
            print(i)
            
#Autre méthode

def print_numbers():
    numbers_to_skip = {26, 37, 88}
    for i in range(101):
        if i not in numbers_to_skip:
            print(i)