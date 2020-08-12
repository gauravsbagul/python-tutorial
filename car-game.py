command = ""
started = False
print("""
start - to start the car
stop - to stop the car
quit - to quit the game
        """)
while True:
    command = input("> ").lower()

    if command == 'start':
        if started:
            print("Car Already started...")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Card stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the game
        """)
    elif command == 'quit' or command == 'exit':
        print("Game terminated")
        break
    else:
        print("Sorry, I don't understand that")
