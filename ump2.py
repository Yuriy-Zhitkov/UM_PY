
import os

class Ump:


    def __init__(self, path: str):
    # path - адрес .mvc
        self.path = path


    def info(self):
        folder = os.path.basename(os.path.dirname(self.path))  # название папки (проекта)
        print(folder)


    def structure(self):
        family = {} # семейства
        level = [] # уровни
        i_f = 0 # счетчик номеров семейств
        i_l = 0 # счетчик номеров уровней
        file = open(self.path, 'r', encoding='cp1251')
        multi = list(file)
        for count, el in enumerate(multi, start=0):
            if el == 'with family;\n':  # если находим семейство, то
                i_f += 1
                family_name = multi[count + 1].replace('  name="', '').replace('";\n', '')
                family[('family_' + f'{i_f}')] = {'name': f'{family_name}',
                                                  'version': None}
                level.append([]) # создаем список для уровней


            elif el == '  with level;\n':  # если находим уровень, то
                level_name = multi[count + 1].replace('    caption="', '').replace('";\n', '')
                level_value = multi[count + 3].replace('      listitems=', '').replace(';\n', '')
                level[i_f - 1].append({'name': f'{level_name}',
                                       'value': f'{eval(level_value)}'})
                # level[i_f - 1].append({'name': f'{multi[count + 1]}'})
                # level[i_f - 1].append({'value': f'{eval(level_value)}'})
            else:
                continue
        file.close()
        return family, level
        # print(family)
        # print(level)




a = Ump('/Users/Yuriy_IT/Documents/Test Loco Lavels/multi.mvc')
# a = Ump('/Users/Yuriy_IT/Documents/R/Обработка UM Result/2ТЭ35А 25000/multi.mvc')
# a = Ump('/Users/Yuriy_IT/Documents/Сравнение Loco 00.16a и 17b/multi.mvc')
a.info()
b = a.structure()

for el in b[0]:
    print(el)

for el in b[1]:
    print(el)


print((b[0]))
# print((b[1]))
