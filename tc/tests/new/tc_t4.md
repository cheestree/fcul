## Test 3
### 1. Constant propagation; Common-subexpression elimination; Copy propagation; Folding; Branch & Dead-code elimination. Consider the following program.


    a = 2
    b = a + 3
    c = m + b
    d = m + b
    if a > b goto L2
L1: e=c * 4
    f=e
    g=f+d
    goto L3
L2: h=m+b
    g=h-1
L3: return g

#### a. Each of an and b is assigned once and never reassigned so its single definition reaches every later use. Apply constant propagation. In which statements does 'a' dissapear?

After constant propagation, 'a' dissapears in the following statements:
- b = 2 + 3
- if 2 > b goto L2

#### b. Apply constant folding to evaluate the constant expressions exposed by exercise a. Does constant folding open new opportunities for propagation? Which expressions reduce to a constant, and which stay symbolic because m is unknown?

With constant folding, the following expressions reduce to constants:
- b = 5
- if 2 > 5 goto L2

#### c. After folding, the test node at 5 becomes 2 > 5. Apply branch elimination. State what this implies for the L2 block (nodes 10-11). Remove the unreachable code.

Since the condition 2 > 5 is false, the branch to L2 will never be taken. Therefore, the L2 block (nodes 10-11) is unreachable and can be removed from the program.

    c = m + 5
    d = m + 5
L1: e=c * 4
    f=e
    g=f+d
    goto L3
L3: return g

#### d. The expression m + 5 is computed more than once on the remaining path. Identify the redundant recomputation and perform common-subexpression elimination.

The redundant recomputation is the expression `m + 5`, which is computed in both statements `c = m + b` and `d = m + b`. We can eliminate this redundancy by storing the result of `m + 5` in a temporary variable and reusing it.

t1 = m + 5
L1: e=t1 * 4
    f=e
    g=f+t1
    goto L3
L3: return g

#### e. Now apply copy propagation to the remaining copies. Then apply dead-code elimination removing every assignment whose target is no longer used. Give the final optimized program.

After applying copy propagation and dead-code elimination, the final optimized program is:

t1 = m + 5
e = t1 * 4
g = e + t1
return g

### 2. Liveness analysis; Dead code elimination. Consider the following program.

    s = c + d
    t = c - d
L1: if t < d goto L2
    d = d + 1
    s = c + d
    goto L1
L2

#### a. Compute the out-live variables at each node. The live variables are a subset of {c, d, s, t}. Suggestion: proceed backwards on thecontrol flow graph.

Control flow:

1 -> 2 -> 3
3 -> 4 if condition false
3 -> 7 if condition true
4 -> 5 -> 6 -> 3

| Node | Statement | Use | Def |
|---|---|---|---|---|
|1| s = c + d | {c, d} | {s} |
|2| t = c - d | {c, d} | {t} |
|3| if t < d goto L2 | {t, d} | {} |
|4| d = d + 1 | {d} | {d} |
|5| s = c + d | {c, d} | {s} |
|6| goto L1 | {} | {} |
|7| L2 | {} | {} |

