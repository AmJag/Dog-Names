import random

foods = ['italian', 'mexican', 'chinese']
def dinner_options(food): 
  
  italian = ['pizza', 'pasta', 'calzone', 'al arabiatta']
  mexican = ['burrito', 'burrito bowl', 'tostatas', ' tacos']
  chinese = ['dim sum', 'chow mein', 'bao zi', 'pho']
  if food == 'italian':
    return italian
  elif food == 'mexican':
    return mexican
  elif food == 'chinese':
    return chinese

chosen_food = random.choice(foods)
print(random.choice(dinner_options(chosen_food)))
