/* Q. Develop a program to design a class for Concurrent Quick Sort Using
Divide and Conquer Strategies. Also Compute it's time complexity */

class QuickSort {
    void Quicksort(int arr[], int lo, int hi) {
        if (lo >= hi) return;
        int pivot_index = partition(arr, lo, hi);
        Quicksort(arr, lo, pivot_index - 1);
        Quicksort(arr, pivot_index + 1, hi);
    }

    int partition(int arr[], int lo, int hi) {
        int i = lo;
        int j = hi + 1;
        int pivot = arr[lo];
        while (true)
        {
            while(less(arr[++i], pivot)) {
                if (i == hi) break;
            }

            while(less(pivot, arr[--j])) {
                if (j == lo) break;
            }

            if (i >= j) break;

            exch(arr, i, j);
        }
        exch(arr, lo, j);
        return j;
    }

    boolean less(int a, int b) {
        return a < b;
    }

    void exch(int arr[], int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    void show(int arr[]) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}

public class Quick {
    public static void main(String[] args) {
        QuickSort obj = new QuickSort();
        int arr[] = {40, 30, 10, 90, 80, 50};
        obj.Quicksort(arr, 0, 6 - 1);
        obj.show(arr);
    }
}