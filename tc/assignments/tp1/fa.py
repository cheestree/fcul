import mermaid as md
from mermaid.graph import Graph

def main():
    render = md.Mermaid("""stateDiagram-v2
    [*] --> q0
    state "Start - no 1 seen" as q0
    state "Last symbol was 1" as q1
    state "Seen 11 once" as q2
    state "Trap" as q3 
    q0 --> q0 : 0
    q0 --> q1 : 1
    q1 --> q0 : 0
    q1 --> q2 : 1
    q2 --> q0 : 0
    q2 --> q3 : 1
    q3 --> q3 : 0,1
""")
    render.to_png("./tp1/diagrams/one_occurrence.png")

    render = md.Mermaid("""stateDiagram-v2
    [*] --> q0
    state "Start - no 1 seen" as q0
    state "Last symbol was 1 (0 occurrences)" as q1
    state "Seen 11 once - last not 1" as q2
    state "Seen 11 once - last was 1" as q3
    state "Seen 11 twice - last not 1" as q4
    state "Seen 11 twice - last was 1" as q5
    state "Trap" as qt
    q0 --> q0 : 0
    q0 --> q1 : 1
    q1 --> q0 : 0
    q1 --> q3 : 1
    q3 --> q2 : 0
    q3 --> q5 : 1
    q2 --> q2 : 0
    q2 --> q3 : 1
    q5 --> q4 : 0
    q5 --> qt : 1
    q4 --> q4 : 0
    q4 --> q5 : 1
""")
    render.to_png("./tp1/diagrams/two_occurrences.png")

    render = md.Mermaid("""stateDiagram-v2
    [*] --> q0
    state "Start - even number of 1s" as q0
    state "Odd number of 1s" as q1
    q0 --> q0 : 0
    q0 --> q1 : 1
    q1 --> q0 : 1
    q1 --> q1 : 0
""")
    render.to_png("./tp1/diagrams/even_ones.png")

    render = md.Mermaid("""stateDiagram-v2
    [*] --> q0
    state "Start / safe" as q0
    state "Seen 1" as q1
    state "Seen 10" as q2
    state "Trap (101 seen)" as qt
    q0 --> q0 : 0
    q0 --> q1 : 1
    q1 --> q1 : 1
    q1 --> q2 : 0
    q2 --> q0 : 0
    q2 --> qt : 1
    qt --> qt : 0,1
""")
    render.to_png("./tp1/diagrams/no_one_zero_one.png")

    render = md.Mermaid("""stateDiagram-v2
    [*] --> q0
    state "Start" as q0
    state "Valid identifier" as q1
    state "Invalid identifier" as q2
    q0 --> q1 : [a-zA-Z_]
    q0 --> q2 : [^a-zA-Z_]
    q1 --> q1 : [a-zA-Z0-9_]
    q1 --> q2 : [^a-zA-Z0-9_]
    q2 --> q2 : .*
""")
    render.to_png("./tp1/diagrams/identifier.png")

    render = md.Mermaid("""stateDiagram-v2
    [*] --> q0
    state "Start" as q0
    state "Valid boolean" as q1
    state "Invalid boolean" as q2
    q0 --> q1 : true
    q0 --> q1 : false
    q0 --> q2 : .*
    q1 --> q2 : .*
    q2 --> q2 : .*
""")
    render.to_png("./tp1/diagrams/boolean.png")

    render = md.Mermaid("""stateDiagram-v2
    [*] --> q0
    state "Start" as q0
    state "Valid double" as q1
    state "Invalid double" as q2
    q0 --> q1 : -?[0-9]+(\.[0-9]*)?([eE][+-]?[0-9]+)?[dD]?
    q0 --> q1 : -?\.[0-9]+([eE][+-]?[0-9]+)?[dD]?
    q0 --> q2 : .*
    q1 --> q1 : [0-9]+(\.[0-9]*)?([eE][+-]?[0-9]+)?[dD]?
    q1 --> q1 : \.[0-9]+([eE][+-]?[0-9]+)?[dD]?
    q1 --> q2 : .*
    q2 --> q2 : .*
""")
    render.to_png("./tp1/diagrams/double.png")

    render = md.Mermaid("""stateDiagram-v2
    [*] --> q0
    state "Start" as q0
    state "Valid integer" as q1
    state "Invalid integer" as q2
    q0 --> q1 : -?[0-9]+
    q0 --> q2 : .*
    q1 --> q1 : [0-9]+
    q1 --> q2 : .*
    q2 --> q2 : .*
""")
    render.to_png("./tp1/diagrams/integer.png")
    
    render = md.Mermaid("""stateDiagram-v2
    [*] --> q0
    state "Start" as q0
    state "Valid float" as q1
    state "Invalid float" as q2
    q0 --> q1 : -?([0-9]*\.[0-9]+|[0-9]+\.[0-9]*)([eE][+-]?[0-9]+)?[fF]
    q0 --> q2 : .* 
    q1 --> q1 : ([0-9]*\.[0-9]+|[0-9]+\.[0-9]*)([eE][+-]?[0-9]+)?[fF]
    q1 --> q2 : .*
    q2 --> q2 : .*
""")
    render.to_png("./tp1/diagrams/float.png")
if __name__ == "__main__":
    main()