"""
Chatbot
Author: 
Period/Core: 

"""

import os
import importlib.util

import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")


if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()
    
    
    
    
    
    x=input("Hi whats your name")
print(x + " That's a cool name")


n=input("whats your favorite sport")
b=0
# line 8-29 are all  about the sport question
if((n =="basketball" )):
  print("I like basketball too")

if((n =="baseball" )):
  print("Baseball is pretty cool but I like lacrosse a little more")

if((n =="soccer" )):
  print("I really like soccer I even played it for a while")

if((n =="motorcross" )):
  print("Motorcross is my favorite too")

if((n =="tennis" )):
  b=input("I have never tried tennis is it fun")
if((b == "yes")):
  print("cool maybe I'll try it sometime")

if((b == "yeah")):
  print("cool maybe I'll try it sometime")

if((n == "football")):
  print(" Football looks pretty fun")

t=input(" How was your day so far today")

if((t == "good" or  "great")):
  print(" Thats awesome")
else:
    print("well Im sorry about that")



#this is where the random number generator but now im stuck


answer=input(" Guess a number 1-10")
import random
number=random.randint(1,10)
while answer != number:
  if answer >= number:
    print ("Too high!")
  else:
    
    print ("Too low!")
  answer = int(input("Try again!"))
 
print ("Congratulations!")

    
