# Add Two Numbers

## Problem Statement

You are given two **non-empty linked lists** representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number `0` itself.

---

## Examples

### Example 1

**Input**

```text
l1 = [2,4,3]
l2 = [5,6,4]
```

**Output**

```text
[7,0,8]
```

**Explanation**

```text
342 + 465 = 807
```

Since the digits are stored in reverse order, the resulting linked list is:

```text
7 → 0 → 8
```

---

### Example 2

**Input**

```text
l1 = [0]
l2 = [0]
```

**Output**

```text
[0]
```

---

### Example 3

**Input**

```text
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
```

**Output**

```text
[8,9,9,9,0,0,0,1]
```

---

## Constraints

- `1 <= Number of nodes in each linked list <= 100`
- `0 <= Node.val <= 9`
- The input lists represent numbers with no leading zeros (except the number `0` itself).

---

## Key Observations

- The digits are stored **in reverse order**, so addition naturally starts from the head of each linked list.
- The two linked lists may have **different lengths**.
- A **carry** generated at one digit must be propagated to the next digit.
- The final addition may generate an **extra carry**, requiring a new node at the end.

---

## Approach

- Optimal (Simulation)

---

## Related Topics

- Linked List
- Math
- Simulation

---

## Difficulty

**Medium**