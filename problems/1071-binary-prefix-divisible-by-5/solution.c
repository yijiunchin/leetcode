/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* prefixesDivBy5(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    bool *ans = malloc(numsSize * sizeof(bool));
    int num = 0;
    for (int i = 0; i < numsSize; ++i) {
        num = (2 * num + nums[i]) % 5;
        ans[i] = (num == 0);
    }
    return ans;
}

