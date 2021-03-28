import fun as f

message = input("what's your name?\n")
message += ",hello!"
print(message)
age = input("how old are you?")
age = int(age)
print(age)

responses = {}
print("enter 'quit' to quit")
while True:
    name = input("what's your name?")
    if name == 'quit':
        break
    response = input("how old are you?")
    if response == 'quit':
        break
    responses[name] = response
print(responses)
