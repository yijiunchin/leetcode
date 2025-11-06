#include <vector>
#include <stack>
using namespace std;

class UF {
private:
    vector<int> parent;

public:
    explicit UF(int n) : parent(n, -1) {
    }

    int root(const int x) {
        if (parent[x] < 0) return x;
        return parent[x] = root(parent[x]);
    }

    bool unite(int a, int b) {
        a = root(a), b = root(b);
        if (a == b)
            return false;
        if (parent[a] > parent[b])
            swap(a, b);
        parent[a] += parent[b];
        parent[b] = a;
        return true;
    }
};

class Solution {
public:
    static vector<int> processQueries(const int c, const vector<vector<int>>& connections,
                                      const vector<vector<int>>& queries) {
        UF dsu(c + 1);
        for (const auto& connection : connections)
            dsu.unite(connection[0], connection[1]);

        vector<stack<int, vector<int>>> grids(c + 1);
        for (int i = c; i >= 0; --i)
            grids[dsu.root(i)].push(i);

        vector<bool> online(c + 1, true);

        vector<int> ret;
        for (const auto& query : queries) {
            const int station = query[1];
            auto& grid = grids[dsu.root(station)];
            if (query[0] == 1)
                if (online[station])
                    ret.push_back(station);
                else {
                    while (not(grid.empty() or online[grid.top()]))
                        grid.pop();
                    ret.push_back(grid.empty() ? -1 : grid.top());
                }
            else
                online[station] = false;
        }
        return ret;
    }
};
