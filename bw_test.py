

def bubble_sort(list):
    for i in range(0,len(list)-1): 
        for j in range(0,len(list)-1-i): 
            if list[j] < list[j+1]: 
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp


list = ['A','B','C','Y','Y','O','a','s','f','s','w']
bubble_sort(list)
print(list)