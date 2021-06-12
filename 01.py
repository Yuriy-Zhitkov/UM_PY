'''
Сбор информации о проектах УМ в указанной дирректории
'''

import glob, os


# Путь к файлам UM
UM_path = '/Users/Yuriy_IT/Documents/**/*.mvc'

# Функция №1 - сбор адресов проектов
# хранилище полных адресов в файлам с описанием проектов UM
# хранилище полных адресов к папкам проектов
UM = {'project_path': [], 'multi_path': [], 'project_name': []} # словарь хранилище
# заполнение словаря хранилища
for filename in glob.iglob('/Users/Yuriy_IT/Documents/**/*.mvc', recursive=True):
    UM['project_path'].append(filename.removesuffix('multi.mvc')) # путь к папке в формате */*/
    UM['multi_path'].append(filename) # полный путь к файлу
    UM['project_name'].append(os.path.basename(os.path.dirname(filename))) # название папки (проекта)
# print(UM)




# Функция №2 - разбор файла multi.mvc
# загрузка файла
multi = list(open(UM['multi_path'][0], 'r', encoding='cp1251'))
# хранилище информации о проекте, семействах, уровнях, значениях
UM_project = {'name': os.path.basename(os.path.dirname(UM['multi_path'][0]))}
# обработка информации о проекте

i_main = 1
i_family = [] # номера строк семейств
ind_family = [] # номер строки с названием семейства

i_level = [] # номер строк уровней семейств
ind_level = [] # номер строки с названием уровня

i_end = len(multi) # последняя строка файла

for i in range(len(multi)): # перебираем все строки файла

    if multi[i] == 'with family;\n': # если находим семейство, то
        i_family.append(i) # запоминаем индекс строки с которой начинается описание семейства
        ind_family.append(i + 1) # запоминаем индекс строки, где есть название семейства
        i_level.append([]) # создаем список для уровней
        ind_level.append([]) # создаем список для названий уровня
    elif multi[i] == '  with level;\n': # если находим уровень, то
        i_level[len(i_level) - 1].append(i) # запоминаем индекс строки, где есть название уровня
        ind_level[len(i_level) - 1].append(i + 1) # запоминаем индекс строки, где есть название уровня
    else:
        continue

print(i_level)







# Функция №3

import struct

#Чтение бинарных (двоичных) файлов
# файл Test.sgr также есть в папке проекта 04_Useful_tools
my_file = open(r'/Users/Yuriy_IT/Documents/R/Read UM Binnary/Test.sgr', 'rb')


# рабочий способ
data = my_file.read()
my_list = []
for i in range(int(len(data)/4)): # цифра 4 означает, что в 4 битах содержится единица информации
    el = data[i * 4 : i * 4 + 4] # срезаю из файла 4 бита
    el = struct.unpack('f', el) # преобразую бинарный формат в число с плавающей точкой (возвращается кортеж)
    my_list.append(list(el)[0]) # преобразую кортеж el в список и добавляю значение в свой список my_list
# print(my_list)

