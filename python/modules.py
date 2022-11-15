#Functions defined in other files can be imported and used in a different File
#This can be done by imorting the functions directly or imprting the specific file

from functions import square
for x in range(6):
    print(f"The square of {x} is {square(x)}")