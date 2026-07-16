# Optimal (Simulation)

## Intuition

The digits of both numbers are stored in **reverse order**, meaning the least significant digit appears first.

This allows us to simulate the same addition process we perform by hand:

1. Add the corresponding digits from both linked lists.
2. Include any carry from the previous addition.
3. Store the current digit (`sum % 10`) in the result list.
4. Carry forward (`sum / 10`) to the next iteration.

Since the linked lists may have different lengths, we continue until both lists are exhausted **and** there is no remaining carry.

---

## Algorithm

1. Create a dummy node to simplify result list construction.
2. Maintain a pointer `tail` to the last node of the result list.
3. Initialize `carry = 0`.
4. While at least one list has remaining nodes or a carry exists:
   - Initialize `sum = carry`.
   - If the first list has a node, add its value and move to the next node.
   - If the second list has a node, add its value and move to the next node.
   - Compute:
     - `digit = sum % 10`
     - `carry = sum / 10`
   - Append a new node containing `digit` to the result list.
5. Return `dummy->next`.

---

## Dry Run

### Input

```text
l1 = [2,4,3]
l2 = [5,6,4]
```

These represent:

```text
342
465
```

| Step | l1 | l2 | Carry In | Sum | Digit | Carry Out | Result |
|-----:|---:|---:|---------:|----:|------:|----------:|--------|
| 1 | 2 | 5 | 0 | 7 | 7 | 0 | 7 |
| 2 | 4 | 6 | 0 | 10 | 0 | 1 | 7 → 0 |
| 3 | 3 | 4 | 1 | 8 | 8 | 0 | 7 → 0 → 8 |

Final Answer:

```text
[7,0,8]
```

---

### Another Example

```text
l1 = [9,9]
l2 = [1]
```

| Step | l1 | l2 | Carry In | Sum | Digit | Carry Out | Result |
|-----:|---:|---:|---------:|----:|------:|----------:|--------|
| 1 | 9 | 1 | 0 | 10 | 0 | 1 | 0 |
| 2 | 9 | - | 1 | 10 | 0 | 1 | 0 → 0 |
| 3 | - | - | 1 | 1 | 1 | 0 | 0 → 0 → 1 |

Final Answer:

```text
[0,0,1]
```

---

## Complexity Analysis

### Time Complexity

**O(max(m, n))**

Each node from both linked lists is visited exactly once.

Where:

- `m` = length of the first linked list
- `n` = length of the second linked list

---

### Space Complexity

**O(max(m, n))**

A new linked list is created to store the result.

Ignoring the output list itself, the auxiliary space complexity is **O(1)**.

---

## Why This Approach Works

The numbers are already stored in reverse order, allowing us to process them from the least significant digit to the most significant digit.

By maintaining a carry and traversing both linked lists simultaneously, every digit is processed exactly once.

The dummy node simplifies insertion into the result list by eliminating special handling for the first node.

---

## Key Takeaways

- Reverse-order storage eliminates the need to reverse either linked list.
- A single traversal is sufficient.
- A dummy node simplifies linked list construction.
- Continue while **either list has nodes or a carry remains**.

---

## Patterns Learned

- Dummy Node
- Tail Pointer
- Carry Propagation
- Simultaneous Traversal of Two Linked Lists

## Source Code

See `solution.cpp`.