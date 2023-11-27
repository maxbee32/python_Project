print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill =0
if height >= 120:
    print('You can ride a rollercoster!')
    age = int(input('What is your age? '))
    if age <= 12:
      bill =5
      print(f'Your bill is ${bill}')
    elif age <= 18:
      bill =7
      print(f'Your bill is ${bill}')
    elif age >= 45 and age >= 55:
      print('Everything is going to be ok. Have a free ride on us!')
    else:
      bill =12
      print(f'Your bill is ${bill}')
    want_photo = input('Do you want a photo taken? Y or N ')
    if want_photo == 'Y':
        bill += 3
        print(f'Your bill is ${bill}')
    
else:
    print('Sorry, you are not tall enough to ride this rollercoaster.')
