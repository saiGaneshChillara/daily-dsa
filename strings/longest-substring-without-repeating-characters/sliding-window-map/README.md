# Sliding Window with Map

## Intuition

The Sliding Window with Set approach maintains a window containing unique characters.

When a duplicate character is encountered, we move the `left` pointer one position at a time and remove characters from the set until the duplicate is removed.

We can optimize this further by storing the **last index at which each character appeared**.

Instead of moving `left` one step at a time, we can directly jump it to the position immediately after the previous occurrence of the duplicate character.

For example, consider:

```text
s = "abcabcbb"
```

After processing:

```text
a b c
0 1 2
```

we encounter another `a` at index `3`.

The map tells us:

```text
lastIndex['a'] = 0
```

Therefore, instead of removing `a`, then `b`, then `c` one by one, we can directly move:

```text
left = 0 + 1
```

So the new window starts at index `1`:

```text
b c a
↑   ↑
left right
```

This allows us to skip unnecessary pointer movements.

---

## Algorithm

1. Initialize:
   - `left = 0`
   - `maxLength = 0`
   - An `unordered_map` to store the last index of each character.

2. Iterate through the string using `right`.

3. For each character:
   - Check if the character has appeared before.
   - If it has, update `left` to the position immediately after its previous occurrence.
   - Update the character's latest index in the map.
   - Calculate the current window length.
   - Update `maxLength`.

4. Return `maxLength`.

---

## Important Condition

When a duplicate character is found, we cannot blindly move `left` backward.

For example:

```text
s = "abba"
```

Consider the second `a` at index `3`.

At this point:

```text
left = 2
```

The previous occurrence of `a` was at index `0`.

If we directly set:

```text
left = 0 + 1
```

we would move `left` backward from `2` to `1`, which would make the window invalid.

Therefore, we use:

```text
left = max(left, lastIndex[s[right]] + 1)
```

This guarantees that `left` only moves forward.

---

## Dry Run

### Input

```text
s = "abcabcbb"
```

Initial state:

```text
left = 0
maxLength = 0
map = {}
```

---

### `right = 0`

Character:

```text
'a'
```

Not seen before.

```text
map['a'] = 0
```

Window:

```text
"a"
```

Length:

```text
1
```

---

### `right = 1`

Character:

```text
'b'
```

Not seen before.

```text
map['b'] = 1
```

Window:

```text
"ab"
```

Length:

```text
2
```

---

### `right = 2`

Character:

```text
'c'
```

Not seen before.

```text
map['c'] = 2
```

Window:

```text
"abc"
```

Length:

```text
3
```

---

### `right = 3`

Character:

```text
'a'
```

`a` was previously seen at index `0`.

Therefore:

```text
left = max(0, 0 + 1)
left = 1
```

Update:

```text
map['a'] = 3
```

Current window:

```text
"bca"
```

Length:

```text
3
```

Notice that we directly jumped `left` from `0` to `1`.

---

### `right = 4`

Character:

```text
'b'
```

Previous occurrence:

```text
map['b'] = 1
```

Update:

```text
left = max(1, 1 + 1)
left = 2
```

Current window:

```text
"cab"
```

Length:

```text
3
```

---

### `right = 5`

Character:

```text
'c'
```

Previous occurrence:

```text
map['c'] = 2
```

Update:

```text
left = max(2, 2 + 1)
left = 3
```

Current window:

```text
"abc"
```

Length:

```text
3
```

The longest substring remains:

```text
"abc"
```

Therefore:

```text
Answer = 3
```

---

## Why Use `max()`?

Consider:

```text
s = "abba"
```

At `right = 3`:

```text
a b b a
```

Before processing the final `a`:

```text
left = 2
```

The previous `a` was at index `0`.

If we did:

```text
left = lastIndex['a'] + 1
```

we would get:

```text
left = 1
```

This moves `left` backward, which is incorrect.

Instead:

```text
left = max(left, lastIndex['a'] + 1)
```

gives:

```text
left = max(2, 1)
left = 2
```

Therefore, `left` never moves backward.

---

## Complexity Analysis

### Time Complexity

We iterate through the string exactly once.

Hash map operations are `O(1)` on average.

Therefore:

```text
O(n)
```

---

### Space Complexity

The map stores the last known index of each distinct character.

```text
O(min(n, charset))
```

where `charset` is the number of distinct possible characters.

---

## Comparison with Sliding Window + Set

### Sliding Window + Set

When a duplicate is found:

```text
Move left one step at a time
Remove characters from the set
```

### Sliding Window + Map

When a duplicate is found:

```text
Use its last known index
Jump left directly
```

Both approaches have:

```text
Time:  O(n)
Space: O(min(n, charset))
```

The map version is more direct because it avoids repeatedly removing characters from the set.

---

## Complete Progression

```text
Brute Force
O(n³)
    ↓
Optimized Brute Force
O(n²)
    ↓
Sliding Window + Set
O(n)
    ↓
Sliding Window + Map
O(n)
```

The final two approaches have the same asymptotic complexity, but the map-based approach demonstrates how storing additional information about previous character positions allows the `left` pointer to jump directly.

---

## Source Code

See `solution.cpp`.