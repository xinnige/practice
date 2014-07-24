#include "stdio.h"
#include "stdlib.h"
#include <vector>
using namespace std;

class Solution{
public:
    int numTrees(int n){
        vector<int>results;
        results.push_back(1);
        results.push_back(1);
        for (int previous=2; previous<=n; previous++){
            int current = 0;
            for (int i=1; i<=previous; i++){
                current += results[i-1]*results[previous-i];
            }
            results.push_back(current);
        }
        return results[n];
    }
};

int main()
{
    Solution sol;
    for(int i=0;i<5;i++){
        int result = sol.numTrees(i);
        printf("%d",result); 
    }
}
