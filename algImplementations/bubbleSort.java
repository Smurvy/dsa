package algImplementations;

public class bubbleSort {
    public static void main(String[] args){
        
        int[] unsorted = {2,6,3,8,2};
        
        //int[] unsorted = {9,3,10,5,4};

        int[] sorted = sort(unsorted);

        for(int i = 0; i < sorted.length; i++){
            System.out.println(sorted[i]);
        }


    }

    public static int[] sort(int[] arr){
        
        for(int i = 0; i < arr.length;i++){
            for(int j = 0; j < arr.length - 1; j++){
                if(arr[j] > arr[j + 1]){
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
                
            }

        }
        // this loop moves the first value larger than its left value up the list until it finds a value that is larger than it
        
        return arr;
    }
}
