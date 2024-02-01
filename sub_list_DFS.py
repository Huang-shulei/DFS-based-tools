class get_sub_list():
    def __init__(self, raw_list, sub_list_lenth):
        self.raw_list = raw_list
        self.sub_list_lenth = sub_list_lenth
        self.sub_list = []

    def get_number(self, index, lenth):
        if lenth > 1:
            for i in range(index, len(self.raw_list)):
                number = self.raw_list[i]
                self.get_number(i + 1, lenth - 1)
                for j in self.sub_list:
                    if len(j) < lenth:
                        j.insert(0, number)
        else:
            for i in range(index, len(self.raw_list)):
                number = self.raw_list[i]
                self.sub_list.append([number])

    def run(self):
        if self.sub_list_lenth > 1:
            for i in range(0, len(self.raw_list)):
                number = self.raw_list[i]
                self.get_number(i + 1, self.sub_list_lenth - 1)
                for j in self.sub_list:
                    if len(j) < self.sub_list_lenth:
                        j.insert(0, number)
        else:
            for i in self.raw_list:
                self.sub_list.append(i)
        return self.sub_list


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = get_sub_list(input_list, 9).run()
print(len(result))
print(result)
