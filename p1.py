print ("Hello world!")
a = str (input ("Имя студента: "))
b = str (input ("Фамилия студента: "))
c = int (input ("Год рождения студента: "))
print (a + ' ' + b + ' ' + str (c))
d = a
a = b
b = d
c = c + 60
print (a + ' ' + b + ' ' + str (c))
