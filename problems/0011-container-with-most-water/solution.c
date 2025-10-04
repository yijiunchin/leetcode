int maxArea(int* height, int heightSize) {
    int max_area = 0, max_height = 0;
    for (int i = 0; i < heightSize - 1; i++) {
        if (max_height >= height[i]) continue;
        for (int j = i + 1; j < heightSize; j++) {
            max_height = fmax(max_height, height[i]);
            int min_height = fmin(height[i], height[j]);
            max_area = fmax(max_area, (j - i) * min_height);
        }
    }
    return max_area;
}
