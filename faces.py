userinput = input("Enter a string with text faces: ")

# Replace text faces with emojis
modifiedinput = userinput.replace(":)", "🙂").replace(":(", "🙁")

print("Modified string:", modifiedinput)
