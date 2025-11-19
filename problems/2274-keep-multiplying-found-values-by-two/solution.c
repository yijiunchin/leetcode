int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int findFinalValue(int* nums, int numsSize, int original) {
    qsort(nums, numsSize, sizeof(*nums), cmp);
    
    int ret = original;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == ret) {
            ret = nums[i] * 2;
        }
    }
    return ret;
}
