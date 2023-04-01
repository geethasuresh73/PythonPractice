numbers="8;7'8*8789;;7"
for a in numbers:
    if not a.isnumeric():
       numbers=numbers.replace(a,'')
       break

print(numbers)

for a in numbers:
    if not a.isnumeric():
       numbers=numbers.replace(a,'')
       continue
       print("I am continuing the code")

print(numbers)

for a in numbers:
    if not a.isnumeric():
       numbers=numbers.replace(a,'')
       pass
       print("I am continuing the code")

print(numbers)
