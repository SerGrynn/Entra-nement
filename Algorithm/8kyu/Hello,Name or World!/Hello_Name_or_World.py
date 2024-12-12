# Le dernier test permet de tester les defaults value des fonctions
def hello(name =""):
    name = name.capitalize()
    if name == "":
        return "Hello, World!"
    else:
        return "Hello, " + name + "!"
    pass
