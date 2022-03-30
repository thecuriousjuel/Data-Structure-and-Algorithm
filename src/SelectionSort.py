import random

def selection_sort(thelist):
    length_of_list = len(thelist)

    for i in range(length_of_list):
        smallest_index = i
        for j in range(i+1, length_of_list):
            if thelist[j] < thelist[smallest_index]:
                smallest_index = j
        
        thelist[i], thelist[smallest_index] = thelist[smallest_index], thelist[i]
        # print(thelist)
    return thelist


mylist = []
for i in range(5):
    mylist.append(random.randint(0, 100))

mylist = [22, 17, 86, 54, 99]
print('Original Data -> ', mylist)
print('Sorted Data -> ', selection_sort(mylist))
