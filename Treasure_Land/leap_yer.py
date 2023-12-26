year =2020

def new_func(year):
    if year % 400 == 0:
      print('Leap year')
    else:
      print('Not leap year')

if year % 4 == 0:
    # print('Leap year')
    if year % 100 == 0:
     new_func(year)

    else:
     print('Leap year')
    
  
else:
  print('Not leap year')