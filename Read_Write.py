file = open('data.txt', 'r')  # opening the file to read
print(file.read())
print(file.readline())
print(file.readline())

File = open('data1.txt', 'w')
File.write('I like to travel to ladak\n')
File.write('I love ns2oo bike\n')
File.write('atmecs')
File.close()
File = open('data1.txt', 'w')
File.write('software\n')
File = open('data1.txt', 'a')
File.write('engineer')

for data in file:
    File.write(data)





