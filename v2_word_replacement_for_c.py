import sys
import re

sys.setrecursionlimit(10000)

input_file = r"C:\Users\Denis\PycharmProjects\Parser_cfg_for_iec61850\example_cfg\model_1_10.cfg"
output_file = r"C:\Users\Denis\Desktop\static_model_Sirius_model_1_10.c"

list_LD = []  # список с именами LD
list_LN = []  # список с именами LN
list_DO = []  # список с именами DO
list_DA1 = []  # список с именами DA 1 уровня
list_DA2 = []  # список с именами DA 2 уровня
list_DA3 = []  # список с именами DA 2 уровня
list_DA4 = []  # список с именами DA 2 уровня

list_param_DA1 = []  # список со значениями DA 1 уровня
list_param_DA2 = []  # список со значениями DA 2 уровня
list_param_DA3 = []  # список со значениями DA 2 уровня
list_param_DA4 = []  # список со значениями DA 2 уровня

index_listLD = 0  # так как все имена LD(Logical Device) записанны в одном массиве,
# index_listLD содержит индекс актуального(ещё не обработанного)
index_listLN = 0  # содержит индекс актуального LN(Logical Node)
index_listDO = 0
index_listDA1 = 0
index_listDA2 = 0
index_listDA3 = 0
index_listDA4 = 0

out_LD = 0
out_LN = 0
out_DO = 0
out_DA1 = 0
out_DA2 = 0
out_DA3 = 0
out_DA4 = 0


def LogialDevice(full_name, name, parent, sibling, first_child):
    with open(output_file, 'a') as f:
        list_for_write = "LogicalDevice {} = {}\n" \
                         "    LogicalDeviceModelType,\n" \
                         "    \"{}\",\n" \
                         "    {},\n" \
                         "    {},\n" \
                         "    {}\n" \
                         "{};\n" \
                         "   \n".format(full_name, "{", name, parent, sibling, first_child, "}")

        f.write(list_for_write)
    # print(full_name)
    f.close()


def LogicalNode(full_name, name, parent, sibling, first_child):
    with open(output_file, 'a') as f:
        list_for_write = "LogicalNode {} = {}\n" \
                         "    LogicalNodeModelType,\n" \
                         "    \"{}\",\n" \
                         "    {},\n" \
                         "    {},\n" \
                         "    {},\n" \
                         "{};\n" \
                         "   \n".format(full_name, "{", name, parent, sibling, first_child, "}")

        f.write(list_for_write)
    # print(full_name)
    f.close()


def DataObject(full_name, name, parent, sibling, first_child, elementCount=0):
    with open(output_file, 'a') as f:
        list_for_write = "DataObject {} = {}\n" \
                         "    DataObjectModelType,\n" \
                         "    \"{}\",\n" \
                         "    {},\n" \
                         "    {},\n" \
                         "    {},\n" \
                         "    {}\n" \
                         "{};\n" \
                         "   \n".format(full_name, "{", name, parent, sibling, first_child, elementCount, "}")

        f.write(list_for_write)
    # print(full_name)
    f.close()


def DataAttribute(full_name, name, parent, sibling, first_child, elementCount, fc, type, triggerOptions, mmsValue,
                  sAddr=0):
    with open(output_file, 'a') as f:
        list_for_write = "DataAttribute {} = {}\n" \
                         "    DataAttributeModelType,\n" \
                         "    \"{}\",\n" \
                         "    {},\n" \
                         "    {},\n" \
                         "    {},\n" \
                         "    {},\n" \
                         "    {},\n" \
                         "    {},\n" \
                         "    {},\n" \
                         "    {},\n" \
                         "    {}{};\n" \
                         "    \n".format(full_name, "{", name, parent, sibling, first_child, elementCount, fc, type,
                                         triggerOptions, mmsValue, sAddr, "}")

        f.write(list_for_write)
    # print(full_name)
    f.close()


"""

Данная функция считывает файл static_model.h и заполняет списки list_***

"""


