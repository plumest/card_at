import doctest

def cardAt(n: int):
    """ Return the name of nth card

    Args:
        n (int): The number of card, from 0 to 51.
    
    Returns:
        str: The string that contain two character first is face, second suit.
            For example: 'AC', '2H' or '0S'

    Raises:
        TypeError: If `n` is not integer.
        CardError: If `n` range is not between 0 to 51.

    >>> cardAt(0)
    '2C'
    >>> cardAt(1)
    '3C'
    >>> cardAt(34)
    '0H'
    >>> cardAt(51)
    'AS'
    >>> cardAt(52)
    Traceback (most recent call last):
        ...
    cardAt.CardError: 52 is not in range 0 and 51
    >>> cardAt('3')
    Traceback (most recent call last):
        ...
    TypeError: <class 'str'> is not 'int'
    """

    suits = ['C', 'D', 'H', 'S']
    faces = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
    if not isinstance(n, int):
        # If n is not integer then raise an error.
        raise TypeError(f"{type(n)} is not 'int'")
    elif(0 <= n <= 51):
        # Check that, `n` in range of 0 and 51. If true return card's name of nth.
        suit_index = int(n / 13)
        face_index = n - suit_index * 13
        suit = suits[suit_index]
        face = faces[face_index]
        return face + suit
    else:
        # If n do not in range of 0 and 51 raise an error.
        raise CardError(f'{n} is not in range 0 and 51')


class CardError(Exception):
    """ Exception that throw when input isn't integer from 0 to 51"""
    pass


if __name__ == "__main__":
    doctest.testmod()

for i in range(52):
    print(cardAt(i))