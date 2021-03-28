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

squares = [value ** 2 for value in range(1, 11, 2)]
print(squares)
print(squares[1:2])
squares_2=squares[1:]
print(squares_2)