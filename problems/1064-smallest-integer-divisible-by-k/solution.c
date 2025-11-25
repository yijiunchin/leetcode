int smallestRepunitDivByK(int k) {
    int n = 0;
    for (int i = 1; i <= k; ++i) {
        n = (10 * n + 1) % k;
        if (n == 0) return i;
    }
    return -1;
}
