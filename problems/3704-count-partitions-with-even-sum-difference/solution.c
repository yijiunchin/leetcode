int countPartitions(int* nums, int numsSize) {
    int sum = 0;
    for (int i = 0; i < numsSize; ++i) {
        sum += nums[i];
    }
    if (sum % 2) return 0;
    return --numsSize;
}
