## text to emojis

```python
emoji_dict = {":)": "😊", ":(": "😞", ":D": "😃", ":P": "😛", ":O": "😲", ":/": "😕", ":*": "😘", "<3": "❤️", ";)": "😉"}

message = input('>')

words = message.split(' ')

output = ''

for word in words:
    output += emoji_dict.get(word, word) + " "

print(output)

```
