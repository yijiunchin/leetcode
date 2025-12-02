int compare(const void *a, const void *b) {
    long long int_a = *(const int *)a;
    long long int_b = *(const int *)b;
    if (int_a < int_b) return -1;
    if (int_a > int_b) return 1;
    return 0;
}

int countTrapezoids(int** points, int pointsSize, int* pointsColSize) {
    if (pointsSize < 4) return 0;

    int *y_coords = (int *)malloc(pointsSize * sizeof(int));
    if (!y_coords) return 0;

    for (int i = 0; i < pointsSize; i++) {
        y_coords[i] = points[i][1];
    }

    qsort(y_coords, pointsSize, sizeof(int), compare);

    long long mod = 1e9 + 7;
    long long ans = 0;
    long long sum_segments = 0;
    
    int i = 0;
    while (i < pointsSize) {
        int current_y = y_coords[i];
        long long count = 0;

        while (i < pointsSize && y_coords[i] == current_y) {
            count++;
            i++;
        }

        if (count < 2) continue;

        long long current_segments = (count * (count - 1) / 2) % mod;
        ans = (ans + (current_segments * sum_segments) % mod) % mod;
        sum_segments = (sum_segments + current_segments) % mod;
    }

    free(y_coords);
    return (int)ans;
}

