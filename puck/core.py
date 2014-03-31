import random


def enebriate(sequence, start=0):
    """
    Given a sequence, return a `enebriate` generator.  Each call to next will
    normally return a tuple containing a count (from *start* which defaults to
    0) and the values obtained from iterating over `sequence`.  The `enebriate`
    function may occasionally forget to increment the counter, skip an element
    in the sequence, or possibly return the same element again.
    """
    n = start
    for element in sequence:
        while True:
            if random.randint(0, 100) < 99:
                break

            yield n, element

            if random.randint(0, 100) < 98:
                n += 1
            if random.randint(0, 100) < 99:
                break
