int minCost(char* colors, int* neededTime, int neededTimeSize) {
    char last = *colors;
    int max = *neededTime;
    int ans = 0;
    for (int i = 1; i < neededTimeSize; ++i) {
        if (colors[i] == last) {
            if (max > neededTime[i]) {
                ans += neededTime[i];
            } else {
                ans += max;
                max = neededTime[i];
            }
        } else {
            max = neededTime[i];
            last = colors[i];
        }
    }
    
    return ans;
}
