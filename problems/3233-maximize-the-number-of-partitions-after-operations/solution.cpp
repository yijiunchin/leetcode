struct CharacterCounter {
private:
    array<int, 26> count;

public:
    CharacterCounter() : count{0} {}
    int distinct() const {
        int result = 0;
        for (int c : count)
            if (c)
                result += 1;
        return result;
    }
    int& operator[](char chr) { return count[chr - 'a']; }
    int at(const char chr) const { return count[chr - 'a']; }
    CharacterCounter& operator+=(const CharacterCounter& rhs) {
        for (char chr = 'a'; chr <= 'z'; ++chr)
            count[chr - 'a'] += rhs.at(chr);
        return *this;
    }
    CharacterCounter& operator-=(const CharacterCounter& rhs) {
        for (char chr = 'a'; chr <= 'z'; ++chr)
            count[chr - 'a'] -= rhs.at(chr);
        return *this;
    }
    CharacterCounter operator-(const CharacterCounter& rhs) const {
        CharacterCounter result = *this;
        for (char chr = 'a'; chr <= 'z'; ++chr)
            result[chr] -= rhs.at(chr);
        return result;
    }
};
class Solution {
public:
    int maxPartitionsAfterOperations(string s, int k) {
        int n = s.size();
        vector<CharacterCounter> prefix(1);
        for (int i = 0; i < n; ++i) {
            prefix.push_back(prefix.back());
            prefix.back()[s[i]] += 1;
        }
        auto distinct = [&prefix](int start, int end) {
            int result = 0;
            for (char c = 'a'; c <= 'z'; ++c)
                if (prefix[end + 1][c] - prefix[start][c])
                    result += 1;
            return result;
        };
        auto exsit = [&prefix](int start, int end, char c) {
            return prefix[end + 1][c] - prefix[start][c];
        };

        vector<vector<int>> parents(n + 1);
        vector<int> next(n);
        auto find_next = [&prefix, n, k, &s](int start, int modify_index,
                                             char modify_char) {
            int left = start + 1, right = n - 1;
            while (left <= right) {
                int mid = (left + right) / 2;

                CharacterCounter counter = prefix[mid + 1] - prefix[start];
                if (start <= modify_index and mid >= modify_index) {
                    counter[s[modify_index]] -= 1;
                    counter[modify_char] += 1;
                }
                if (counter.distinct() <= k)
                    left = mid + 1;
                else
                    right = mid - 1;
            }
            return left;
        };

        for (int i = 0; i < n; i++) {
            int left = find_next(i, INT32_MIN, 0);
            parents[left].push_back(i);
            next[i] = left;
        }
        vector<int> dp(n + 1, 0);
        for (int i = n; i > 0; --i) {
            for (int parent : parents[i])
                dp[parent] = max(dp[parent], dp[i] + 1);
        }

        vector<int> split_points;
        for (int i = 0;; i = next[i]) {
            split_points.push_back(i);
            if (i == n)
                break;
        }

        int result = dp[0];
        for (int mid = 0; mid < n; ++mid) {
            auto iter =
                upper_bound(split_points.begin(), split_points.end(), mid);
            int left = *(iter - 1);
            for (char change_to = 'a'; change_to <= 'z'; ++change_to) {
                if (s[mid] == change_to or exsit(left, mid - 1, change_to))
                    continue;
                int next_node = find_next(left, mid, change_to);
                if (next_node == mid)
                    result =
                        max(result,
                            static_cast<int>(iter - split_points.begin()) + 1 +
                                dp[find_next(next_node, mid, change_to)]);
                else
                    result = max(result,
                                 static_cast<int>(iter - split_points.begin()) +
                                     dp[next_node]);
            }
        }
        return result;
    }
};
