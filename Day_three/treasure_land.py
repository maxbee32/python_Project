print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You are at a cross road. Where do you want to go? Type 'left' or 'right' \n")
if direction == 'left':
  print("You are at a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
  direction =input()
  if direction == 'wait':
    print('You arrived at the island unharmed. Thre is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?')
  else:
    print('Attacked by trout.Game Over.') 
    direction = input()
    if direction == 'red':
     print('Burned by fire. Game over!')
    elif direction == 'yellow':
     print('You found the treasure! You win!')
    elif direction == 'blue':
     print('You fell in the hole. Game over!')
    else:
      print('Invalid choice. Game over!')
else:
  print("You fell into a hole. Game over.")
  quit()
