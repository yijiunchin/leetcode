int strStr(char* haystack, char* needle) {
    char *p = strstr(haystack, needle);
    return p == NULL ? -1 : p - haystack;
}
