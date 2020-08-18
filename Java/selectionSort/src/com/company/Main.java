package com.company;

public class Main {

    public static void sort(int[] array){
        for (int i = 0; i < array.length; i++){
            int min = array[i];
            int min_i = i;

            for (int j = i + 1; j < array.length; j++){
                if (array[j] < min){
                    min = array[j];
                    min_i = j;
                }
            }
            if (i != min_i){
                int tmp = array[i];
                array[i] = array[min_i];
                array[min_i] = tmp;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {5,1,4,8,5,4,2,1,9};
        sort(arr);
        for(int i:arr){
            System.out.print(i + " ");
        }
    }
}
