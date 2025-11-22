int minimumOperations(int* nums, int numsSize) {
    int sums = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] % 3 != 0) sums++;
    }
    return sums;
}
