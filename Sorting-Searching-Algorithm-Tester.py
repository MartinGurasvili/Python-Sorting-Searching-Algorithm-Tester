import random
import time
# sorting algorithms

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

        count+=1
    
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx], arr[i]
    
def quick_sort(arr,low,high):

    if len(arr) == 1:
        return arr
    if low < high:
        i = (low-1)         
        pivot = arr[high]   
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        pi=(i+1)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


# serching algorithms
def linear_search(arr):    
    itemPos = 0
    itemFound = False
    while itemPos < len(array) and itemFound == False:
        if arr[itemPos] == itemWanted:
            itemFound = True
        else:
            itemPos +=1
    if itemFound == True:
        print("item at index ", itemPos)
    else:
        print("item not in list")
        

def binary_search(arr, low, high):
    if high >= low:
  
        mid = (high + low) // 2
        if arr[mid] == itemWanted:
            print("item at index ", mid)
  
        elif arr[mid] > itemWanted:
            return binary_search(arr, low, mid-1)
  
        else:
            return binary_search(arr, mid + 1, high)
  
    else:
        print("item not in list")

        
if __name__ == "__main__":      
    array = []

    itemWanted = 10
    length_of_list = 100000

    # fills an array with random numbers from range specified
    for x in range(length_of_list):
        array.append(random.randint(0,length_of_list))
    start_time = time.time()
    # sorting algorithm
    
    quick_sort(array,0,len(array)-1)
    
    past_time=time.time() - start_time
    
    print("--- %s seconds to sort ---" % (time.time() - start_time))
    # searching algorithm    
    binary_search(array,0,len(array)-1)
    
    print("--- %s seconds to find ---" % ((time.time() - start_time) - past_time))
     
