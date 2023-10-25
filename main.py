def menu():
    print('Menu')
    print('-------------')
    print('1. Encoder')
    print('2. Decoder')
    print('3. Quit')


def encoder(user_password):
    password = ''
    for char in user_password:
        password += str(int(char) + 3)[-1]
    return password


# decoder done by Zachary Wright
def decode(pass_in):
    final_pass = ''
    for char in pass_in:
        final_pass += str(int(char) - 3)[-1]
    return final_pass


def main():
    encoded_pass = ''
    user_password = ''
    while True:
        menu()
        user_input = input('Please enter an option: ')
        if user_input == '1':
            user_password = input('Please enter your password to encode: ')
            encoded_pass = encoder(user_password)
            print('Your password has been encoded and stored!')
        elif user_input == '2':
            print(f'The encoded password is {encoded_pass}, and the original password is {user_password}')
        elif user_input == '3':
            break

if __name__ == '__main__':
    main()