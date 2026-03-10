# number=0
# if number > 0:
  #   print("the number is positive")
# elif number < 0:
  #   print("the number is negative")
# else :
  #   print("the number is zero")
    

        
# if number % 2 == 0:
  #   print("the number is even")
# else:
  #   print(" the number is odd")
    
# if number>100:
 #    print("the number is greater than 100")
    

###########################


# text = input("Enter a string: ")

# for char in text:
   #  print(char)
    
######################################   
    
# text = input("Enter a string: ")

# count = 0
# for char in text:
   #  count = count + 1

# print(count)

######################################       
    
# text = input("Enter a string: ")

# count = 0
# for char in text:
    # if char.lower() in "aeiou":
    #     count = count + 1

# print(count)

#####################################

# text = input("Enter a string: ")

# for char in text:
  #   print(char.upper())
    
###########################################
    
text = input("Enter a string: ")

reverse = ""
for char in text:
    reverse = char + reverse

print(reverse)