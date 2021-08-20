





text = list(input())
new_text = []
for char in text:
    if char.isupper():
        new_text.append('_')
        new_text.append(char.lower())
    else:
        new_text.append(char)
print(''.join(new_text).strip('_'))
