# lab 2: implement quick sort using divide and conquer strategy. 
# time complexity: best case: nlog(n) and worst case: n^2

class QuickSort:
    def partition(self, A, l, h):
        pivot = A[l]
        i = l
        j = h
        while i < j:
            while A[i] <= pivot:
                i += 1
            while A[j] > pivot:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]

        A[l], A[j] = A[j], A[l]
        return j

    def quickSort(self, A, l, h):
        if l < h:
            pivot = self.partition(A, l, h)
            self.quickSort(A, l, pivot)
            self.quickSort(A, pivot+1, h)

def main():
    A = [10, 5, 8, 9, 15, 6, 3, 12, 16]
    l = 0
    h = len(A) - 1
    print(f'Unsorted Array: {A}')
    obj = QuickSort()
    obj.quickSort(A, l, h)
    print(f'Sorted Array: {A}')

if __name__ == '__main__':
    main()
