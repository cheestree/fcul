import re as r

def main():
    one_occurrence = r"^(0|10)*11(01|0)*$" # (0|10)*11(0|01)*
    two_occurrences = r"^(0|10)*11(0|01)*11(01|0)*$"
    even_ones = r"^0*(10*10*)*$"
    no_one_zero_one = r"^(0|11|100)*(|1|10)$"

    identifier = r"^([a-zA-Z_][a-zA-Z0-9_]*'*)$"
    boolean = r"^(true|false)$"
    double = r"^-?([0-9]+(\.[0-9]*)?|\.[0-9]+)([eE][+-]?[0-9]+)?[dD]?$"
    integer = r"^-?[0-9]+$"
    float = r"^-?([0-9]*\.[0-9]+|[0-9]+\.[0-9]*)([eE][+-]?[0-9]+)?[fF]$"

    print(r.match(one_occurrence, "1101"))
    print(r.match(two_occurrences, "110110"))
    print(r.match(even_ones, "1010"))
    print(r.match(no_one_zero_one, "1001"))

    print(r.match(identifier, "_validIdentifier123"))
    print(r.match(boolean, "true"))
    print(r.match(double, "-3.14e-10"))
    print(r.match(integer, "-42"))
    print(r.match(float, "3.14"))

if __name__ == "__main__":
    main()