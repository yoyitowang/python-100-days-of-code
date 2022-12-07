import art, game_data
import random
from replit import clear


def get_random_data():
    return random.choice(game_data.data)

def check_answer(guess, af, bf):
  if af['follower_count'] > bf['follower_count']:
    return guess == 'a'
  else:
    return guess == 'b'


if __name__ == '__main__':
    game_on = True
    score = 0
    b = get_random_data()
  
    while game_on:    
      a = b
      b = get_random_data()
      while a == b:
        b = get_random_data()
      clear()
      print(art.logo)
      print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
      print(art.vs)
      print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")
      answer = input(f"Who has more followers? Type 'A' or 'B': ").lower()
      if not check_answer(answer, a, b):
        game_on = False
      
    # print logo
