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
      for (int right = left; right < n; right++) {
        if (isValid(left, right, s)) {
          maxLength = max(maxLength, right - left + 1);
        }
      }
    }
    return maxLength;
  }
private:
  bool isValid(int left, int right, const string& s) {
    unordered_set<char> seen;

    for (int i = left; i <= right; i++) {
      if (seen.find(s[i]) != seen.end()) {
        return false;
      }
      seen.insert(s[i]);
    }
    return true;
  }
};