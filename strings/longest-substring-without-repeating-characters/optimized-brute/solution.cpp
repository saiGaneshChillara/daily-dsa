#include <algorithm>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    int maxLength = 0;
    int n = s.length();

    for (int left = 0; left < n; left++) {
      unordered_set<char> seen;

      for (int right = left; right < n; right++) {
        if (seen.find(s[right]) != seen.end()) {
          break;
        }
        seen.insert(s[right]);
        maxLength = max(maxLength, right - left + 1);
      }
    }
    return maxLength;
  }
};