def tree_reading():
    file = open(input_file, 'r')
    for line in file.readlines():
        output = line.find('extern LogicalDevice ')
        if output == 0:
            LD = line[(output + 21):(line.find(';', output + 20, len(line)))]  # выделяем имя логического девайся
            list_LD.append(LD)  # помещаем его в список логических девайсов
        else:
            output = line.find('extern LogicalNode   ')
            if output == 0:
                LN = line[(output + 21):(line.find(';', output + 20, len(line)))]
                list_LN.append(LN)
            else:
                output = line.find('extern DataObject    ')
                if output == 0:
                    DO = line[(output + 21):(line.find(';', output + 20, len(line)))]
                    list_DO.append(DO)
                else:
                    output = line.find('extern DataAttribute ')
                    if output == 0:
                        DA = line[(output + 21):(line.find(';', output + 20, len(line)))]
                        if DA.count('_') == 4:
                            list_DA1.append(DA)
                        elif DA.count('_') == 5:
                            list_DA2.append(DA)
                        elif DA.count('_') == 6:
                            list_DA3.append(DA)
                        elif DA.count('_') == 7:
                            list_DA4.append(DA)

    file.close()
    full_tree = [list_LD, list_LN, list_DO, list_DA1, list_DA2, list_DA3]
    print(" list_LD {} \n"
          " list_LN {} \n"
          " list_DO {} \n"
          " list_DA1 {} \n"
          " list_DA2 {} \n"
          " list_DA3 {} \n"
          " list_DA4 {}".format(list_LD, list_LN,
                                list_DO, list_DA1,
                                list_DA2, list_DA3,
                                list_DA4))


def tree_reading2():
    level = 0
    file = open(input_file, 'r')
    LD = ""
    LN = ""
    DO = ""
    DA1 = ""
    DA2 = ""
    DA3 = ""
    DA4 = ""
    global list_LD
    global list_LN
    global list_DO
    global list_DA1
    global list_DA2
    global list_DA3
    global list_DA4

    global list_param_DA1
    global list_param_DA2
    global list_param_DA3
    global list_param_DA4
    for line in file.readlines():

        ''' 
        Считали строку и в output проверяем, нет ли в ней LD
        если есть, то это LogicalDevice, нужно поместить его в соответствующий список
        и так проверяем каждую строку и помещаем название узлов в правильные списки
        '''
        output = line.find('LD')
        if output == 0:
            LD = "LD" + line[line.find("(") + 1:line.find(")")]  # выделяем имя логического девайся
            full_name = "iedModel_" + LD  # создаём полное имя
            list_LD.append(full_name)  # помещаем его в список логических девайсов
            # остановился тут
        else:
            output = line.find('LN')
            if output == 0:
                LN = line[line.find("(") + 1:line.find(")")]  # потом заменить(регулярки)
                full_name = "iedModel_" + LD + "_" + LN
                list_LN.append(full_name)
            else:
                output = line.find('DO')
                if output == 0:
                    DO = line[line.find("(") + 1:line.find(" 0") or line.find(")")]
                    full_name = "iedModel_" + LD + "_" + LN + "_" + DO
                    list_DO.append(full_name)
                else:
                    output = line.find('DA')
                    if output == 0:
                        DA_param = re.findall(r'\d+', line)
                        if level == 4:
                            DA1 = line[line.find("(") + 1:line.find(r" 0") or line.find(")")]
                            full_name = "iedModel_" + LD + "_" + LN + "_" + DO + "_" + DA1
                            list_DA1.append(full_name)
                            list_param_DA1.append(DA_param)
                        elif level == 5:
                            DA2 = line[line.find("(") + 1:line.find(r" 0") or line.find(")")]
                            full_name = "iedModel_" + LD + "_" + LN + "_" + DO + "_" + DA1 + "_" + DA2
                            list_DA2.append(full_name)
                            list_param_DA2.append(DA_param)
                        elif level == 6:
                            DA3 = line[line.find("(") + 1:line.find(r" 0") or line.find(")")]
                            full_name = "iedModel_" + LD + "_" + LN + "_" + DO + "_" + DA1 + "_" + DA2 + "_" + DA3
                            list_DA3.append(full_name)
                            list_param_DA3.append(DA_param)
                        elif level == 7:
                            DA4 = line[line.find("(") + 1:line.find(r" 0") or line.find(")")]
                            full_name = "iedModel_" + LD + "_" + LN + "_" + DO + "_" + DA1 + "_" + \
                                        DA2 + "_" + DA3 + "_" + DA4
                            list_DA4.append(full_name)
                            list_param_DA4.append(DA_param)
        if len(re.findall("{", line)):
            level += 1
        elif len(re.findall("}", line)):
            level -= 1

    file.close()
    # full_tree = [list_LD, list_LN, list_DO, list_DA1, list_DA2, list_DA3]
    print(" list_LD {} \n"
          " list_LN {} \n"
          " list_DO {} \n"
          " list_DA1 {} \n"
          " list_DA2 {} \n"
          " list_DA3 {} \n"
          " list_DA4 {} \n"
          "list_param_DA1 {} \n"
          "list_param_DA2 {} \n"
          "list_param_DA3 {} \n"
          "list_param_DA4 {}".format(list_LD, list_LN,
                                     list_DO, list_DA1,
                                     list_DA2, list_DA3,
                                     list_DA4, list_param_DA1,
                                     list_param_DA2, list_param_DA3,
                                     list_param_DA4, ))


