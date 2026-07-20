# Optimized Brute Force

## Intuition

In the brute force approach, every possible substring is generated and validated independently.

This leads to a lot of repeated work. For example, while checking substrings starting at the same index, the characters that have already been processed are scanned again and again.

Instead of rebuilding a hash set for every substring, we can maintain a single hash set for each starting index and expand the substring one character at a time.

As soon as a duplicate character is encountered, we stop extending the current substring because any longer substring starting from the same index will also contain that duplicate.

This eliminates the repeated validation step and improves the overall time complexity.

---

## Algorithm

1. Initialize `maxLength` to `0`.
2. Iterate over every possible starting index `left`.
3. Create an empty hash set for the current starting index.
4. Expand the ending index `right` from `left` to the end of the string.
5. For each character:
   - If it already exists in the hash set:
     - Stop expanding this substring.
   - Otherwise:
     - Insert the character into the hash set.
     - Update the maximum length.
6. Return the maximum length.

---

## Dry Run

### Input

```text
s = "abcabcbb"
```

### Iteration 1 (`left = 0`)

```text
{}
↓
a      ✓
{a}

ab     ✓
{a, b}

abc    ✓
{a, b, c}

abca   ✗
Duplicate 'a'
Stop
```

Maximum length so far:

```text
3
```

---

### Iteration 2 (`left = 1`)

```text
{}
↓
b      ✓
{b}

bc     ✓
{b, c}

bca    ✓
{b, c, a}

bcab   ✗
Duplicate 'b'
Stop
```

Maximum length remains:

```text
3
```

---

### Input

```text
s = "bbbbb"
```

For every starting index:

```text
{}
↓
b      ✓
{b}

bb     ✗
Stop
```

Answer:

```text
1
```

---

## Complexity Analysis

### Time Complexity

For every starting index, the ending index expands until a duplicate is found.

```text
Outer Loop : O(n)
Inner Loop : O(n)
```

Overall:

```text
O(n²)
```

---

### Space Complexity

The hash set stores the characters present in the current substring.

```text
O(min(n, charset))
```

where `charset` is the number of distinct possible characters.

---

## Why This Is Better Than Brute Force

### Brute Force

For every substring:

```text
abc
abca
abcab
```

the hash set is rebuilt from scratch.

Time Complexity:

```text
O(n³)
```

---

### Optimized Brute Force

The same hash set is reused while expanding the substring.

Instead of validating every substring independently, we only insert one new character at a time.

Time Complexity:

```text
O(n²)
```

---

## Limitation

Although we avoid repeatedly validating substrings, we still restart the process from every starting index.

For example, after processing:

```text
abc
```

we again process:

```text
bc
```

from scratch.

This repeated work can be eliminated using the **Sliding Window** technique, reducing the time complexity to **O(n)**.

---

## Source Code

See `solution.cpp`.