def greet(name):
    """Greet the user"""
    return f"Hello, {name}!"

def main():
    """Main function to execute the program"""
    name = input("Please enter your name: ")
    greeting = greet(name)
    print(greeting)

if __name__ == "__main__":
    main()
