print('\n\n')

import glob, os


def ump(path: str):
    '''
    Сбор адресов проектов UM (ориентир *.mvc)
    :param path: адрес папки для поиска
    :return: словарь: project_path - путь к папке проекта в формате */*/
                      multi_path - полный путь к файлу *.mvc
                      project_name - название папки (проекта)
    '''
    UM_path = path + '/**/*.mvc' # полный адрес для поиска *.mvc во всех вложенных папках
    UM = {'project_path': [], 'multi_path': [], 'project_name': []}  # словарь хранилище
    for filename in glob.iglob(UM_path, recursive=True):
        UM['project_path'].append(filename.removesuffix('multi.mvc'))  # путь к папке в формате */*/
        UM['multi_path'].append(filename)  # полный путь к файлу
        UM['project_name'].append(os.path.basename(os.path.dirname(filename)))  # название папки (проекта)
    return UM


def level(mlt_path: list, prj_name: list):

    UM_project = {}
    for count, mlt in enumerate(mlt_path, start=0):
        UM_project[('project_' + f'{count + 1}')] = {'name': prj_name[count], 'test': 'text123'}

        for i in range(len(mlt)):  # перебираем все строки файла
            multi = list(open(mlt, 'r', encoding='cp1251'))
            if multi[i] == 'with family;\n':  # если находим семейство, то
               UM_project[('project_' + f'{count + 1}')]['family_' + f'{i + 1}'] = {'name': f'{multi[i+1]}'}



        # !!!!! нужно дабавить в шаблон словаря - семейства, затем уровни!!!!!!!!№№№№№№№№№№

        # for i in range(len(multi)):  # перебираем все строки файла
        #     if multi[i] == 'with family;\n':  # если находим семейство, то
        #         UM_project[('Project_' + f'{count + 1}')][f'i'] = i
        #
        #     elif multi[i] == '  with level;\n':  # если находим уровень, то
        #         print(2)
        #         # i_level[len(i_level) - 1].append(i)  # запоминаем индекс строки, где есть название уровня
        #         # ind_level[len(i_level) - 1].append(i + 1)  # запоминаем индекс строки, где есть название уровня
        #     else:
        #         continue

        # print(UM_project)
    return UM_project








# a = ump('/Users/Yuriy_IT/Documents')
# # print(a)
#
# print(a['multi_path'])
#
# b = level(a['multi_path'], a['project_name'])
# # print(b['Project_1']['name'])
# print(b)

