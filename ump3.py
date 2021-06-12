
import os
import itertools as it





class Ump:


    def __init__(self, path: str):
    # path - адрес .mvc
        self.path = path


    def info(self):
        folder = os.path.basename(os.path.dirname(self.path))  # название папки (проекта)
        print(folder)


    def structure(self):
        family = [] # семейства
        level = [] # уровни
        i_f = 0 # счетчик номеров семейств
        file = open(self.path, 'r', encoding='cp1251')
        multi = list(file)
        for count, el in enumerate(multi, start=0):
            if el == 'with family;\n':  # если находим семейство, то
                family.append([])
                level.append([]) # создаем список для уровней
                i_f += 1
                i_l = 0  # счетчик номеров уровней
                family_name = multi[count + 1].replace('  name="', '').replace('";\n', '')

                family[i_f - 1] = {'fml_num': i_f,
                                   'name': f'{family_name}',
                                   'version': None}
            elif el == '  with level;\n':  # если находим уровень, то
                i_l += 1
                level_name = multi[count + 1].replace('    caption="', '').replace('";\n', '')
                level_value = multi[count + 3].replace('      listitems=', '').replace(';\n', '')
                level[i_f - 1].append({'lvl_num': i_l,
                                       'name': f'{level_name}',
                                       'value': eval(level_value)})


            else:
                continue
        file.close()
        return family, level
        # print(family)
        # print(level)

    def hierarchy(self, family: list, level: list):
        hrh = {'family': [], }

        return hrh





# a = Ump(r'/Users/Yuriy_IT/Documents/Test Loco Lavels/multi.mvc')
# a = Ump(r'/Users/Yuriy_IT/Documents/R/Обработка UM Result/2ТЭ35А 25000/multi.mvc')
# a = Ump(r'/Users/Yuriy_IT/Documents/Сравнение Loco 00.16a и 17b/multi.mvc')
a = Ump(r'/Users/Yuriy_IT/Documents/UM_PY/Test_01/multi.mvc')
a.info()
b = a.structure()

for el in b[0]:
    print(el)

for el in b[1]:
    print(el)


print(len(b[0]))
print(len(b[1]))