"""

Функции **_handler созданы для определения параметров, 
которыми должны быть заполнены поля logicalDevice, LogicalNote и прочие

"""


def LD_handler(LD):
    global index_listLD
    global index_listLN
    global out_LD
    add_line = "(ModelNode*) &"
    full_name = LD  # полное имя устройства соотвествует записанному в список значению
    index = [i for i, symb in enumerate(LD) if symb == "_"]  # определяет позиции "_"
    name = LD[(index[0] + 1):len(LD)]  # имя содержится в полном имени после нижнего подчеркивания(_)
    parent = add_line + LD[0:index[0]]  # родитель содержится в полном имени до нижнего почеркивания
    try:  # попытаться в sibling записать имя следующего в списке устройства
        sibling = add_line + list_LD[index_listLD + 1]
    except IndexError:
        sibling = "NULL"  # если такой строчки нет, то ловим ошибку и записываем "NULL"
    first_child = "NULL"
    for i in range(len(list_LN)):  # для того чтобы заполнить поле first_child перебираем все значения
        if list_LD[index_listLD] in list_LN[i]:  # list_LN, при первом совпадении имён(если LN включает в себя LD)
            index_listLN = i  # записываем индекс найденного LN
            first_child = add_line + list_LN[i]
            break
    index_listLD += 1  # указываем на следующий элемент списка логических устройств

    LogialDevice(full_name, name, parent, sibling, first_child)  # вызываем функцию LogicalDevice для оформления LD

    if index_listLD == len(list_LD):
        out_LD = 1
    LN_handler(list_LN[index_listLN])  # вызываем функцию по заполнению полей найденого логического узла


def LN_handler(LN):
    global index_listLN
    global index_listDO
    global out_LN
    add_line = "(ModelNode*) &"
    full_name = LN
    index = [i for i, symb in enumerate(LN) if symb == "_"]  # определяет позиции "_"
    name = LN[(index[1] + 1):len(LN)]
    parent = add_line + LN[0:index[1]]
    try:
        # print(list_LN[index_listLN], list_LN[index_listLN + 1])
        if list_LD[index_listLD - 1] in list_LN[index_listLN + 1]:
            # print(list_LN[index_listLN], list_LN[index_listLN + 1])
            sibling = add_line + list_LN[index_listLN + 1]
        else:
            sibling = "NULL"
    except IndexError:
        sibling = "NULL"
    first_child = "NULL"
    for i in range(len(list_DO)):
        if list_LN[index_listLN] in list_DO[i]:
            index_listDO = i
            first_child = add_line + list_DO[i]
            break
    index_listLN += 1
    LogicalNode(full_name, name, parent, sibling, first_child)

    if index_listLN == len(list_LN):
        out_LN = 1
    DO_handler(list_DO[index_listDO])


