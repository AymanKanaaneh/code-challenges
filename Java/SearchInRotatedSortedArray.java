//https://leetcode.com/problems/search-in-rotated-sorted-array/

//Time Complexity O(log(n))

class SearchInRotatedSortedArray {
    public int search(int[] nums, int target) {

        int start = 0;
        int end = nums.length-1;
        int pivot = getPivotIndex(nums, start, end);
        return Math.max(binarySearch(nums, target, start, pivot), binarySearch(nums, target, pivot+1, end));
    }

    public int getPivotIndex(int[] nums, int start, int end) {

        if (start >= end) {
            return start;
        }

        int mid = start + (end - start) / 2;

        if (mid < end && nums[mid] > nums[mid + 1]) {
            return mid;
        }

        if (nums[mid] > nums[end]) {
            return getPivotIndex(nums, mid + 1, end);
        }
        return getPivotIndex(nums, start, mid);
    }


    public int binarySearch(int[] nums, int target, int start, int end){
        int mid = start + (end - start) / 2;

        if(start > end) {
            return -1;
        }

        if(nums[mid] > target){
            return binarySearch(nums, target, start, mid-1);
        }else if(nums[mid] < target){
            return binarySearch(nums, target, mid+1, end);
        }else {
            return mid;
        }
    }
}