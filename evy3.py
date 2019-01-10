#has output be a string a characters
import string

#has output be random assortment
from random import *

#has output be made of differnt numbers, punctuations, and digits
characters = string.ascii_letters + string.punctuation  + string.digits

#gives limits to output
password =  "".join(choice(characters) for x in range(randint(8, 16)))

#prints the actual password
print password