def DO_handler(DO):
    global index_listDO
    global index_listDA1
    global out_DO
    add_line = "(ModelNode*) &"
    full_name = DO
    index = [i for i, symb in enumerate(DO) if symb == "_"]  # определяет позиции "_"
    name = DO[(index[2] + 1):len(DO)]
    parent = add_line + DO[0:index[2]]
    try:
        if list_LN[index_listLN - 1] in list_DO[index_listDO + 1]:
            sibling = add_line + list_DO[index_listDO + 1]
        else:
            sibling = "NULL"
    except IndexError:
        sibling = "NULL"
    first_child = "NULL"
    for i in range(len(list_DA1)):
        if list_DO[index_listDO] in list_DA1[i]:
            index_listDA1 = i
            first_child = add_line + list_DA1[i]
            break
    index_listDO += 1
    DataObject(full_name, name, parent, sibling, first_child)

    if index_listDO >= len(list_DO):
        out_DO = 1
    DA1_handler(list_DA1[index_listDA1])


def DA1_handler(DA1):
    global index_listDO
    global index_listDA1
    global index_listDA2
    global out_LD
    global out_LN
    global out_DO
    global out_DA1
    global out_DA2
    global out_DA3
    add_line = "(ModelNode*) &"
    full_name = DA1
    index = [i for i, symb in enumerate(DA1) if symb == "_"]  # определяет позиции "_"
    name = DA1[(index[3] + 1):len(DA1)]
    parent = add_line + DA1[0:index[3]]

    try:
        if list_DO[index_listDO - 1] + "_" in list_DA1[index_listDA1 + 1]:
            sibling = add_line + list_DA1[index_listDA1 + 1]
        else:
            sibling = "NULL"
    except IndexError:
        sibling = "NULL"
    first_child = "NULL"
    if list_DA2:
        for i in range(len(list_DA2)):
            if list_DA1[index_listDA1] + "_" in list_DA2[i]:
                index_listDA2 = i
                first_child = add_line + list_DA2[i]
                break
    some_param = some_param_data_attribute2(list_param_DA1[index_listDA1])
    elementCount = "0"
    fc = some_param[0]
    type = some_param[1][0]
    triggerOptions = some_param[1][1]
    mmsValue = "NULL"
    index_listDA1 += 1
    DataAttribute(full_name, name, parent, sibling, first_child, elementCount, fc, type, triggerOptions, mmsValue)

    if index_listDA1 >= len(list_DA1):
        out_DA1 = 1

    if not out_DA2 and first_child != "NULL":
        DA2_handler(list_DA2[index_listDA2])
    elif not out_DA1 and sibling != "NULL":
        DA1_handler(list_DA1[index_listDA1])
    elif not out_DA1 and (list_DO[index_listDO - 1] + "_" in list_DA1[index_listDA1]):
        DA1_handler(list_DA1[index_listDA1])
    elif not out_DO and (list_LN[index_listLN - 1] in list_DO[index_listDO]):
        DO_handler(list_DO[index_listDO])
    elif not out_LN and (list_LD[index_listLD - 1] in list_LN[index_listLN]):
        LN_handler(list_LN[index_listLN])
    elif not out_LD:
        LD_handler(list_LD[index_listLD])
    else:
        print("This is it!!!")


