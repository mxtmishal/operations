#     CREATE A NEW FILE

# file = open("example.txt","a")

# file.write("Hello mishal! \n")
# file.write("This is file handling in python")

# content=file.read()
# print(content)
# file.close()


#   USING WITH


#  write
# with open("demo.txt","w") as file:
#     file.write("python is easy")

# append
# with open("demo.txt","a") as file:
#     file.write("\nLearning file handling")
    
# read
# with open("demo.txt","r") as file:
#     print("file.read")



#//////////////////////////////////////////////////////


# f = open('sample.txt','w')
# for i in range(1,11):
#     f.write('Hello'+'\n')
    
# f = open('sample.txt','r')

# data = f.read(4)
# print(f.tell())
# f.seek(0)
# print(f.tell())
# data1 = f.read()



# print(data)
# print(data1)    


# first_line = f.readline(2)
# remaining = f.readline()
# print(first_line)
# print(remaining)


