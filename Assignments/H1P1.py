print("Enter your first name:")
first_name = input()

print ("Enter your last name:")
last_name = input ()

print ("Enter your age:")
age = int(input())

print ("Enter your confidence in programmers between 1-100%:")
confidence = int(input ())

dog_age = age * 7
print ("Hello",first_name, last_name, ", nice to meet you! You might be" ,age,"in human years, but in dog years you are",dog_age,".")


if (confidence<50):
  print ("I agree, programmers can't be trusted!")
elif (confidence>50):
  print ("Writing good code takes hard work!")
elif confidence == 50:  
    print("Professor Lindsay didn't instruct...You entered 50, though.")
