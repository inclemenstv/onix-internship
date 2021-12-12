list = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]
print(list)

################ Задание 1.1 #####################

############### Первый вариант ###################
def sortBySecondElement(value):
    return value[1]

list.sort(key=sortBySecondElement)
print(list)

############### Второй вариант ###################

# def SortByElement(list):
#     list.sort(key=lambda x: x[1])
#     return list
#
# print(SortByElement(list))


################### Задание 1.2 #################


def createDict(list):
    dict = {}
    for i in list:
        new_list = []
        dict[i[1]] = new_list
        for n, j in enumerate(i):
            if n == 1:
                continue
            new_list.append(j)

    return dict


dict = createDict(list)

print(dict)

################### Задание 1.3 #################
for i in dict:
    new_list = dict.get(i)
    new_list.sort(reverse=True)
    dict[i] = new_list

print(dict)

################### Задание 1.4 #################

list = []
for i in dict.values():
    for n in i:
        list.append(n)

x = set(list)
print(x)
################### Задание 1.5 #################