def DA2_handler(DA2):
    global index_listDO
    global index_listDA1
    global index_listDA2
    global index_listDA3
    global out_LD
    global out_LN
    global out_DO
    global out_DA1
    global out_DA2
    global out_DA3
    add_line = "(ModelNode*) &"
    full_name = DA2
    index = [i for i, symb in enumerate(DA2) if symb == "_"]  # определяет позиции "_"
    name = DA2[(index[4] + 1):len(DA2)]
    parent = add_line + DA2[0:index[4]]
    try:
        if list_DA1[index_listDA1 - 1] in list_DA2[index_listDA2 + 1]:
            sibling = add_line + list_DA2[index_listDA2 + 1]
        else:
            sibling = "NULL"
    except IndexError:
        sibling = "NULL"

    first_child = "NULL"
    if list_DA3:
        for i in range(len(list_DA3)):
            if list_DA2[index_listDA2] in list_DA3[i]:
                index_listDA3 = i
                first_child = add_line + list_DA3[i]
                break
    some_param = some_param_data_attribute2(list_param_DA2[index_listDA2])
    elementCount = "0"
    fc = some_param[0]
    type = some_param[1][0]
    triggerOptions = some_param[1][1]
    mmsValue = "NULL"
    index_listDA2 += 1
    DataAttribute(full_name, name, parent, sibling, first_child, elementCount, fc, type, triggerOptions, mmsValue)

    if index_listDA2 == len(list_DA2):
        out_DA2 = 1

    if not out_DA3 and first_child != "NULL":
        DA3_handler(list_DA3[index_listDA3])
    elif not out_DA2 and sibling != "NULL":
        DA2_handler(list_DA2[index_listDA2])
    elif not out_DA2 and (list_DA1[index_listDA1 - 1] in list_DA2[index_listDA2]):
        DA2_handler(list_DA2[index_listDA2])
    elif not out_DA1 and (list_DO[index_listDO - 1] in list_DA1[index_listDA1]):
        DA1_handler(list_DA1[index_listDA1])
    elif not out_DO and (list_LN[index_listLN - 1] in list_DO[index_listDO]):
        DO_handler(list_DO[index_listDO])
    elif not out_LN and (list_LD[index_listLD - 1] in list_LN[index_listLN]):
        LN_handler(list_LN[index_listLN])
    elif not out_LD:
        LD_handler(list_LD[index_listLD])
    else:
        print("This is it!!!")


def DA3_handler(DA3):
    global index_listDO
    global index_listDA1
    global index_listDA2
    global index_listDA3
    global index_listDA4
    global out_LD
    global out_LN
    global out_DO
    global out_DA1
    global out_DA2
    global out_DA3
    global out_DA4
    add_line = "(ModelNode*) &"
    full_name = DA3
    index = [i for i, symb in enumerate(DA3) if symb == "_"]  # определяет позиции "_"
    name = DA3[(index[5] + 1):len(DA3)]
    parent = add_line + DA3[0:index[5]]
    try:
        if list_DA2[index_listDA2 - 1] in list_DA3[index_listDA3 + 1]:
            sibling = add_line + list_DA3[index_listDA3 + 1]
        else:
            sibling = "NULL"
    except IndexError:
        sibling = "NULL"
    first_child = "NULL"
    if list_DA4:
        for i in range(len(list_DA4)):
            if list_DA3[index_listDA3] in list_DA4[i]:
                index_listDA4 = i
                first_child = add_line + list_DA4[i]
                break
    some_param = some_param_data_attribute2(list_param_DA3[index_listDA3])
    elementCount = "0"
    fc = some_param[0]
    type = some_param[1][0]
    triggerOptions = some_param[1][1]
    mmsValue = "NULL"
    index_listDA3 += 1
    DataAttribute(full_name, name, parent, sibling, first_child, elementCount, fc, type, triggerOptions, mmsValue)

    if index_listDA3 == len(list_DA3):
        out_DA3 = 1

    if not out_DA4 and first_child != "NULL":
        DA4_handler(list_DA4[index_listDA4])
    if not out_DA3 and sibling != "NULL":
        DA3_handler(list_DA3[index_listDA3])
    elif not out_DA3 and (list_DA2[index_listDA2 - 1] in list_DA3[index_listDA3]):
        DA3_handler(list_DA3[index_listDA3])
    elif not out_DA2 and (list_DA1[index_listDA1 - 1] in list_DA2[index_listDA2]):
        DA2_handler(list_DA2[index_listDA2])
    elif not out_DA1 and (list_DO[index_listDO - 1] in list_DA1[index_listDA1]):
        DA1_handler(list_DA1[index_listDA1])
    elif not out_DO and (list_LN[index_listLN - 1] in list_DO[index_listDO]):
        DO_handler(list_DO[index_listDO])
    elif not out_LN and (list_LD[index_listLD - 1] in list_LN[index_listLN]):
        LN_handler(list_LN[index_listLN])
    elif not out_LD:
        LD_handler(list_LD[index_listLD])
    else:
        print("This is it!!!")


