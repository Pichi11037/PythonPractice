from fileManager import FileManager

# with open('test.txt', 'w+', encoding='utf8') as f:
#     string = 'hola mundo'
#     for s in string:
#         f.write(s + '\n')
#     print(f.read())
    

with FileManager('test.txt') as f:
    print(f.readlines())