class DFA:
    def __init__(self) -> None:
        self.states = {}
        self.num_states = None
        self.alphabet_size = None
        self.initial_state = None
        self.num_final_states = None

        self.final_states = None
        self.symbols = None

        self.construct()


    def construct(self):
        self.num_states, self.alphabet_size, self.initial_state, self.num_final_states = map(int, input().strip().split())


        self.symbols = input().strip()


        self.final_states = list(map(int, input().strip().split()))

        for i in range(1, self.num_states + 1):
            self.states[f"state_{i}"] = State(f"state_{i}")


        for i in range(1, self.num_states + 1):
            transitions = input().strip().split()
            for j, symbol in enumerate(self.symbols):
                destination = int(transitions[j])
                self.states[f"state_{i}"].connections[symbol] = self.states[f"state_{destination}"]


        for state in self.final_states:
            self.states[f"state_{state}"].final = True


    def read(self):
        strings = int(input())

        for i in range(strings):
            current_state = self.states[f"state_{self.initial_state}"]

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
        num_states = None
        alphabet_size = None
        initial_state = None
        num_final_states = None

        final_states = None
        symbols = None

class State:
    def __init__(self, name):
        self.connections = dict()
        self.final = False 
        self.name = name # for debugging purposes

    def __repr__(self):
        return f"State({self.name}, final={self.final})"