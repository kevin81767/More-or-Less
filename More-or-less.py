
     #More-Or-Less

import os
from random import randrange
import time



the_number = randrange(1,101)
the_number=int(the_number)   #Conversion of the number in int
user_number=int()
user_name=input("what's your name? ")  #The name of the user
user_trial=1


while user_number != the_number:  
       print("Guess the number: ")
       user_number=input()
       user_number=int(user_number)
       if the_number > user_number:
           print(" It's More.")      #In case the number is greater
           user_trial=user_trial+1
       elif the_number < user_number:
               print(" It's Less.")   #In case the number is lower
               user_trial=user_trial+1
       else:
                   print(" Congratulation ",user_name," you found the right number. With ",user_trial," trial")   #If the user win
                   print("")


                   time.sleep(3)



                  
