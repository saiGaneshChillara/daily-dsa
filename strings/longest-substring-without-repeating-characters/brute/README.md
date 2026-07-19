# Brute Force

## Intuition

To find the longest substring without repeating characters, we can examine every possible substring and check whether it contains only unique characters.

For every starting index, we try every possible ending index and validate the resulting substring.

Among all valid substrings, we keep track of the maximum length encountered.

Although this approach is straightforward, it performs a large amount of repeated work because many overlapping substrings are checked multiple times.

---

## Algorithm

1. Generate all possible substrings using two nested loops.
2. For each substring:
   - Check whether it contains duplicate characters.
   - If it does not contain duplicates:
     - Update the maximum length.
3. Return the maximum length found.

---

## Dry Run

### Input

```text
s = "abcabcbb"
```

Generated substrings:

```text
"a"      ✓
"ab"     ✓
"abc"    ✓
"abca"   ✗

"b"      ✓
"bc"     ✓
"bca"    ✓
"bcab"   ✗

"c"      ✓
"ca"     ✓
"cab"    ✓
"cabc"   ✗
...
```

Longest valid substrings:

```text
"abc"
"bca"
"cab"
```

Length:

```text
3
```

---

### Another Example

```text
s = "bbbbb"
```

Substrings:

```text
"b"      ✓
"bb"     ✗
"bbb"    ✗
"bbbb"   ✗
"bbbbb"  ✗
```

Longest valid substring:

```text
"b"
```

Length:

```text
1
```

---

## Complexity Analysis

### Time Complexity

There are:

```text
O(n²)
```

possible substrings.

For each substring, we validate uniqueness by scanning its characters:

```text
O(n)
```

Therefore:

```text
Time Complexity = O(n³)
```

---

### Space Complexity

A hash set is used during validation.

In the worst case:

```text
Space Complexity = O(min(n, charset))
```

where `charset` represents the number of distinct possible characters.

---

## Why This Approach Is Inefficient

Many substrings overlap.

For example:

```text
"abc"
"abca"
"abcab"
```

Each validation repeatedly scans characters that were already checked in previous substrings.

This repeated work causes the cubic time complexity.

---

## Key Observation

The expensive part is repeatedly rechecking characters while validating substrings.

If we can avoid rebuilding the set from scratch for every substring, we can improve the solution from:

```text
O(n³)
```

to:

```text
O(n²)
```

which leads to the Optimized Brute Force approach.

---

## Source Code

See `solution.cpp`.