user_name = input("Enter Name: ")


def printName(user_name):

    for i in range(len(user_name)):
        for j in range(len(user_name)):
            if i == j:
                print(f"{user_name[i]}", end="")
            else:
                print(' ', end="")

        print('\n')


printName(user_name)