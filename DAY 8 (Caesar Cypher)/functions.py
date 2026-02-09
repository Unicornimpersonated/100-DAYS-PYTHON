def greet():
    print("hello! Aneri")
    print("How do you do?")
    print("Isn't the weather nice?")

greet()

# Functions that allows for inputs

def greet_with_name(name):
    print(f"hello!{name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice?")

greet_with_name("Aneri")

# name is parameter
# Aneri is argument

# Functions with more than one input
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What it is like in {location}")

greet_with("Aneri","Indore")

def my_function(a,b,c):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")

my_function(b=2,c=4,a=1)
