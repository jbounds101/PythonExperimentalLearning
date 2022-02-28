# Section: Files
f = open('data.txt', 'w')  # create a data.txt file with write privileges
f.write('Hello\n')
print(f.write('world!\n'))  # returns the number of characters printed
f.close()

f = open('data.txt')  # reading is the default operation
text = f.read()  # files are always read as strings
print(text)
f.close()
