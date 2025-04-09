# Task 1: Read a File and Handle Errors
# try:
#     file = open('Assingment4/sample.txt','r+')
#     f = file.readlines()
#     print('Reading the content of file')
#     x = 1
#     for i in f:
#         print(f"line {x}: {i}",end=" ")
#         x+=1
# except FileNotFoundError  as e:
#     print(f"Error: The file 'sample.txt' not found")
#     file.close()



#Task 2: Write and Append Data to a File
file = open('Assingment4/output.txt','r+')
file.write(input("Enter text to write to the file:")+'\n')
print(f"Data successfully written to the 'output.txt'",'\n')

file.write(input("Enter additional text to append:"))
print('Data Successfully accepted!','\n')

file.seek(0)
print(f"final content of output.txt")
print('\n'.join(i.strip() for i in file.readlines()))
file.close()