emoji_dict = {":)": "😊", ":(": "😞", ":D": "😃", ":P": "😛", ":O": "😲", ":/": "😕", ":*": "😘", "<3": "❤️", ";)": "😉"}

message = input('>')


words = message.split(' ')

output = ''

for word in words:
    output += emoji_dict.get(word, word) + " "

print(output)









# my_dict = {1: "one", 2: "two", 3: "three", 4: "one", 5: "two", 6: "three", 7: "one", 8: "two", 9: "three", 10: "one"}

# phone_number = input('Phone Number: ')

# # for digit in [int(phone_number) for phone_number in str(phone_number)]

# for digit in phone_number:
#     print(my_dict[int(digit)], end=" ")

