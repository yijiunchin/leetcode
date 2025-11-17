bool kLengthApart(int* nums, int numsSize, int k) {
    int last_index = -k - 1;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) {
            if (i - last_index <= k) return false;
            last_index = i;
        }
    }
    return true;
}
