import os
import pickle

list = []
list1 = []

def get_sub_dir_path(parent_name_path):
        sub_dir_names = os.listdir(parent_name_path)
        sub_dir_path_list = []
        for i in sub_dir_names:
            sub_dir_path = os.path.join(parent_name_path, i)
            sub_dir_path_list.append(sub_dir_path)
        return sub_dir_path_list

def try_function(dict_path):
        try:
            datanames1 = get_sub_dir_path(dict_path)
            for i in datanames1:
                datanames2 = try_function(i)
                list.append(datanames2)
        except NotADirectoryError:
            return dict_path

def search_all_file_path(self,dict_name):
        a = try_function(dict_name)
        for i in list:
            if i != None:
                list1.append(i)



search_all_file_path("/home/ubuntu/data0/hsl/1000/input")

for i in list1:
    with open(i, 'rb') as f:
        npy = pickle.load(f)
    label = os.path.split(i)[1]
    
