# include "vector"
#include "iostream"
#include "unordered_map"

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashmap;
        for(int i=0;i<nums.size();i++){
            auto it = hashmap.find(target-nums[i]);
            if(it != hashmap.end()){
                return {it->second, i};
            }
            hashmap[nums[i]]=i;
        }
        return {};
    }
};
