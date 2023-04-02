choice=1
while(choice==1 or choice==2 or choice==3):
    choice=int(input('''
    1.Quick Sort
    2.Merge Sort
    3. exit
    '''))

#Quick sort 
    if(choice==1):

        arr = list(map(int, input("Enter the array elements: ").split()))

        def quick_sort(arr):
            n = len(arr)
            if n <= 1:
                return arr
            pivot = arr[n // 2]
            L = [x for x in arr if x < pivot]
            M = [x for x in arr if x == pivot]
            R = [x for x in arr if x > pivot]
            return quick_sort(L) + M + quick_sort(R)

        if arr == sorted(arr):
            print("--------------------------------------------------------------------")
            print("Sorted Array:", arr)
            print("--------------------------------------------------------------------")
            print("Best Case: O(nlogn)")
            print("--------------------------------------------------------------------")

        elif arr == sorted(arr, reverse=True):
            print("--------------------------------------------------------------------")
            print("Sorted Array:", arr)
            print("--------------------------------------------------------------------")
            print("Worst Case: O(n^2)")
            print("--------------------------------------------------------------------")
            
        else:
            sorted_arr = quick_sort(arr)
            print("--------------------------------------------------------------------")
            print("Sorted Array:", sorted_arr)
            print("--------------------------------------------------------------------")
            print("Average Case: O(nlogn)")
            print("--------------------------------------------------------------------")
            
#Merge Sort
    elif(choice==2):
        def mergeSort(array):
            if l(array) > 1:
                r = l(array)//2
                L = array[:r]
                M = array[r:]
                mergeSort(L)
                mergeSort(M)

                p = q = t = 0
                while p < l(L) and q < l(M):
                    if L[p] < M[q]:
                        array[k] = L[p]
                        p += 1
                    else:
                        array[k] = M[q]
                        q += 1
                        t += 1

                while p < l(L):
                    array[k] = L[p]
                    p += 1
                    t += 1

                while j < l(M):
                    array[t] = M[q]
                    q += 1
                    t += 1
                    
        def Print(array):
            for p in range(l(array)):
                print(array[p], end=" ")
            print()
            
        array = list(map(int, input("Enter the array elements: ").split()))
        if array == sorted(array):
            print("--------------------------------------------------------------------")
            print("Sorted Array:", array)
            print("--------------------------------------------------------------------")
            print("Best Case: O(nlogn)")
            print("--------------------------------------------------------------------")
            
        elif array == sorted(array, reverse=True):
            print("--------------------------------------------------------------------")
            print("Sorted Array:", array)
            print("--------------------------------------------------------------------")
            print("Worst Case: O(nlogn)")
            print("--------------------------------------------------------------------")

#end the program
    elif(choice ==3):
        break
