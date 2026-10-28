from random import randint

print("-----------\nYOUR TURN\n-----------") #Player section
random_card = randint(1, 13)
random_card2 = randint(1, 13)

if random_card == 1:
  print("Drew an Ace")
elif random_card == 8: 
    print("Drew an 8")
elif random_card >= 2 and random_card <= 10:
    print(f"Drew a {random_card}")
elif random_card == 11:
    print("Drew a Jack")
elif random_card == 12:
    print("Drew a Queen")
elif random_card == 13:
    print("Drew a King")
else:
    print("BAD CARD")

if random_card2 == 1:
  print("Drew an Ace")
elif random_card2 == 8: 
    print("Drew an 8")
elif random_card2 >= 2 and random_card2 <= 10:
    print(f"Drew a {random_card2}")
elif random_card2 == 11:
    print("Drew a Jack")
elif random_card2 == 12:
    print("Drew a Queen")
elif random_card2 == 13:
    print("Drew a King")
else:
    print("BAD CARD")

if random_card == 11 or random_card == 12 or random_card == 13:
  card_value = 10
elif random_card == 1:
  card_value = 11
else:
  card_value = random_card

if random_card2 == 11 or random_card2 == 12 or random_card2 == 13:
  card_value2 = 10
elif random_card2 == 1:
  card_value2 = 11
else:
  card_value2 = random_card2



hand_value1 = int(card_value + card_value2)

if hand_value1 < 21:
  user_answer = input(f"You have {hand_value1}. Hit (y/n)? ")

  while hand_value1 < 21 and user_answer != 'n':
    if user_answer == 'y': 
      random_card3 = randint(1, 13)
    
      if random_card3 == 1:
        print("Drew an Ace")
      elif random_card3 == 8: 
          print("Drew an 8")
      elif random_card3 >= 2 and random_card3 <= 10:
          print(f"Drew a {random_card3}")
      elif random_card3 == 11:
          print("Drew a Jack")
      elif random_card3 == 12:
          print("Drew a Queen")
      elif random_card3 == 13:
          print("Drew a King")
      else:
          print("BAD CARD")

      if random_card3 == 11 or random_card3 == 12 or random_card3 == 13:
        card_value3 = 10
      elif random_card3 == 1:
        card_value3 = 11
      else:
        card_value3 = random_card3
      hand_value1 = int(hand_value1 + card_value3)

    elif user_answer != 'n': 
      print("Sorry I didn't get that.")
    if hand_value1 < 21:
      user_answer = input(f"You have {hand_value1}. Hit (y/n)? ")



print(f"Final hand: {hand_value1}.")
if hand_value1 == 21:
  print('BLACKJACK!')
elif hand_value1 > 21 and hand_value1 <= 31:
  print('BUST.')


print("-----------\nDEALER TURN\n-----------") #Dealer Section
random_card = randint(1, 13)
random_card2 = randint(1, 13)

if random_card == 1:
  print("Drew an Ace")
elif random_card == 8: 
    print("Drew an 8")
elif random_card >= 2 and random_card <= 10:
    print(f"Drew a {random_card}")
elif random_card == 11:
    print("Drew a Jack")
elif random_card == 12:
    print("Drew a Queen")
elif random_card == 13:
    print("Drew a King")
else:
    print("BAD CARD")

if random_card2 == 1:
  print("Drew an Ace")
elif random_card2 == 8: 
    print("Drew an 8")
elif random_card2 >= 2 and random_card2 <= 10:
    print(f"Drew a {random_card2}")
elif random_card2 == 11:
    print("Drew a Jack")
elif random_card2 == 12:
    print("Drew a Queen")
elif random_card2 == 13:
    print("Drew a King")
else:
    print("BAD CARD")

if random_card == 11 or random_card == 12 or random_card == 13:
  card_value = 10
elif random_card == 1:
  card_value = 11
else:
  card_value = random_card

if random_card2 == 11 or random_card2 == 12 or random_card2 == 13:
  card_value2 = 10
elif random_card2 == 1:
  card_value2 = 11
else:
  card_value2 = random_card2

hand_value2 = int(card_value + card_value2)

if hand_value2 < 17:
    print(f"Dealer has {hand_value2}.")

while hand_value2 < 17:
    new_card = randint(1, 13)
    
    if new_card == 1:
        print("Drew an Ace")
    elif new_card == 8: 
        print("Drew an 8")
    elif new_card >= 2 and new_card <= 10:
        print(f"Drew a {new_card}")
    elif new_card == 11:
        print("Drew a Jack")
    elif new_card == 12:
        print("Drew a Queen")
    elif new_card == 13:
        print("Drew a King")
    else:
        print("BAD CARD")

    if new_card == 11 or new_card == 12 or new_card == 13:
        card_value3 = 10
    elif new_card == 1:
        card_value3 = 11
    else:
        card_value3 = new_card

    hand_value2 = int(hand_value2 + card_value3)
    if hand_value2 < 17:
        print(f"Dealer has {hand_value2}.")

print(f"Final hand: {hand_value2}.")

if hand_value2 == 21:
  print('BLACKJACK!')
elif hand_value2 > 21 and hand_value2 <= 31:
  print('BUST.')

print("-----------\nGAME RESULT\n-----------")

if hand_value1 > 21: 
  print("Dealer wins!")
elif  hand_value1 < hand_value2 and hand_value2 <= 21:
  print("Dealer wins!")
elif hand_value2 > 21:
  print("You win!")
elif hand_value1 > hand_value2:
  print("You win!")
else:
  print("Push.")