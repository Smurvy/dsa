package algImplementations;

public class bubbleSort {
    public static void main(String[] args){
        int[] unsorted = {};

        int[] sorted = sort(unsorted);

        for(int i = 0; i < sorted.length; i++){
            System.out.println(sorted[i]);
        }


    }

    public static int[] sort(int[] arr){
    
        for(int i = 0; i < arr.length; i++){
        
            for(int j = i;j < arr.length;j++){
                if(j != arr.length - 1 && arr[j] > arr [j + 1]){
                    int temp = arr[j];

                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                } 
            }
        }
        return arr;
    }
}
