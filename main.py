def task1(input_string: str) -> bool:
    """
    The finite state machine for searching for a subword "abacab".
    :param input_string: (str) Input string with word.
    :return: (bool) True if the subword "abacab" was found, else False.
    """

    alphabet = {'a', 'b', 'c'}
    states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
    start_state = 'q0'
    final_state = 'q6'

    transitions = {
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


if __name__ == "__main__":
    print(task1("cabacabac"))
    print("---------------------")
    print(task1("cabaaaaaac"))
