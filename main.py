#method 1 using for loop
#
number=int(input("Enter Armstrong Number:"))
armstrong_number=number 
sum=0 
for i in str(number):
  each_digit=armstrong_number%10
  sum+=each_digit**len(str(number))
  armstrong_number=armstrong_number//10
if(sum==number):
  print(f'${number} is a Armstrong Number')
else:
   print(f'{number} is Not a Armstrong Number')


#method 2 using while loop 
  
number=int(input("Enter Armstrong Number:"))
armstrong_number=number 
sum=0 
while armstrong_number >0 :
  each_digit=armstrong_number%10
  sum+=each_digit**len(str(number))
  armstrong_number=armstrong_number//10
if(sum==number):
  print(f'${number} is a Armstrong Number')
else:
   print(f'{number} is Not a Armstrong Number')