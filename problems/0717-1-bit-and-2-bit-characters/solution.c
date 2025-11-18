bool isOneBitCharacter(int* bits, int bitsSize) {
    int i = 0;
    while (i < bitsSize - 1) {
        if (bits[i] == 1) {
            i += 2;
            continue;
        }
        ++i;
    }
    if (i == bitsSize) return false;
    return true;
}
