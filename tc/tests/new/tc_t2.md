## Test 2 - Parsing

### A. Determine whether the following grammar is LL(1). Justify your answer.

S -> uBDz
B -> Bv | w
D -> EF
E -> y | ε
F -> x | ε

It is not LL(1) because the production for B is left-recursive (B -> Bv). Left recursion violates the LL(1) property, which requires that the grammar be free of left recursion.

Can be formally checked via a FIRST and FOLLOW set analysis.

### B. Rewrite the grammar to eliminate left recursion.

S -> uBDz
B -> wB'
B' -> vB' | ε
D -> EF
E -> y | ε
F -> x | ε

### C. The table below gives the Nullabke, First and Follow values for each non-terminal in the grammar. Using these values as a starting point, compute Nullable, First and Follow for any new non-terminals introduced in part B.

||Nullable|First|Follow|
|---|---|---|---|
|S|No|{u}|{$}|
|B|No|{w}|{v, y, x, z}|
|B'|Yes|{v}|{y, x, z}|
|D|Yes|{y, x}|{z}|
|E|Yes|{y}|{x, z}|
|F|Yes|{x}|{z}|

### D. Construct the LL(1) parsing table for the grammar in part B and determine whther it is LL(1). If it is not, explain why.

|| u | w | v | y | x | z | $ |
|---|---|---|---|---|---|---|---|
|S| S -> uBDz | | | | | | |
|B| | B -> wB' | | | | | |
|B'| | | B' -> vB' | B' -> ε | B' -> ε | B' -> ε | |
|D | | | | D -> EF | D -> EF | D -> EF | |
|E | | | | E -> y | E -> ε | E -> ε | |
|F | | | | | | F -> x | F -> ε | |

The rewritten grammar is indeed LL(1) as there are no conflicts in the parsing table. Each cell contains at most one production, satisfying the LL(1) condition.

### E. Consider the below grammar and its LR parsing table
E -> E + T
E -> T
T -> T * F
T -> F
F -> ( E )
F -> id

||id|+|*|( |)|$|E|T|F|
|---|---|---|---|---|---|---|---|---|---|
|0|s5|||s4|||1|2|3|
|1| |s6||| |a| | | |
|2| |r2|s7||r2|r2| | | |
|3| |r4|r4||r4|r4| | | |
|4|s5|||s4|||8|2|3|
|5| |r6|r6||r6|r6| | | |
|6|s5|||s4||| |9|3|
|7|s5|||s4||| | |10|
|8| |s6|||s11|| | | |
|9| |r1|s7||r1|r1| | | |
|10| |r3|r3||r3|r3| | | |
|11| |r5|r5||r5|r5| | | |

#### Using the LR parsing table above, trace the complete sequence of configurations of a shift-reduce parser on the input id * id, starting from the below configuration.

|Stack|Input|Action|
|---|---|---|
|0|id * id $|Shift|
|0 id 5|* id $|Reduce by F -> id|
|0 F 3| * id $|Reduce by T -> F|
|0 T 2| * id $|Shift|
|0 T 2 * 7|id $|Shift|
|0 T 2 * 7 id 5|$|F -> id|
|0 T 2 * 7 F 10|$|T -> T * F|
|0 T 2|$|Reduce by E -> T|
|0 E 1|$|Accept|

#### F. Consider the grammar below and its LR(0) automaton. Determine whether the grammar is LR(0) and justify your answer.

For a grammar to be considered LR(0), it must not have any shift-reduce or reduce-reduce conflicts in its LR(0) parsing table.
Based on the automaton, there is a shift/reduce conflict in state 2, where S -> E.+S and S-> E. are present. The first production indicates a shift action, while the second indicates a reduce action. This conflict violates the LR(0) property, which requires that each state in the automaton has a unique action for each input symbol. Therefore, the grammar is not LR(0).