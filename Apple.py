import pickle
from datetime import datetime


with open('arr2.pkl', 'rb') as file:
    test_arr = pickle.load(file)


def get_fixed_point(array):
    for key in range(len(array)):
        if array[key] == key:
            return array[key]
    return False


start = datetime.now()
result = get_fixed_point(test_arr)
finish = datetime.now() - start
print(f'Result func1 => {result}  time: {finish}')
