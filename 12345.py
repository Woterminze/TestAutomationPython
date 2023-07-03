# a - запись новых данных в файл в его конец
# w - запись новых данных в файл, с удалением старых данных
# r - чтение
var = input("Write smthg ")
fw = open('test/file.txt', 'a')  #открытие и дозаписывание в конец
fw.write("Hi dudes\n")  # то что вносим
fw.write(var)
fw.close()  # закрываем

var = input("Write smthg again ")
fw = open('test/file.txt', 'w')  #открытие и дозаписывание в конец
fw.write("Hi dudes\n")  # то что вносим
fw.write(var)
fw.close()  # закрываем

fr = open('test/file.txt', 'r')
text = fr.read()
fr.close()
print(text)