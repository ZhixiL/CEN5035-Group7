import os
import itertools as it

path = "./CustomInputData"
os.chdir(path)

for file in os.listdir():
    input = dict()
    file_path = f"/Users/yukikentybonita/Desktop/FSU/CEN5035/CEN5035-Group7/CustomInputData/{file}"
    with open(file_path, 'r') as f:
        counter = 0
        for key,group in it.groupby(f,lambda line: line.startswith('-----PARTBREAKER-----')):
            if not key:
                group = list(group)
                group_str = ''.join(map(str,group)).strip()
                
                if counter == 0:
                    input['question'] = group_str
                elif counter == 1:
                    input['input_output'] = group_str
                elif counter == 2:
                    input['difficulty'] = group_str
                elif counter == 3:
                    input['acceptance_rate'] = group_str
                elif counter == 4:
                    input['constraints'] = group_str
                elif counter == 5:
                    input['initial_code'] = group_str
                counter += 1