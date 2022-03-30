import this


def insertion_sort(thislist):
    length_of_list = len(thislist)
    for i in range(length_of_list):
        for j in range(i+1, length_of_list):
            if thislist[j]



mylist = [22, 17, 86, 54, 99]
print('Original Data -> ', mylist)
print('Sorted Data -> ', insertion_sort(mylist))

