
user_input = None
largest = None
smallest = None
user_input = raw_input('Enter the number')
try: 
     user_input = int(user_input)
except:
    print('Invalid input')
    quit()
largest = (user_input)
smallest = (user_input)
while user_input != 'done':
    user_input = raw_input('Enter the number')
    if(user_input == 'done'):
        break
    try:
        if(user_input!= 'done'):
            int(user_input)
    except:
        print('Invalid input')
        continue
    if(int(user_input)< smallest):
        smallest = int(user_input)
    if(int(user_input)> largest):
        largest = int(user_input)
 
           
print'Maximum is ',largest
print'Minimum is ',smallest