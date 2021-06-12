import os
import itertools as it


class Ump:

    def __init__(self, path: str):
        # path - адрес .mvc
        self.path = path


    def info(self):
        folder = os.path.basename(os.path.dirname(self.path))  # название папки (проекта)
        return folder


    def structure(self, print_info = False):

        family = []  # семейства
        level = []  # уровни

        i_f = 0  # счетчик номеров семейств
        file = open(self.path, 'r', encoding='cp1251')
        multi = list(file)
        for count, el in enumerate(multi, start=0):
            if el == 'with family;\n':  # если находим семейство, то
                i_f += 1
                family.append([])
                i_l = 0  # счетчик номеров уровней
                level.append([])  # создаем список для уровней
                family_name = multi[count + 1].replace('  name="', '').replace('";\n', '')
                family[i_f - 1] = {'fml_num': i_f,
                                   'name': f'{family_name}',
                                   'version': None}
            elif el == '  with level;\n':  # если находим уровень, то
                i_l += 1
                level_name = multi[count + 1].replace('    caption="', '').replace('";\n', '')
                level[i_f - 1].append({'lvl_num': i_l,
                                       'name': f'{level_name}'})
            elif el == '    with identifier;\n': # если находим группу идентификаторов, то
                id_value = multi[count + 1].replace('      listitems=', '').replace(';\n', '')
                id_weight = multi[count + 2].replace('      listweights=', '').replace(';\n', '')
                level[i_f - 1][i_l - 1]['id_value'] = id_value
                level[i_f - 1][i_l - 1]['id_weight'] = id_weight
                level[i_f - 1][i_l - 1]['id_name'] = []
            elif '      idennames=' in el:
                id_name = multi[count].replace('      idennames=', '').replace(';\n', '')
                level[i_f - 1][i_l - 1]['id_name'].append(id_name)
            else:
                continue
        file.close()

        if print_info == True:
            print(f'\nПроект сканирования: {self.info()}')
            print(f'Количество семейств: {len(family)}')
            for i in range(len(family)):
                print(family[i])
                print(f'\tКоличество уровней: {len(level[i])}')
                for j in range(len(level[i])):
                    print('\t' + f'{level[i][j]}')
        return family, level

    @staticmethod
    def hierarchy(family: list, level: list):
        hrh = []
        for el in family:
            hrh_list = {f'{key}': [] for key in el.keys()}
            hrh.append(hrh_list)

        return hrh


# a = Ump(r'/Users/Yuriy_IT/Documents/Test Loco Lavels/multi.mvc')
# a = Ump(r'/Users/Yuriy_IT/Documents/R/Обработка UM Result/2ТЭ35А 25000/multi.mvc')
# a = Ump(r'/Users/Yuriy_IT/Documents/Сравнение Loco 00.16a и 17b/multi.mvc')
a = Ump(r'/Users/Yuriy_IT/Documents/UM_PY/Test_01/multi.mvc')
a.info()
b = a.structure(print_info=True)

h = a.hierarchy(b[0], b[1])
print(h)

