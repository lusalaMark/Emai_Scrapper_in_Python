import re

text = "random string. mymother@website.com. mark is coming. lusala-mark17@gmail.com."

pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")

result = pattern.findall(text)

print(result)