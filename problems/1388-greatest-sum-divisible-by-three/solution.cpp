class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        int ret = 0;
        int div1[2]{100000000}, div2[2]{100000000};

        for (auto& i: nums) {
            ret += i;
            if (i % 3 == 1) {
                if (div1[0] >= i) {
                    div1[1] = div1[0];
                    div1[0] = i;
                } else if (div1[1] > i) {
                    div1[1] = i;
                }
            } else if (i % 3 == 2) {
                if (div2[0] >= i) {
                    div2[1] = div2[0];
                    div2[0] = i;
                } else if (div2[1] > i) {
                    div2[1] = i;
                }
            }
        }

        if (ret % 3 == 1) {
            return ret - min(div1[0], div2[0] + div2[1]);
        } else if (ret % 3 == 2) {
            return ret - min(div2[0], div1[0] + div1[1]);
        }

        return ret;
    }
};
