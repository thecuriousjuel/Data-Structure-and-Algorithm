import random

# def bubble_sort(the_list):
#     for i in range(len(the_list)):
#         for j in range(len(the_list)-i-1):
#             if the_list[j] > the_list[i]:
#                 the_list[i], the_list[j] = the_list[j], the_list[i] 

#     return the_list


def bubble_sort(A):
    swapped = 1
    for passnum in range(len(A)-1, 0, -1):
        if swapped == 0:
            return
        
        for i in range(passnum):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swapped = 1

    return A


mylist = []
for i in range(5):
    mylist.append(random.randint(0, 100))

mylist = [1,2,3,4]

print("The original list -> ", mylist)
print("The changed list -> ", bubble_sort(mylist))

