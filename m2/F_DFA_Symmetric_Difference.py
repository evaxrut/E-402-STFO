from DFA2 import DFA

dfa1 = DFA()
dfa2 = DFA()

# union_dfa, x = dfa1.union(dfa2)
# inter_dfa = dfa1.intersection(dfa2)

symmetric_diff_dfa = dfa1.symmetric_difference(dfa2)