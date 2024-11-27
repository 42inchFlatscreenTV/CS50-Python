#Ask user for their name
name = input("What's your name? ")

#Removes white space from str and capitalises user's name
name = name.strip( ).title( )

#Say hello to user
print(f"Hello, {name}")