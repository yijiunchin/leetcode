int maxOperations(char* s) {
    int size = strlen(s);
    int ans = 0;
    int part = 0;
    bool one = true;
    for (int i = size - 1; i >= 0; --i) {
        if (s[i] == '1') {
            one = true;
            ans += part;
            continue;
        }
        if (one && s[i] == '0') {
            one = false;
            ++part;
        }
    }
    return ans;
}
