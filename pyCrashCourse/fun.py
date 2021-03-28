def greet_user(user_name):
    """简单的打招呼"""
    print("hello " + user_name)


def dog_inf(name, master, kind='jinmao'):
    print(name + "'s master is " + master + ".  " + kind)


def pizza(size, *toppings):
    toppings_inf = ""
    for topping in toppings[0:-1]:
        toppings_inf += topping + " ,"
    toppings_inf += toppings[-1]
    print("your pizza is " + str(size) + "\ntoppings:" + toppings_inf)


def student(name, **inf):
    infor = ""
    for keys, values in inf.items():
        infor += keys + ":" + values + "\n"
    print(infor)



