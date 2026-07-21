#include <algorithm>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    int maxLength = 0;
    int left = 0;

    unordered_map<char, int> lastIndex;

    for (int right = 0; right < s.size(); right++) {
      char current = s[right];

      if (lastIndex.find(current) != lastIndex.end()) {
        left = max(left, lastIndex[current] + 1);
      }

      lastIndex[current] = right;
      maxLength = max(maxLength, right - left + 1);
    }

    return maxLength;
  }
};