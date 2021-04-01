import json


class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def return_object(self):
        return {'name': self.name,
                'age': self.age,
                'address': self.address}


users = []
wsp = User('wsp', 21, '华中科技大学')
mmf = User('mmf', 19, '华中师范大学')
users.append(wsp.return_object())
users.append(mmf.return_object())
file_name = "numbers.json"
with open(file_name, 'w') as file:
    json.dump(users, file)

with open(file_name) as file:
    file_users = json.load(file)

for user in file_users:
    print(user['name'] + " is " + str(user['age']) + " years old.")

user_name = input("please input your name:")
user_file_path = user_name + '.json'
try:
    with open(user_file_path) as file:
        user_inf = json.load(file)
except FileNotFoundError:
    with open(user_file_path, 'w') as file:
        user_inf = {'name': user_name}
        password = input("please input your password:")
        user_inf['password'] = password
        json.dump(user_inf, file)
else:
    password = user_inf['password']
    print(user_name + ' your password is ' + password)