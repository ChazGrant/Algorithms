package com.company;


public class Main {

    public static int bn(int[] arr, int item){
        int low = 0;
        int high = arr.length - 1;
        int mid,guess;

        while (low <= high) {
            mid = (low + high) / 2;
            guess = arr[mid];
            if (guess == item) {
                return mid;
            }
            else if (guess > item)
                high = mid - 1;
            else
                low = mid + 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {1,5,6,7,9,2};
        System.out.println(bn(arr,5));
    }
}
