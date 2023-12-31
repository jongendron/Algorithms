
def insertion_sort(a: list, n: int, increasing: bool=True) -> None:
    """Insertion sort: sorts array `a` in either increasing or decreasing monotonic order."""
    
    for i in range(1,n):
        key = a[i]  # creates copy of a[i] and saves to variable key (rather than a pointer)
        # Insert a[i] into the sorted subarray a[0:i-1]
        j = i - 1
        if increasing:
            while j > -1 and a[j] > key:
                a[j+1] = a[j]
                j -= 1
        else:
            while j > -1 and a[j] < key:
                a[j+1] = a[j]
                j -= 1
        a[j+1] = key

a1 = [5,1,4,2,3]
print(a1)
insertion_sort(a1,len(a1))
print(a1)
print()

a1 = [5,1,4,2,3]
print(a1)
insertion_sort(a1,len(a1),False)
print(a1)

