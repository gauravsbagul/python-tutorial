# def greet_user(first_name, last_name):
#     print(f'Hi, there {first_name} {last_name}!')
#     print('Welcome aboard')
#
# print("Start")
# first_name = input('Enter name: ')
# greet_user(first_name, 'bagul')
#
# print("finish")


# def square(number):
#     return number * number
#
#
# print(f'square of 3 is: {square(3)}')


def greet_with_emoji(message):
    emojis = {
        ":)": "😊",
        ":(": "🙁"
    }
    words = message.split(" ")
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(greet_with_emoji(input("> ")))



