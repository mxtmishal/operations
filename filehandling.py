#     CREATE A NEW FILE

# file = open("example.txt","a")

# file.write("Hello mishal! \n")
# file.write("This is file handling in python")

# content=file.read()
# print(content)
# file.close()


#   USING WITH


#  write
with open("demo.txt","w") as file:
    file.write("python is easy")

# append
with open("demo.txt","a") as file:
    file.write("\nLearning file handling")
    
# read
with open("demo.txt","r") as file:
    print("file.read")




