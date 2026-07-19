# Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the **length of the longest substring** without repeating characters.

A **substring** is a contiguous sequence of characters within a string.

---

## Examples

### Example 1

**Input**

```text
s = "abcabcbb"
```

**Output**

```text
3
```

**Explanation**

The longest substring without repeating characters is:

```text
"abc"
```

Its length is **3**.

Other valid substrings of the same length include:

```text
"bca"
"cab"
```

---

### Example 2

**Input**

```text
s = "bbbbb"
```

**Output**

```text
1
```

**Explanation**

Every substring longer than one character contains duplicate `'b'`.

The longest valid substring is:

```text
"b"
```

---

### Example 3

**Input**

```text
s = "pwwkew"
```

**Output**

```text
3
```

**Explanation**

One longest substring without repeating characters is:

```text
"wke"
```

Its length is **3**.

> **Note:** `"pwke"` is **not** a valid answer because it is a **subsequence**, not a **substring**.

---

## Constraints

- `0 <= s.length <= 5 × 10⁴`
- `s` consists of English letters, digits, symbols, and spaces.

---

## Key Observations

- The answer requires the **length** of the longest valid substring, not the substring itself.
- A substring must consist of **contiguous** characters.
- Duplicate characters invalidate the current substring.
- We need to efficiently determine whether a character has already appeared in the current substring.
- As the input size grows, repeatedly checking every substring becomes inefficient, motivating progressively better approaches.

---

## Approaches

- Brute Force
- Optimized Brute Force
- Optimal (Sliding Window)

---

## Related Topics

- Strings
- Hashing
- Sliding Window
- Two Pointers

---

## Difficulty

**Medium**