def age_checker(age):
  age = int(input('What is your age?'))
  if age>= 18:
    print('Powering On. Enjoy the ride!')
  elif age<18:
    print('Sorry, you are too young to drive this car. Powering off')
    
age_checker(1)    