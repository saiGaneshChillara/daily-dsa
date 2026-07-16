#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> index_map;

    int n = nums.size();

    for (int i = 0; i < n; i++) {
      int required = target - nums[i];
      auto it = index_map.find(required);
      if (it != index_map.end()) {
        return {it->second, i};
      }
      index_map[nums[i]] = i;
    }
    return {};
  }
};