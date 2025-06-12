import random

#randint()
#randrange()

# print(f'Printing random integer {random.randrange(0,10)}')
# random.choice

# name = ["Kyaw","Khine","Zaw","Lin","Naing"]
# print(f"Select element: {random.choice(name)}") 

# random.sample
name = ["Kyaw","Khine","Zaw","Lin","Naing"]
print(f"Select element: {random.sample(name,3)}") 

# random.seed()
random.seed(10)
print(f'Random.seed : {random.random()}')