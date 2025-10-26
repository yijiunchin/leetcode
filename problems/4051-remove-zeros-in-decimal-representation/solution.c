long long removeZeros(long long n) {
    int digit, i = 0;
    long long ans = 0;
    while (n > 0) {
        digit = n % 10;
        if (digit == 0) {
            n /= 10;
            continue;
        }
        ans += digit * pow(10, i);
        n /= 10;
        i++;
    }
    return ans;
}
