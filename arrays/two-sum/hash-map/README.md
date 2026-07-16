# Optimal (Hash Map)

## Intuition

The brute force approach repeatedly searches the remaining elements for a number that forms the target sum. This results in many unnecessary comparisons.

Instead, while traversing the array, we can remember the elements we have already seen using a **hash map**.

For every element `nums[i]`, compute the value required to reach the target:

```text
complement = target - nums[i]
```

If the complement has already been seen, we have found the required pair and can immediately return their indices.

Otherwise, store the current element and its index in the hash map and continue.

This eliminates the need for the nested loop and reduces the time complexity from **O(n²)** to **O(n)**.

---

## Algorithm

1. Create an empty hash map to store `(value → index)`.
2. Traverse the array from left to right.
3. For each element:
   - Compute `complement = target - nums[i]`.
   - If the complement exists in the hash map:
     - Return the stored index of the complement and the current index.
   - Otherwise, insert the current element and its index into the hash map.
4. Since the problem guarantees exactly one solution, the algorithm will always return a valid answer.

---

## Dry Run

### Input

```text
nums = [2, 7, 11, 15]
target = 9
```

| Index | Value | Complement | Hash Map | Action |
|------:|------:|-----------:|----------|--------|
| 0 | 2 | 7 | {} | Store `(2 → 0)` |
| 1 | 7 | 2 | {2 → 0} | ✅ Complement found. Return `{0, 1}` |

---

### Another Example

```text
nums = [3, 2, 4]
target = 6
```

| Index | Value | Complement | Hash Map | Action |
|------:|------:|-----------:|----------|--------|
| 0 | 3 | 3 | {} | Store `(3 → 0)` |
| 1 | 2 | 4 | {3 → 0} | Store `(2 → 1)` |
| 2 | 4 | 2 | {3 → 0, 2 → 1} | ✅ Complement found. Return `{1, 2}` |

---

## Complexity Analysis

### Time Complexity

**O(n)**

The array is traversed only once.

Each hash map lookup and insertion takes **O(1)** on average.

```text
Time Complexity = O(n)
```

---

### Space Complexity

**O(n)**

In the worst case, every element is stored in the hash map.

```text
Space Complexity = O(n)
```

---

## Why This Approach Works

Instead of searching the remaining elements for every index, the hash map remembers all previously visited elements.

For each element, finding the required complement becomes an average **O(1)** operation instead of scanning the rest of the array.

This reduces the overall complexity from **O(n²)** to **O(n)**.

---

## Key Observation

For every element `x`, we only need to know whether

```text
target - x
```

has already been seen.

A hash map provides exactly this capability with constant-time average lookup.

---

## Source Code

See `solution.cpp`.