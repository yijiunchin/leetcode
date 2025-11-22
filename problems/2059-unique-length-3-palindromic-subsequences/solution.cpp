class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int ans = 0;
      
        for (char c = 'a'; c <= 'z'; ++c) {
            uint32_t first_index = s.find_first_of(c);
            if (first_index == string::npos) continue;
            uint32_t last_index = s.find_last_of(c);
            if (first_index == last_index) continue;
          
            uint32_t appear = 0;
            for (uint32_t i = first_index + 1; i < last_index; ++i) {
                uint8_t c_index = s[i] - 'a';
                if ((appear & (1 << c_index)) == 0) {
                    appear |= (1 << c_index);
                    ++ans;
                }
            }
        }
      
        return ans;
    }
};
