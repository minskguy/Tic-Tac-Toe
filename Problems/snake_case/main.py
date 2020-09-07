camel_case = input()
phrase = list(camel_case)
processed = ""

for letter in phrase:
    if letter.isupper():
        processed += "_" + letter.lower()
    else:
        processed += letter
print(processed)
