#Task 1: Create a Dictionary of Student Marks
dict = {'Alice': 65 , 'Bob': 79 , 'cop': 80 , 'david': 99}
name = input("Enter the students name: ")
if ( name in dict ):
    print(f"{name} marks:",dict[name])
else:
    print("Student not found.")

#Task 2: Demonstrate List Slicing 
l = [1,2,3,4,5,6,7,8,9,10]
print(f"Origianl List : {l}")
ll = l[0:5]
print(f"Extracted first five elements :{ll}")
lll = ll[::-1]
print(f"revrse of extracted : {lll}")