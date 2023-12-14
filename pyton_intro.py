import mylib

print('Hello, Django girls!')
if 3 > 2:
    print('It works!')
else:
    print('Estoy en else')

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("Me duelen las orejas! :(")


mylib.hi("Pepe")

girls= ['Ana', 'María', 'Carol']
for name in girls:
    mylib.hi(name)