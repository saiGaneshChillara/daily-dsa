# Brute Force

## Intuition

To find two numbers whose sum equals the target, the most straightforward approach is to check **every possible pair** in the array.

For each element, compare it with every element that comes after it. If the sum of the pair equals the target, return their indices.

Since the problem guarantees **exactly one valid solution**, we can return immediately once the correct pair is found.

---

## Algorithm

1. Iterate through the array using index `i`.
2. For every `i`, iterate through the remaining elements using index `j = i + 1`.
3. Check whether `nums[i] + nums[j] == target`.
4. If the condition is true, return `{i, j}`.
5. Since the problem guarantees one solution, the algorithm will always return a valid answer.

---

## Dry Run

### Input

```text
nums = [2, 7, 11, 15]
target = 9
```

| i | j | nums[i] | nums[j] | Sum | Action |
|---|---|---------|---------|-----|--------|
| 0 | 1 | 2 | 7 | 9 | ✅ Return {0, 1} |

The algorithm finds the required pair immediately and terminates.

---

### Another Example

```text
nums = [3, 2, 4]
target = 6
```

| i | j | Pair | Sum | Action |
|---|---|------|-----|--------|
| 0 | 1 | (3,2) | 5 | Continue |
| 0 | 2 | (3,4) | 7 | Continue |
| 1 | 2 | (2,4) | 6 | ✅ Return {1,2} |

---

## Complexity Analysis

### Time Complexity

**O(n²)**

In the worst case, every possible pair is checked.

Total pairs:

```text
(n − 1) + (n − 2) + ... + 1
= n(n − 1)/2
```

Therefore,

```text
Time Complexity = O(n²)
```

---

### Space Complexity

**O(1)**

The algorithm uses only a few variables (`i` and `j`) irrespective of the input size.

The returned vector is not counted as extra space.

---

## Why This Approach Is Inefficient

Many comparisons are repeated unnecessarily.

For example, while checking `nums[i]`, we repeatedly search the remaining part of the array even though we've already seen some elements.

This repeated work leads to quadratic time complexity.

The next optimization is to avoid repeatedly searching by using a data structure that allows fast lookups.

---

## Source Code

See `solution.cpp`.