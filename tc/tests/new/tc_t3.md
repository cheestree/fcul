## Test 3 - AST, semantics and stack
### A. Consider a typing environment (or context), mapping variables xi to types Ti

E = x1: T1, ..., xn: Tn

Further consider a bidirectional type system with judgements of the two forms below.
E ⊢ e ⇐ T (e checks against type T in context E) E ⊢ e input, T output (under context E, synthesize T of expression e)
E ⊢ e ⇒ T (e synthesizes type T in context E) E ⊢ e ⇐ T input (under context E, analyze expression e against Type t)

#### a. Consider a language with support for arrays. The type of an array access expression is T if exp1 is of type T[] and exp2 is of type int. an array access expression is written exp1[exp2] where exp1 denotes an array and exp2 an index in the array. Write the synthesis rule for array access.

The synthesis rule for array access can be expressed as follows:
```
E ⊢ exp1 ⇒ T[]   E ⊢ exp2 ⇐ int
-----------------------------------
E ⊢ exp1[exp2] ⇒ T
```

#### b. Now write the analysis rule for array access.
The analysis rule for array access can be expressed as follows:
```
E ⊢ exp1 ⇐ T[]   E ⊢ exp2 ⇐ int
-----------------------------------
E ⊢ exp1[exp2] ⇐ T
```

#### c. Recall the synthesis rule for function call expressions:
```
E ⊢ e1 ⇒ (T → U)   E ⊢ e2 ⇐ T
-----------------------------------
E ⊢ e1(e2) ⇒ U
```
Write the analysis rule for function call expressions.

The analysis rule for function call expressions can be expressed as follows:
```
E ⊢ e1 ⇒ (T → U)   E ⊢ e2 ⇐ T  U = V
-----------------------------------
E ⊢ e1(e2) ⇐ U
```

#### d. COnsider the following MAGOITO expression insert("hi") where insert is a function of type String -> Int. Consider the goal:

```
E ⊢ insert("hi") ⇐ Bool
```

where E is the environment insert: String -> Int. This goal may be validated with the genreal rule for analysis or else the special rule derived in item 1c. Each could yield a different error message. Propose messages for each case. Include the expression or sub-expression target of the error message (include the text of the expressions involved or the column numbers). Explain how each error message is obtained; consider writing the typing derivation in each case.

For analysis using the general rule, we have:
```
E ⊢ insert("hi") ⇒ Int   E ⊢ Bool ⇐ Bool
-----------------------------------
E ⊢ insert("hi") ⇐ Bool
```

So we can have an error message of type mismatch: expected Bool but found Int in expression insert("hi").

but with the special rule derived in item 1c, we have:
```
E ⊢ insert ⇒ (String → Int)   E ⊢ "hi" ⇐ String
-----------------------------------
E ⊢ insert("hi") ⇐ Int
```

So we can have an error message of type mismatch: expected Int but found Bool in expression insert("hi").


### 2. COnsider the following program:

type strlist = {head: string, tail: strlist}
function join(words: strlist) : string =
    let
        var output :=
        function emit (s: string) =
            output := concat (output, s)
        function walk(sep: string, ws: strlist) =
            let function pad(s: string) =
                (for i := 1 to 2
                    do emit (" ");
                output := concat (output, s))
            in if ws = nil then emit ("."))
                else (pad({ws.head);
                emit (sep);
                walk(sep, ws.tail))
        end
    in walk(",", words); output
end

and the goal join({head="a", tail={head="b", tail=nil}}).

#### a. Draw the various stack frames when evaluation is about to call concat(output, "b") on line 14. Include the local variables, the return address (in the form of a line number) and the arguments. Draw the static links of each frame by means of arrows connectiong frames.

Top to bottom, the stack frames are as follows:

Frame: pad
Arguments:
  s = "b"
Locals:
  i = after/inside loop, depending on exact point
Return address:
  line after pad(ws.head), probably line 15: emit(sep)
Static link:
  points to the second walk frame
Dynamic link:
  points to the second walk frame

Frame: walk  [second call]
Arguments:
  sep = ","
  ws = { head = "b", tail = nil }
Locals:
  function pad
Return address:
  line after recursive call in the first walk, probably end of else branch
Static link:
  points to join frame
Dynamic link:
  points to first walk frame

Frame: walk  [first call]
Arguments:
  sep = ","
  ws = { head = "a", tail = { head = "b", tail = nil } }
Locals:
  function pad
Return address:
  line after walk(",", words) in join
Static link:
  points to join frame
Dynamic link:
  points to join frame

Frame: join
Arguments:
  words = { head = "a", tail = { head = "b", tail = nil } }
Locals:
  output
  function emit
  function walk
Return address:
  caller of join
Static link:
  points to global frame
Dynamic link:
  points to caller frame



#### b. Given teh stack frames. explain how function pad accesses variable output.

The runtime follows static links according to lexical nesting. The function pad accesses the variable output through its static link, which points to the join frame where output is defined.