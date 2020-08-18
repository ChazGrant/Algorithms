package com.company;

import java.util.Arrays;

public class Main {

    public static int sum(int[] arr){
        if (arr.length == 0)
            return 0;
        return arr[0] + sum(Arrays.copyOfRange(arr, 1, arr.length));
    }


    public static void main(String[] args) {
        int[] array = {2,3,4,5,6,7};
        System.out.println(sum(array));

    }
}
