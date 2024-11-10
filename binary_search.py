# program to design a function for binary search using divide and search strategy.

def binarySearch(A, l, h, key):
    if (l == h):
        if (A[l] == key):
            return l
        else:
            return -1 # not found
    else:
        mid = (l+h)//2
        if (A[mid] == key):
            return mid;
        if (A[mid] > key):
            return binarySearch(A, l, mid-1, key)
        else:
            return binarySearch(A, mid+1, h, key)

def main():
    A = [3, 6, 8, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62]
    l = 0
    h = 14
    key = 42
    
    result = binarySearch(A, l, h, key)
    if (result):
        print(f'{key} found at position {result + 1}')
    else:
        print(f'{key} not found')

if __name__ == '__main__':
    main()