def DA4_handler(DA4):
    global index_listDO
    global index_listDA1
    global index_listDA2
    global index_listDA3
    global index_listDA4
    global out_LD
    global out_LN
    global out_DO
    global out_DA1
    global out_DA2
    global out_DA3
    global out_DA4

    add_line = "(ModelNode*) &"
    full_name = DA4
    index = [i for i, symb in enumerate(DA4) if symb == "_"]  # определяет позиции "_"
    name = DA4[(index[5] + 1):len(DA4)]
    parent = add_line + DA4[0:index[5]]
    try:
        if list_DA3[index_listDA3 - 1] in list_DA4[index_listDA4 + 1]:
            sibling = add_line + list_DA4[index_listDA4 + 1]
        else:
            sibling = "NULL"
    except IndexError:
        sibling = "NULL"
    first_child = "NULL"
    some_param = some_param_data_attribute2(list_param_DA4[index_listDA4])
    elementCount = "0"
    fc = some_param[0]
    type = some_param[1][0]
    triggerOptions = some_param[1][1]
    mmsValue = "NULL"
    index_listDA4 += 1
    DataAttribute(full_name, name, parent, sibling, first_child, elementCount, fc, type, triggerOptions, mmsValue)

    if index_listDA4 == len(list_DA4):
        out_DA4 = 1

    if out_DA4 and sibling != "NULL":
        DA4_handler(list_DA4[index_listDA4])
    elif not out_DA4 and (list_DA3[index_listDA3 - 1] in list_DA4[index_listDA4]):
        DA4_handler(list_DA4[index_listDA4])
    elif not out_DA3 and (list_DA2[index_listDA2 - 1] in list_DA3[index_listDA3]):
        DA3_handler(list_DA3[index_listDA3])
    elif not out_DA2 and (list_DA1[index_listDA1 - 1] in list_DA2[index_listDA2]):
        DA2_handler(list_DA2[index_listDA2])
    elif not out_DA1 and (list_DO[index_listDO - 1] in list_DA1[index_listDA1]):
        DA1_handler(list_DA1[index_listDA1])
    elif not out_DO and (list_LN[index_listLN - 1] in list_DO[index_listDO]):
        DO_handler(list_DO[index_listDO])
    elif not out_LN and (list_LD[index_listLD - 1] in list_LN[index_listLN]):
        LN_handler(list_LN[index_listLN])
    elif not out_LD:
        LD_handler(list_LD[index_listLD])
    else:
        print("This is it!!!")


