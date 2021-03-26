message = "this is a message"
print(message.title().rsplit())
message = message.rsplit()
message.append('!')
print(message)
message[1] = "isn't"
print(message)
del message[0]
print(message)
message.remove('a')
print(message)
print(len(message))
