def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    pass

	def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    # n = pq
    n = p * q

    # phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

    def gcd(a, b):
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if b==0:
        return a
    else:
        return gcd(b, a%b)
    pass
    def multiplicative_inverse(e, phi):
    """
    >>> multiplicative_inverse(7, 40)
    23
    """
    def gcdex(a, b):
        if b == 0:
            return a, 1, 0
        else:
            d, x, y = gcdex(b, a % b)
            return d, y, x - y * (a // b)

    d, x, y = gcdex(e, phi)
    return x % phi

    