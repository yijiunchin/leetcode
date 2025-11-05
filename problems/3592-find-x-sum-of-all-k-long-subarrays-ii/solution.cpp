class Solution {
public:
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        using FreqValuePair = pair<int, int>; // {frequency, value}

        set<FreqValuePair> topX, remaining;
        long long currentSum = 0;
        unordered_map<int, int>
            frequency; // Maps value to its frequency in current window

        // Helper function to add an element to the appropriate set after its
        // frequency changes
        auto addToSets = [&](int value) {
            if (frequency[value] == 0) {
                return; // Element not in window, nothing to add
            }

            FreqValuePair element = {frequency[value], value};

            if (!topX.empty() && element > *topX.begin()) {
                currentSum += 1LL * element.first * element.second;
                topX.insert(element);
            } else {
                remaining.insert(element);
            }
        };

        auto removeFromSets = [&](int value) {
            if (frequency[value] == 0) {
                return;
            }

            FreqValuePair element = {frequency[value], value};

            auto it = topX.find(element);
            if (it != topX.end()) {
                currentSum -= 1LL * element.first * element.second;
                topX.erase(it);
            } else {
                remaining.erase(element);
            }
        };

        vector<long long> result;

        for (int i = 0; i < nums.size(); ++i) {
            removeFromSets(nums[i]); // Remove old frequency entry
            ++frequency[nums[i]];    // Update frequency
            addToSets(nums[i]);      // Add new frequency entry

            int windowStart = i - k + 1;
            if (windowStart < 0) {
                continue; // Window not yet complete
            }

            while (!remaining.empty() && topX.size() < x) {
                FreqValuePair best = *remaining.rbegin();
                currentSum += 1LL * best.first * best.second;
                remaining.erase(best);
                topX.insert(best);
            }

            while (topX.size() > x) {
                FreqValuePair worst = *topX.begin(); // Get worst from topX
                currentSum -= 1LL * worst.first * worst.second;
                topX.erase(worst);
                remaining.insert(worst);
            }

            result.push_back(currentSum);

            removeFromSets(nums[windowStart]); // Remove old frequency entry
            --frequency[nums[windowStart]];    // Update frequency
            addToSets(nums[windowStart]); // Add new frequency entry (or nothing
                                          // if freq becomes 0)
        }

        return result;
    }
};
