from command import rover

if __name__ == '__main__':

    print("Write initial coordinates in the form x,y,direction")

    initial_state = tuple(input().split(","))

    receiver = rover.Rover(initial_state)

    while True:
        print("the receiver is at the position", receiver.get_state())
        print("Write command:")
        command_parameters = input()
        receiver.move(command_parameters)
        print(receiver.get_state())


