sub_list = []

def get_number(index, raw_list, generation):
    if generation > 1:
        for i in range(index, len(raw_list)):
            number = raw_list[i]
            get_number(i + 1, raw_list, generation - 1)
            for j in sub_list:
                if len(j) < generation:
                    j.insert(0, number)
    else:
        for i in range(index, len(raw_list)):
            number = raw_list[i]
            sub_list.append([number])

def get_sub_list(raw_list, generation):
    for i in range(0, len(raw_list)):
        number = raw_list[i]
        get_number(i + 1, raw_list, generation-1)
        for j in sub_list:
            if len(j) < generation:
                j.insert(0, number)

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = get_sub_list(input_list,6)
print(len(sub_list))
print(sub_list)
