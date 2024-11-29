from __future__ import annotations
from ast import Tuple
from itertools import product
import sys

sys.setrecursionlimit(100000)

import copy

class DFA:
    def __init__(self) -> None:
        self.states = {}
        self.transitions = list()
        self.final_states = set()

        self.construct()


    def construct(self):
        self.num_states, self.alphabet_size, self.initial_state, self.num_final_states = map(int, input().strip().split())


        self.symbols = input().strip()


        self.final_states = set(map(int, input().strip().split()))

        for i in range(1, self.num_states + 1):
            self.states[i] = State(i)


        for i in range(1, self.num_states + 1):
            transitions = input().strip().split()
            self.transitions.append(transitions)
            for j, symbol in enumerate(self.symbols):
                destination = int(transitions[j])
                self.states[i].connections[symbol] = self.states[destination]


        for state in self.final_states:
            self.states[state].final = True


    def read(self):
        strings = int(input())

        for i in range(strings):
            current_state = self.states[self.initial_state]

            transitions = list(input())

            for transition in transitions:

                if transition in current_state.connections:
                    # print(f"Current state: {current_state} transitioning with {transition} to {current_state.connections[transition]}")
                    current_state = current_state.connections[transition]
                else:
                    print("reject")
                    break
            else:
                if current_state.final:
                    print("accept")
                else:
                    print("reject")


    def complement(self):
        complement_dfa = copy.deepcopy(self)
        complement_dfa.final_states = [x for x in range(1, self.num_states + 1) if x not in self.final_states]

        return complement_dfa
        # print(complement_dfa.num_states, complement_dfa.alphabet_size, complement_dfa.initial_state, len(complement_dfa.final_states))
        # print(complement_dfa.symbols)
        # print(*complement_dfa.final_states)
        # for transition in complement_dfa.transitions:
        #     print(*transition)


    def union(self, other_dfa: DFA):
        union_dfa = DFA.__new__(DFA)
        union_dfa.symbols = self.symbols
        union_dfa.alphabet_size = self.alphabet_size
        
        states_union = set(product(self.states.keys(), other_dfa.states.keys()))

        union_state_names = dict()
        union_state_idx = 1

        union_dfa.final_states = set()
        for (s1, s2) in sorted(states_union):
            union_state_names[s1, s2] = union_state_idx
            
            if (s1 in self.final_states) or (s2 in other_dfa.final_states):
                union_dfa.final_states.add(union_state_idx)
            
            union_state_idx += 1 

        union_dfa.num_final_states = len(union_dfa.final_states)
        union_dfa.initial_state = union_state_names[self.initial_state, other_dfa.initial_state]
        
        union_dfa.states = union_state_names
        union_dfa.num_states = len(union_state_names)

        union_dfa.num_states = len(states_union)
        union_dfa.num_final_states = len(union_dfa.final_states)

        transitions_union = []
        for (s1, s2) in sorted(states_union):
            transition = []
            for symbol in union_dfa.symbols:
                next_s1 = self.states[s1].connections[symbol].name
                next_s2 = other_dfa.states[s2].connections[symbol].name
                new_state = union_state_names[next_s1, next_s2]
                transition.append(str(new_state))
            transitions_union.append(transition)

        union_dfa.transitions = transitions_union
        return (union_dfa, states_union)
        # union_dfa.print_cause_strings_in_python_dont_concatinate_well()

    def intersection(self, other_dfa: DFA):
        intersection_dfa, states_union = self.union(other_dfa)
        
        intersection_dfa.final_states = {
            intersection_dfa.states[(s1, s2)]
            for (s1, s2) in states_union
            if s1 in self.final_states and s2 in other_dfa.final_states
        }
        
        intersection_dfa.num_final_states = len(intersection_dfa.final_states)
        
        intersection_dfa.print_cause_strings_in_python_dont_concatinate_well()

    def difference(self, other_dfa: DFA):
        complement_other = other_dfa.complement()
        self.intersection(complement_other)
    
    def print_cause_strings_in_python_dont_concatinate_well(self):
        print(self.num_states, self.alphabet_size, self.initial_state, len(self.final_states))
        print(self.symbols)
        print(*sorted(self.final_states))
        for transition in self.transitions:
            print(*transition)
 


    def __str__(self):
        result = f"{self.num_states} {self.alphabet_size} {self.initial_state} {len(self.final_states)}\n"
        result += f"{self.symbols}\n"
        result += " ".join(map(str, self.final_states)) + "\n"
        for i in range(self.num_states - 1):
            result += " ".join(self.transitions[i]) + "\n"

        return result

        

            

class State:
    def __init__(self, name):
        self.connections = dict()
        self.final = False 
        self.name = name # for debugging purposes

    def __repr__(self):
        return f"State({self.name}, final={self.final})"