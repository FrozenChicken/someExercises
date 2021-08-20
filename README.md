Since we are learning Python, sometimes it might be useful to convert text from lowerCamelCase to snake_case. 
The main trick is to find the correct place where to insert an underscore.
Let's make a rule that it's right before a capital letter of the next word. 
If the first letter is capitalized, convert it to lowercase and don't forget to insert an underscore before it.







text = list(input())
new_text = []
for char in text:
    if char.isupper():
        new_text.append('_')
        new_text.append(char.lower())
    else:
        new_text.append(char)
print(''.join(new_text).strip('_'))
