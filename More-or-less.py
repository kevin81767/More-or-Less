
     #More-Or-Less

import os
from random import randrange



the_number = randrange(1,101)
the_number=int(the_number)   #Conversion of the number in int
user_number=int()
user_name=input("what's your name? ")  #The name of the user


while user_number != the_number:  
       print("Guess the number: ")
       user_number=input()
       user_number=int(user_number)
       if the_number > user_number:
           print(" It's More.")      #Au cas ou ca sere superieur
       elif the_number < user_number:
               print(" It's Less.")   #Au cas ou ca sere inferieur
       else:
                   print(" Congratulation ",user_name," you find the right number")   #Au cas ou il gagne


                   os.system("pause")



                  
