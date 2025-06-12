#CSPRNG
#Cryptographically strong Pseudo-Random Number Generator
#Random
#secrets 3.6

import secrets 
print("Printing integer number using secrets modules")
secureGenerator = secrets.SystemRandom()
randomNumber = secureGenerator.randint(0,10)
print(randomNumber)