int numSub(char* s) {
    uint64_t ans = 0;
    uint64_t appear = 0;

    for (int i = 0; s[i] != '\0'; ++i) {
        if (s[i] == '0') {
            ans += ((1 + appear) * appear / 2) % 1000000007;
            appear = 0;
        } else {
            ++appear;
        }
    }
    
    ans += ((1 + appear) * appear / 2) % 1000000007;

    return ans;
}
