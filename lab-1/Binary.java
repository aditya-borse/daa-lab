/* Q. Develop a program to design a function for Binary Search using Divide 
and Conquer Strategies. Also compute it's time complexity. */

import java.io.FileReader;
import java.io.FileWriter;
import java.util.Scanner;
import java.util.Vector;

class BinarySearch {
    int recursiveBinarySearch(Vector <Integer> arr, int l, int h, int key) {
        if (h < l) {
            return -1;
        }

        int mid = (l + h) / 2;

        if (key > arr.get(mid)) {
            return recursiveBinarySearch(arr, mid + 1, h, key);
        } else if (key < arr.get(mid)) {
            return recursiveBinarySearch(arr, l, mid - 1, key);
        } else {
            return mid + 1;
        }
    }

    int iterativeBinary(Vector <Integer> arr, int l, int h, int key) {
        while (h >= l) {
            int mid = (l + h) / 2;
            if (key > arr.get(mid)) {
                l = mid + 1;
            } else if (key < arr.get(mid)) {
                h = mid - 1;
            } else {
                return mid + 1;
            }
        }
        return -1;
    }
}

public class Binary {
    public static void main(String[] args) throws Exception {
        FileReader fr = new FileReader("input.txt");
        Scanner sc = new Scanner(fr);
        Vector<Integer> arr = new Vector<>();
        int key = 0;
        if (sc.hasNextLine()) {
            String line = sc.nextLine();
            String[] parts = line.split(" ");
            for (int i = 0; i < parts.length - 1; i++) {
                arr.add(Integer.parseInt(parts[i]));
            }
            key = Integer.parseInt(parts[parts.length - 1]);
        }
        fr.close();
        sc.close();
        BinarySearch bs = new BinarySearch();
        int recursive = bs.recursiveBinarySearch(arr, 0, arr.size() - 1, key);
        int iterative = bs.iterativeBinary(arr, 0, arr.size() - 1, key);
        FileWriter fw = new FileWriter("output.txt");
        fw.write("-1 means element not found\n");
        fw.write("Recursive approach: " + recursive + "\n");
        fw.write("Iterative approach: " + iterative + "\n");
        fw.close();
    }
}