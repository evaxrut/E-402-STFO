from __future__ import annotations
from ast import Tuple
from itertools import product
import sys
from collections import deque
# from graphviz import Digraph
import logging
import cProfile
import pstats

sys.setrecursionlimit(100000)

import copy

LOG = logging.getLogger(__name__)

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

    def symmetric_difference(self, other_dfa: DFA) -> DFA:
        sym_diff_dfa = DFA.__new__(DFA)
        sym_diff_dfa.symbols = self.symbols
        sym_diff_dfa.alphabet_size = self.alphabet_size

        states_product = set(product(self.states.keys(), other_dfa.states.keys()))

        sym_diff_state_names = {}
        sym_diff_state_idx = 1

        sym_diff_dfa.final_states = set()
        for (s1, s2) in sorted(states_product):
            sym_diff_state_names[(s1, s2)] = sym_diff_state_idx
            if (s1 in self.final_states) != (s2 in other_dfa.final_states):
                sym_diff_dfa.final_states.add(sym_diff_state_idx)

            sym_diff_state_idx += 1

        sym_diff_dfa.num_states = len(sym_diff_state_names)
        sym_diff_dfa.num_final_states = len(sym_diff_dfa.final_states)
        sym_diff_dfa.initial_state = sym_diff_state_names[(self.initial_state, other_dfa.initial_state)]
        sym_diff_dfa.states = sym_diff_state_names

        transitions_sym_diff = []
        for (s1, s2) in sorted(states_product):
            transition = []
            for symbol in sym_diff_dfa.symbols:
                next_s1 = self.states[s1].connections[symbol].name
                next_s2 = other_dfa.states[s2].connections[symbol].name
                new_state = sym_diff_state_names[(next_s1, next_s2)]
                transition.append(int(new_state))
            transitions_sym_diff.append(transition)

        sym_diff_dfa.transitions = transitions_sym_diff

        sym_diff_dfa.print_cause_strings_in_python_dont_concatinate_well()
    
    def print_cause_strings_in_python_dont_concatinate_well(self):
        print(self.num_states, self.alphabet_size, self.initial_state, len(self.final_states))
        print(self.symbols)
        print(*sorted(self.final_states))
        for transition in self.transitions:
            print(*transition)

    def is_empty_question_mark(self):
        visited = set()
        queue = deque([self.initial_state]) 

        while queue:
            current = queue.popleft()
            if current in self.final_states:
                print("non-empty")
                return
            if current in visited:
                continue
            visited.add(current)

            for symbol in self.symbols:
                next_state = self.states[current].connections[symbol].name
                if next_state not in visited:
                    queue.append(next_state)

        print("empty")

    def minimum_word_length(self):
        word_len = 0
        visited = set()
        queue = deque([(self.initial_state, 0)]) 

        while queue:
            current, word_len = queue.popleft()
            if current in self.final_states:
                print(word_len)
                return
            if current in visited:
                continue
            visited.add(current)

            for symbol in self.symbols:
                next_state = self.states[current].connections[symbol].name
                if next_state not in visited:
                    queue.append((next_state, word_len + 1))

    def topological_sort(self, intersection):
        # https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
        # copy_dfa = DFA.__new__(DFA)
        # copy_dfa.states = self.states
        # copy_dfa = 

        inter = {state for state in self.states if state in intersection}

        in_degree = {state: 0 for state in inter}
        for state in inter:
            for symbol, neighbor in self.states[state].connections.items():
                if neighbor.name in inter:
                    in_degree[neighbor.name] += 1

        L = list()
        S = deque([state for state in inter if in_degree[state] == 0])

        while S:
            n = S.popleft()
            L.append(n)
            connections_copy = self.states[n].connections.copy()
            for symbol, m in connections_copy.items():
                if m.name in inter:
                    in_degree[m.name] -= 1
                    # del self.states[n].connections[symbol] 
                    if in_degree[m.name] == 0:
                        S.append(m.name)
        
        if any(in_degree[state] > 0 for state in inter):
            print("infinite")
        else:
            return(L)

    def accessable(self):
        accessible = set()
        queue = deque([self.initial_state])

        while queue:
            current = queue.popleft()
            if current not in accessible:
                accessible.add(current)
                for symbol, next_state in self.states[current].connections.items():
                    if next_state.name not in accessible:
                        queue.append(next_state.name)

        return accessible

    def reverse_transitions(self) -> dict:
        reverse_trans = {state: set() for state in self.states}
        for state in self.states.values():
            for symbol, next_state in state.connections.items():
                reverse_trans[next_state.name].add(state.name)
        return reverse_trans

    def co_accessable(self):
        co_accessible = set()
        queue = deque(self.final_states)
        reverse_transitions = self.reverse_transitions()

        while queue:
            current = queue.popleft()
            if current not in co_accessible:
                co_accessible.add(current)
                for predecessor in reverse_transitions.get(current, []):
                    if predecessor not in co_accessible:
                        queue.append(predecessor)

        return co_accessible

    def is_finite(self):
        #TODO: find accessible
        accessible = self.accessable()

        #TODO find co-accessable
        co_accessible = self.co_accessable()
        #TODO: sniðmengi af þeim
        intersection_ = accessible.intersection(co_accessible)
        return self.topological_sort(intersection_)

    def __str__(self):
        result = f"{self.num_states} {self.alphabet_size} {self.initial_state} {len(self.final_states)}\n"
        result += f"{self.symbols}\n"
        result += " ".join(map(str, self.final_states)) + "\n"
        for i in range(self.num_states - 1):
            result += " ".join(self.transitions[i]) + "\n"

        return result


    def concatenate(self, other):
        def up(i):
            return int(i) + int(self.num_states)

        def down(i):
            return int(i) - int(self.num_states)

        def get_transition(i, j):
            if i <= self.num_states:
                return int(self.transitions[i - 1][j])
            else:
                return up(other.transitions[down(i) - 1][j])

        initial_state = {self.initial_state}
        if self.initial_state in self.final_states:
            initial_state.add(up(other.initial_state))
        initial_state = frozenset(initial_state)
        new_states = [initial_state]
        set_state_map = dict()
        set_state_map[initial_state] = 1
        new_final_states = set()
        new_transitions = [[]]
        queue = deque([initial_state])

        while queue:
            cur_state = queue.popleft()
            if any(down(x) in other.final_states for x in cur_state):
                new_final_states.add(set_state_map[cur_state])
            for j in range(len(self.symbols)):
                next_state = set()
                for elem in cur_state:
                    next_state.add(get_transition(int(elem), int(j)))
                if any(x in self.final_states for x in next_state):
                    next_state.add(up(other.initial_state))
                next_state = frozenset(next_state)
                if next_state not in set_state_map:
                    set_state_map[next_state] = len(new_states) + 1
                    new_states.append(next_state)
                    new_transitions.append([])
                    queue.append(next_state)

                new_transitions[set_state_map[cur_state] - 1].append(set_state_map[next_state])

        concatinated_dfa = DFA.__new__(DFA)
        concatinated_dfa.states = new_states
        concatinated_dfa.symbols = self.symbols
        concatinated_dfa.num_states = len(new_states)
        concatinated_dfa.final_states = new_final_states
        concatinated_dfa.num_final_states = len(new_final_states)
        concatinated_dfa.alphabet_size = len(self.symbols)
        concatinated_dfa.transitions = new_transitions
        concatinated_dfa.initial_state = 1 

        # concatinated_dfa.print_cause_strings_in_python_dont_concatinate_well()
        return concatinated_dfa

    def maximum_word_length(self):
        # f = dict()
        toplogogical_sort = self.is_finite()
        assert toplogogical_sort is not None
        # print(toplogogical_sort)

        top_set = set(toplogogical_sort)

        distance = {state: -1 for state in self.states}
        # distance = dict()

        distance[self.initial_state] = 0

        # states = [state for state in self.states if state in toplogogical_sort]
        for state in toplogogical_sort:
            # print("state: ", state)
            if distance[state] == -1:
                # LOG.debug("distance[state] "  distance[state])
                continue
            LOG.debug("here1")
            LOG.debug(f"connections , {self.states[state].connections}")
            for symbol, neighbour in self.states[state].connections.items():
                # LOG.debug("neighbour name: ", neighbour.name)
                if neighbour.name in top_set:
                    LOG.debug("here")
                    distance[neighbour.name] = max(distance[neighbour.name], distance[state] + 1)
            #TODO
        
        # LOG.debug("distance: ", distance)
        max_length = -1
        for final_state in self.final_states:
            if final_state in distance and distance[final_state] != -1:
                max_length = max(max_length, distance[final_state])
                # print("distance: ", distance[final_state])

        # print(distance)

        print(max_length)
   


    def kleene_star(self):
        concat = self.concatenate



        

class State:
    def __init__(self, name):
        self.connections = dict()
        self.final = False 
        self.name = name
        self.accessible = False
        self.coaccessible = False

    def __repr__(self):
        return f"State({self.name}, final={self.final})"

def main():
    dfa1 = DFA()
    dfa1.maximum_word_length()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # cProfile.run("main()", "output.prof")
    # stats = pstats.Stats("output.prof")
    # stats.sort_stats("cumulative").print_stats()
    main()