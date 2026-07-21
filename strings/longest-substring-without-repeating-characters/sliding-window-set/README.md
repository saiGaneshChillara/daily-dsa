# Sliding Window with Set

## Intuition

The optimized brute force approach improves the solution to `O(n²)` by maintaining a set while expanding the substring.

However, it still restarts the search from every possible starting index.

We can eliminate this repeated work using the **Sliding Window** technique.

The idea is to maintain a window `[left, right]` that always contains unique characters.

We use an `unordered_set` to keep track of the characters currently present in the window.

- `right` expands the window by adding new characters.
- If `s[right]` is not present in the set, we add it and continue expanding.
- If `s[right]` is already present, the window contains a duplicate.
- We then move `left` forward and remove characters from the set until the duplicate is removed.

Since both `left` and `right` only move forward, each character is added and removed from the set at most once.

---

## Algorithm

1. Initialize:
   - `left = 0`
   - `right = 0`
   - `maxLength = 0`
   - An empty `unordered_set` named `seen`.

2. While `right` is within the string:
   - If `s[right]` is not present in `seen`:
     - Insert `s[right]` into the set.
     - Update `maxLength`.
     - Move `right` forward.
   - Otherwise:
     - Remove `s[left]` from the set.
     - Move `left` forward.

3. Return `maxLength`.

---

## Dry Run

### Input

```text
s = "abcabcbb"
```

### Initial State

```text
left = 0
right = 0
seen = {}
maxLength = 0
```

---

### Step 1

Character:

```text
s[right] = 'a'
```

`a` is not in the set.

```text
seen = {a}
window = "a"
```

```text
maxLength = 1
right++
```

---

### Step 2

Character:

```text
s[right] = 'b'
```

`b` is not in the set.

```text
seen = {a, b}
window = "ab"
```

```text
maxLength = 2
right++
```

---

### Step 3

Character:

```text
s[right] = 'c'
```

`c` is not in the set.

```text
seen = {a, b, c}
window = "abc"
```

```text
maxLength = 3
right++
```

---

### Step 4

Character:

```text
s[right] = 'a'
```

`a` already exists in the set.

The current window is:

```text
"a b c a"
↑     ↑
left  right
```

Remove `s[left]`, which is `a`:

```text
seen = {b, c}
left++
```

Now the window is:

```text
"b c a"
```

Add the new `a`:

```text
seen = {a, b, c}
right++
```

The window is again valid.

---

### Continue

The same process continues as the window moves through the string.

The longest valid window found is:

```text
"abc"
```

Therefore:

```text
Answer = 3
```

---

## Visual Representation

The sliding window dynamically changes as the pointers move.

For example:

```text
s = "abcabcbb"

[a b c]
 ↑     ↑
left  right
```

When the next character is another `a`:

```text
[a b c a]
```

A duplicate is detected.

Move `left` and remove characters:

```text
[a b c a]
 ↑
remove 'a'
```

The window becomes:

```text
[b c a]
  ↑   ↑
 left right
```

The window is valid again, so we continue expanding.

---

## Why Is This O(n)?

At first glance, there are two loops:

```text
right → moves from 0 to n - 1
left  → also moves from 0 to n - 1
```

However, neither pointer ever moves backward.

Therefore:

- `right` moves at most `n` times.
- `left` moves at most `n` times.

Each character is:

- Inserted into the set at most once.
- Removed from the set at most once.

Therefore, the total number of operations is proportional to `n`.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Both `left` and `right` traverse the string at most once.

---

### Space Complexity

The `unordered_set` stores the characters currently inside the sliding window.

```text
O(min(n, charset))
```

where `charset` is the number of distinct possible characters.

---

## Comparison with Previous Approaches

| Approach | Time | Space | Key Idea |
|---|---:|---:|---|
| Brute Force | O(n³) | O(min(n, charset)) | Generate and validate every substring |
| Optimized Brute Force | O(n²) | O(min(n, charset)) | Maintain set while expanding from each start |
| Sliding Window + Set | O(n) | O(min(n, charset)) | Dynamically maintain a valid window |

---

## Key Takeaway

The major improvement comes from **not restarting the search from every starting index**.

Instead, we maintain one continuously moving window:

```text
[left ........ right]
```

The window always contains unique characters.

When a duplicate is found, we shrink the window from the left until it becomes valid again.

This allows us to solve the problem in:

```text
O(n)
```

time.

---

## Source Code

See `solution.cpp`.