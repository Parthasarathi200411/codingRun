public class linearSearch {
    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i; // Return the index of the target element if found
            }
        }
        return -1; // Return -1 if the target element is not found in the array
    }

    public static void main(String[] args) {
        int[] array = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        int target = 56;

        int resultIndex = linearSearch(array, target);
        if (resultIndex != -1) {
            System.out.println("Element " + target + " found at index " + resultIndex);
        } else {
            System.out.println("Element " + target + " not found in the array");
        }
    }
}
