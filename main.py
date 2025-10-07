from itertools import product
from pprint import pprint

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