def some_param_data_attribute2(name):
    functional_constraint = int(name[1])
    data_type = int(name[2])

    Data_Type = {
        0: "IEC61850_FC_ST",
        1: "IEC61850_FC_MX",
        2: "IEC61850_FC_SP",
        3: "IEC61850_FC_SV",
        4: "IEC61850_FC_CF",
        5: "IEC61850_FC_DC",
        6: "IEC61850_FC_SG",
        7: "IEC61850_FC_SE",
        8: "IEC61850_FC_SR",
        9: "IEC61850_FC_OR",
        10: "IEC61850_FC_BL",
        11: "IEC61850_FC_EX",
        12: "IEC61850_FC_CO",
        13: "IEC61850_FC_US",
        14: "IEC61850_FC_MS",
        15: "IEC61850_FC_RP",
        16: "IEC61850_FC_BR",
        17: "IEC61850_FC_LG",
        18: "IEC61850_FC_GO",
        99: "IEC61850_FC_ALL",
        -1: "IEC61850_FC_NONE"
    }

    Functional_Constraint = {
        0: ["IEC61850_BOOLEAN", "0 + TRG_OPT_DATA_CHANGED"],
        1: ["IEC61850_INT8", "0 + TRG_OPT_DATA_CHANGED"],
        2: ["IEC61850_INT16", "0 + TRG_OPT_DATA_CHANGED"],
        3: ["IEC61850_INT32", "0 + TRG_OPT_DATA_CHANGED"],
        4: ["IEC61850_INT64", "0 + TRG_OPT_DATA_CHANGED"],
        5: ["IEC61850_INT128", "0 + TRG_OPT_DATA_CHANGED"],
        6: ["IEC61850_INT8U", "0 + TRG_OPT_DATA_CHANGED"],
        7: ["IEC61850_INT16U", "0 + TRG_OPT_DATA_CHANGED"],
        8: ["IEC61850_INT24U", "0 + TRG_OPT_DATA_CHANGED"],
        9: ["IEC61850_INT32U", "0 + TRG_OPT_DATA_CHANGED"],
        10: ["IEC61850_FLOAT32", "0 + TRG_OPT_DATA_CHANGED"],
        11: ["IEC61850_FLOAT64", "0 + TRG_OPT_DATA_CHANGED"],
        12: ["IEC61850_ENUMERATED", "0"],
        13: ["IEC61850_OCTET_STRING_64", "0"],
        14: ["IEC61850_OCTET_STRING_6", "0"],
        15: ["IEC61850_OCTET_STRING_8", "0"],
        16: ["IEC61850_VISIBLE_STRING_32", "0"],
        17: ["IEC61850_VISIBLE_STRING_64", "0"],
        18: ["IEC61850_VISIBLE_STRING_65", "0"],
        19: ["IEC61850_VISIBLE_STRING_129", "0"],
        20: ["IEC61850_VISIBLE_STRING_255", "0"],
        21: ["IEC61850_UNICODE_STRING_255", "0"],
        22: ["IEC61850_TIMESTAMP", "0"],
        23: ["IEC61850_QUALITY", "0 + TRG_OPT_QUALITY_CHANGED"],
        24: ["IEC61850_CHECK", "0"],
        25: ["IEC61850_CODEDENUM", "0 + TRG_OPT_DATA_CHANGED"],
        26: ["IEC61850_GENERIC_BITSTRING", "0"],
        27: ["IEC61850_CONSTRUCTED", "0"],
        28: ["IEC61850_ENTRY_TIME", "0"],
        29: ["IEC61850_PHYCOMADDR", "0"],
        30: ["IEC61850_CURRENCY", "0"],
        31: ["IEC61850_OPTFLDS", "0"],
        32: ["IEC61850_TRGOPS", "0"],
    }

    da_iec61850 = [Data_Type.get(data_type, -1), Functional_Constraint.get(functional_constraint, 0)]
    return da_iec61850


