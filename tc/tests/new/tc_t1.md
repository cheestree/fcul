## Test 1 - Lexical Analysis

### A. Describe informally the language accepted by the following finite automaton.

The automaton accepts strings over {a, b} that are empty, or that begin with b and do not contain the substring aa. In other words, every 'a' must be preceded by a 'b'.

### B. Construct a regular expression for currency in euros, represented as a positive decimal number rounded to the nrearest one-hundredth. Such numbers begin wit hteh charcter '€', have commas separating each group of three digits to the left of the decimal point, may not contain trailing zeroes, and end with two digits to the riht of the decimal point, for example, €1,234.56 is valid, but €1,234.5 and €1,234.567 are not.

[0-9]{1,3} represents the first group of one to three digits, (,[0-9]{3})* represents zero or more groups of a comma followed by exactly three digits, and \.[0-9]{2} represents a decimal point followed by exactly two digits. Therefore, the complete regular expression for the currency in euros is:

(€[0-9]{1,3}(,[0-9]{3})*\.[0-9]{2})

### C. Construct a finite automaton that accepts the following language.

{w belongs to {a, b}* | w contains aaa as a substring and does not contain bb as a substring}

(?=.*aaa) somewhere must be a substring of aaa, and (?!.*bb) must not be a substring of bb. The regular expression for this language is:

^(?=.*aaa)(?!.*bb)[ab]*$

So the finite automaton can be constructed as follows:
1. Start in the initial state q0.
2. From q0, if the input is 'a', transition to state q1;
3. From q1, if the input is 'a', transition to state q2;
4. From q2, if the input is 'a', transition to the accepting state q3;
5. From q0, if the input is 'b', transition to state q4;
6. From q4, if the input is 'a', transition to state q1;
7. From q4, if the input is 'b', transition to a dead state q5 (since 'bb' is not allowed);
8. From q1, if the input is 'b', transition to state q4;
9. From q2, if the input is 'b', transition to state q4;
10. From q3, if the input is 'a', stay in state q3 (since we have already accepted 'aaa');
11. From q3, if the input is 'b', transition to state q4;
12. From q5, if the input is 'a' or 'b', stay in state q5 (dead state).

### D. Consider the regular expression (0|1)*1100 1\*. Use the algorithm studied in class to construct an NFA for the regular expression. LAbel each state with adifferent capital letter.

1. Start in the initial state q0.
2. From q0, if the input is '0' or '1', transition to state q1 (this represents the (0|1)* part).
3. From q1, if the input is '1', transition to state q2.
4. From q2, if the input is '1', transition to state q3.
5. From q3, if the input is '0', transition to state q4.
6. From q4, if the input is '0', transition to state q5.
7. From q5, if the input is '1', transition to state q6 (this represents the 1* part).
8. From q6, if the input is '1', stay in state q6 (since we can have zero or more 1's).
9. From q6, if the input is '0', transition to a dead state q7 (since we cannot have any more 0's after the 1* part).
10. From q7, if the input is '0' or '1', stay in state q7 (dead state).

So, with thompsons construction, the NFA can be represented as follows:

### E. Use the subset consutrction algorithm (studied in class) to obtain a DFA equivalent to the previous one. Label your states according to exercise D.