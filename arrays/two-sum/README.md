# Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input has **exactly one solution**, and you may not use the same element twice.

You can return the answer in **any order**.

---

## Examples

### Example 1

**Input**

```text
nums = [2,7,11,15], target = 9
```

**Output**

```text
[0,1]
```

**Explanation**

Because `nums[0] + nums[1] == 9`, we return `[0,1]`.

---

### Example 2

**Input**

```text
nums = [3,2,4], target = 6
```

**Output**

```text
[1,2]
```

---

### Example 3

**Input**

```text
nums = [3,3], target = 6
```

**Output**

```text
[0,1]
```

---

## Constraints

- `2 <= nums.length <= 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`
- `-10⁹ <= target <= 10⁹`
- Only one valid answer exists.

---

## Approaches

- Brute Force
- Optimized Brute
- Optimal