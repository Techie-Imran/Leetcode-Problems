void moveZeroes(int* nums, int numsSize) {
    int l=0, temp, r;
    for(r=0;r<numsSize;r++){
        if(nums[r] != 0){
            temp = nums[l];
            nums[l] = nums[r];
            nums[r] = temp;
            l++;
        }
    }
}