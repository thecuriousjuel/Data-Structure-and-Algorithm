def insertion_sort(thislist):
    length_of_list = len(thislist)
    for i in range(length_of_list-1):
        
        for j in range(i, 0, -1):
            print(f'{thislist[i]} < {thislist[j]} -> {thislist[i] < thislist[j]}')
            # if thislist[index]  < thislist[j]:
            #     continue
            

            # temp = thislist[j]
            # thislist[j] = thislist[index] 
            # for k in range(j+1, length_of_list-1):
            #     thislist[k] = thislist[k+1]
        # print(thislist)
    return thislist




mylist = [4,3,2,10,12,1,5,6]
print('Original Data -> ', mylist)
print('Sorted Data -> ', insertion_sort(mylist))

