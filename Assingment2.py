#Qustion 1:
n = int(input("enter a number :"))
if(n % 2 == 0):
    print(f"{n},Is a even number")
else:
    print(f"{n},Is a odd number")


#Question 2:
sum = 0 
for i in range(51):
    sum += i
print(f"The sum of number from 1 to 50 is {sum}")