def some_param_data_attribute(name):
    stVal_param = ["IEC61850_FC_ST", "IEC61850_ENUMERATED", "0 + TRG_OPT_DATA_CHANGED"]
    q_param = ["IEC61850_FC_ST", "IEC61850_QUALITY", "0 + TRG_OPT_QUALITY_CHANGED"]
    t_param = ["IEC61850_FC_ST", "IEC61850_TIMESTAMP", "0"]
    ctlModel_param = ["IEC61850_FC_CF", "IEC61850_ENUMERATED", "0"]
    vendor_param = ["IEC61850_FC_DC", "IEC61850_VISIBLE_STRING_255", "0"]
    swRev_param = ["IEC61850_FC_DC", "IEC61850_VISIBLE_STRING_255", "0"]
    d_param = ["IEC61850_FC_DC", "IEC61850_VISIBLE_STRING_255", "0"]
    configRev_param = ["IEC61850_FC_DC", "IEC61850_VISIBLE_STRING_255", "0"]
    ldNs_param = ["IEC61850_FC_EX", "IEC61850_VISIBLE_STRING_255", "0"]
    mag_param = ["IEC61850_FC_MX", "IEC61850_CONSTRUCTED", "0 + TRG_OPT_DATA_CHANGED"]
    f_param = ["IEC61850_FC_MX", "IEC61850_FLOAT32", "0 + TRG_OPT_DATA_CHANGED"]
    origin_param = ["IEC61850_FC_ST", "IEC61850_CONSTRUCTED", "0"]
    orCat_param = ["IEC61850_FC_ST", "IEC61850_CONSTRUCTED", "0"]
    orIdent_param = ["IEC61850_FC_ST", "IEC61850_OCTET_STRING_64", "0"]
    Oper_param = ["IEC61850_FC_CO", "IEC61850_CONSTRUCTED", "0"]
    Test_param = ["IEC61850_FC_CO", "IEC61850_BOOLEAN", "0"]
    Check_param = ["IEC61850_FC_CO", "IEC61850_CHECK", "0"]
    ctlVal_param = ["IEC61850_FC_CO", "IEC61850_BOOLEAN", "0"]
    ctlNum_param = ["IEC61850_FC_CO", "IEC61850_INT8U", "0"]
    T_param = ["IEC61850_FC_CO", "IEC61850_TIMESTAMP", "0"]
    dU_param = ["IEC61850_FC_DC", "IEC61850_UNICODE_STRING_255", "0"]
    cVal_param = ["IEC61850_FC_MX", "IEC61850_CONSTRUCTED", "0 + TRG_OPT_DATA_CHANGED + TRG_OPT_DATA_UPDATE"]
    ang_param = ["IEC61850_FC_MX", "IEC61850_CONSTRUCTED", "0 + TRG_OPT_DATA_CHANGED + TRG_OPT_DATA_UPDATE"]
    numHar_param = ["IEC61850_FC_CF", "IEC61850_INT16U", "0 + TRG_OPT_DATA_CHANGED"]
    numCyc_param = ["IEC61850_FC_CF", "IEC61850_INT16U", "0 + TRG_OPT_DATA_CHANGED"]
    evalTm_param = ["IEC61850_FC_CF", "IEC61850_INT16U", "0 + TRG_OPT_DATA_CHANGED"]
    frequency_param = ["IEC61850_FC_CF", "IEC61850_FLOAT32", "0 + TRG_OPT_DATA_CHANGED"]
    maxVal_param = ["IEC61850_FC_CF", "IEC61850_INT32", "0 + TRG_OPT_DATA_CHANGED"]
    minVal_param = ["IEC61850_FC_CF", "IEC61850_INT32", "0 + TRG_OPT_DATA_CHANGED"]
    SBO_param = ["IEC61850_FC_CF", "IEC61850_VISIBLE_STRING_129", "0 + TRG_OPT_DATA_CHANGED"]
    units_param = ["IEC61850_FC_CF", "IEC61850_CONSTRUCTED", "0"]
    setVal_param = ["IEC61850_FC_SP", "IEC61850_CONSTRUCTED", "0"]
    stepSize_param = ["IEC61850_FC_CF", "IEC61850_INT32U", "0 + TRG_OPT_DATA_CHANGED"]
    multiplier_param = ["IEC61850_FC_CF", "IEC61850_ENUMERATED", "0"]
    SIUnit_param = ["IEC61850_FC_CF", "IEC61850_ENUMERATED", "0"]
    diff_param = ["IEC61850_FC_ST", "IEC61850_BOOLEAN", "0//diff"]

    data_attribute = {
        "stVal": stVal_param,
        "q": q_param,
        "t": t_param,
        "ctlModel": ctlModel_param,
        "vendor": vendor_param,
        "swRev": swRev_param,
        "d": d_param,
        "configRev": configRev_param,
        "ldNs": ldNs_param,
        "mag": mag_param,
        "f": f_param,
        "origin": origin_param,
        "orCar": orCat_param,
        "orIdent": orIdent_param,
        "Oper": Oper_param,
        "Test": Test_param,
        "Check": Check_param,
        "ctlVal": ctlVal_param,
        "ctlNum": ctlNum_param,
        "T": T_param,
        "dU": dU_param,
        "cVal": cVal_param,
        "ang": ang_param,
        "numHar": numHar_param,
        "numCyc": numCyc_param,
        "evalTm": evalTm_param,
        "frequency": frequency_param,
        "maxVal": maxVal_param,
        "minVal": minVal_param,
        "SBO": SBO_param,
        "units": units_param,
        "setVal": setVal_param,
        "step": stepSize_param,
        "multiplier": multiplier_param,
        "SiUnit": SIUnit_param
    }
    return data_attribute.get(name, diff_param)


tree_reading2()
LD_handler(list_LD[index_listLD])
