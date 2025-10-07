from itertools import product
from pprint import pprint

import matplotlib.pyplot as plt
import networkx as nx

alphabet = {'a', 'b', 'c'}


def task1(input_string: str) -> bool:
    """
    The finite state machine for searching for a subword "abacab".
    :param input_string: (str) Input string with word.
    :return: (bool) True if the subword "abacab" was found, else False.
    """

    start_state, final_state = 'q0', 'q6'

    transitions: dict[tuple[str, str], str] = {
        ('q0', 'a'): 'q1', ('q0', 'b'): 'q0', ('q0', 'c'): 'q0',
        ('q1', 'a'): 'q1', ('q1', 'b'): 'q2', ('q1', 'c'): 'q0',
        ('q2', 'a'): 'q3', ('q2', 'b'): 'q0', ('q2', 'c'): 'q0',
        ('q3', 'a'): 'q1', ('q3', 'b'): 'q4', ('q3', 'c'): 'q0',
        ('q4', 'a'): 'q1', ('q4', 'b'): 'q0', ('q4', 'c'): 'q5',
        ('q5', 'a'): 'q6', ('q5', 'b'): 'q2', ('q5', 'c'): 'q0',
        ('q6', 'a'): 'q6', ('q6', 'b'): 'q6', ('q6', 'c'): 'q6',
    }

    # Searching for a subword
    current_state = start_state

    for symbol in input_string:
        if symbol not in alphabet:
            print("S T O P")
            return False

        current_state = transitions[(current_state, symbol)]
        print(f"{symbol} -> {current_state}")

    return current_state == final_state


def task2(table1: dict[tuple[str, str], str], table2: dict[tuple[str, str], str],
          final_states1: list[str], final_states2: list[str]) -> None:
    """
    Construction of the union and intersection of two finite machines.
    :param table1: (dict[tuple[str, str], str]) Machine 1 transfer table.
    :param table2: (dict[tuple[str, str], str]) Machine 2 transfer table.
    :param final_states1: (list[str]) Final states for machine 1.
    :param final_states2: (list[str]) Final states for machine 2.
    :return: None
    """

    states1 = set(q for (q, _) in t1.keys())
    states2 = set(q for (q, _) in t2.keys())
    states = set(product(states1, states2))

    transition = {}
    unification = []
    intersection = []

    for (q1, q2) in states:
        for a in alphabet:
            state1 = table1.get((q1, a), q1)
            state2 = table2.get((q2, a), q2)
            transition[((q1, q2), a)] = (state1, state2)

        if q1 in final_states1 or q2 in final_states2:
            unification.append((q1, q2))
        if q1 in final_states1 and q2 in final_states2:
            intersection.append((q1, q2))

    print(type(transition))
    pprint(transition)

    print("Unification")
    print(*unification)

    print("Intersection")
    print(*intersection)


def draw(transitions: dict[tuple[str, str], str], start_state, final_states) -> None:
    """
    Draw DFA using NetworkX and Matplotlib.
    :param transitions: (dict[tuple[str, str], str])  Machine transfer table.
    :param start_state: (str) Start state.
    :param final_states: (list[str]) Final states.
    :return: None
    """
    G = nx.DiGraph()

    edge_labels = {}
    for (state, symbol), next_state in transitions.items():
        if G.has_edge(state, next_state):
            edge_labels[(state, next_state)] += f", {symbol}"
        else:
            G.add_edge(state, next_state)
            edge_labels[(state, next_state)] = symbol

    pos = nx.spring_layout(G)

    plt.figure(figsize=(8, 6))
    node_colors = ['lightgreen' if n in final_states else 'lightblue' for n in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1500)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, connectionstyle='arc3, rad=0.1')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    x, y = pos[start_state]
    plt.scatter(x - 0.2, y, s=300, c='green', marker='>')
    plt.text(x - 0.25, y + 0.05, 'start', fontsize=10, fontweight='bold')

    plt.axis('off')
    plt.title("DFA Visualization")
    plt.show()


if __name__ == "__main__":
    print(task1("cabacabac"))
    print("---------------------")
    print(task1("cabaaaaaac"))

    t1: dict[tuple[str, str], str] = {
        ('q0', 'a'): 'q1', ('q0', 'b'): 'q0', ('q0', 'c'): 'q0',
        ('q1', 'a'): 'q2', ('q1', 'b'): 'q1', ('q1', 'c'): 'q0',
        ('q2', 'a'): 'q3', ('q2', 'b'): 'q2', ('q2', 'c'): 'q0',
        ('q3', 'a'): 'q4', ('q3', 'b'): 'q3', ('q3', 'c'): 'q2',
        ('q4', 'a'): 'q0', ('q4', 'b'): 'q4', ('q4', 'c'): 'q3',
    }
    t2: dict[tuple[str, str], str] = {
        ('q0', 'a'): 'q1', ('q0', 'b'): 'q0', ('q0', 'c'): 'q0',
        ('q1', 'a'): 'q2', ('q1', 'b'): 'q1', ('q1', 'c'): 'q0',
        ('q2', 'a'): 'q3', ('q2', 'b'): 'q2', ('q2', 'c'): 'q1',
        ('q3', 'a'): 'q4', ('q3', 'b'): 'q3', ('q3', 'c'): 'q2',
        ('q4', 'a'): 'q0', ('q4', 'b'): 'q4', ('q4', 'c'): 'q3',
    }

    pprint(t1)
    pprint(t2)

    task2(t1, t2, ['q2', 'q4'], ['q1', 'q3'])

    # draw(t2, 'q0', ['q1', 'q3'])
    # draw(t1, 'q0', ['q2', 'q4'])
