local_val = 'magical unicorns'
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

# Now we have a document with a local variable, a function and a class. If we run this document form the command line, we will see no results. We haven't asked to print anything, nor have we called our function or class method. As we know, without printing, it's difficult to know what our code did when it ran. Let's look at our code by running our functions and printing the result. 

# In the same file, add the following below the User class
print(square(5))
user = User('Anna')
print(user.name)
print(user.say_hello())

if __name__ == "__main__":
    print("The file is being executed directly")
else:
    print("the file is being executed because it is being imported by another file. The file is called:", __name__)