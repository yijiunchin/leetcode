int numWaterBottles(int numBottles, int numExchange) {
    int max_bottles = numBottles;
    while (numBottles / numExchange >= 1) {
        max_bottles += (numBottles / numExchange);
        numBottles = numBottles / numExchange + numBottles % numExchange;
    }
    return max_bottles;
}

