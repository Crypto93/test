def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1)>len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if (0<=dna1.find(dna2)):
        return True

    return False


def is_valid_sequence(dna):
    '''(str) -> bool

    Check if the dna is a valid DNA sequence. Sequence with non-capital letters is not a valid DNA sequence.

    >>> is_valid_sequence('ATACAGAT')
    True
    >>> is_valid_sequence('ATGREAT')
    False
    '''

    condition=True
    for char in dna:
        if char not in 'ATCG':
            condition=False
        
    return condition

def insert_sequence(dna1, dna2, index):
    '''(str, str, int) -> str

    Add dna2 to dna1 at a certain index. Assume that the index is valid.

    >>> insert_sequence('ATAT', 'CG', 2)
    'ATCGAT'
    >>> insert_sequence('CGATC', 'ATAT', 0)
    'ATATCGATC'
    '''

    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    '''(str) -> str

    Returns the complement of  a given nucleotide.

    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    '''

    if nucleotide in 'A':
        return 'T'
    elif nucleotide in 'T':
        return 'A'
    elif nucleotide in 'C':
        return 'G'
    elif nucleotide in 'G':
        return 'C'

def get_complementary_sequence(dna):
    '''(str) -> str

    Returns the complementary sequence of  a given dna.

    >>> get_complementary_sequence('ATCG')
    'TAGC'
    >>> get_complementary_sequence('GCGAT')
    'CGCTA'
    '''
    complementary_sequence=''
    
    for char in dna:
        if char in 'A':
            complementary_sequence=complementary_sequence + 'T'
        elif char in 'T':
            complementary_sequence=complementary_sequence + 'A'
        elif char in 'C':
            complementary_sequence=complementary_sequence + 'G'
        elif char in 'G':
            complementary_sequence=complementary_sequence + 'C'

    return complementary_sequence
