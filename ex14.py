from sys import argv

[script, user_name] = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you some questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"""
Ok, so likes is {likes} and lives is {lives}. 
Cool.
""")



