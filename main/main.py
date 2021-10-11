def printMenu():
    print("1.Citire date")
    print("2.Determinare cea mai lungă subsecvență cu proprietatea 5.")
    print("3.Determinare cea mai lungă subsecvență cu proprietatea 2.")
    print("Pentru a inchide, introduce x")


def citire_lista():
    lst = []
    n = int(input("Dati numarul de elemente din lista: "))
    for i in range(n):
        lst.append(int(input("lst[" + str(i) + "]=")))
    return lst


def is_palindrome(n):
    '''
    Determina daca un numar este palindrom sau nu
    :param n numar intreg:
    :return True daca n este palindrom sau False daca nu:
    '''
    auxiliar = int(n)
    k = 0
    while auxiliar > 0:
        k = k * 10 + auxiliar % 10
        auxiliar = auxiliar // 10
    if n == k:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(189) is False
    assert is_palindrome(18981) is True
    assert is_palindrome(72) is False


test_is_palindrome()


def toateElementelePalindroame(lst):
    """
    Determina daca toate numerele dintr-o secventa a listei lst sunt palindrom
    :param lst - lista de numere:
    :return True sau False:
    """
    for x in lst:
        if is_palindrome(x) is False:
            return False
    return True


def get_longest_all_palindromes(lst: list[int]):
    """
    Determina cea mai lunga subsecventa de numere de tip palindrom
    :param lst - lista de numere:
    :return lista cu cea mai lunga subsecventa de numere palindrom din lst:
    """
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if toateElementelePalindroame(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = lst[i:j + 1]
    return subsecventaMax


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([1, 2, 89, 3, 4, 5, 6]) == [3, 4, 5, 6]
    assert get_longest_all_palindromes([2, 3, 4, 1, 5]) == [2, 3, 4, 1, 5]


test_get_longest_all_palindromes()


def NrPrim(n):
    '''
    Functia determina daca un numar este prim sau nu
    :param n numar intreg:
    :return adevarat sau fals:
    '''
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def toateElementelePrime(lst):
    """
    Determina daca toate numerele dintr-o secventa a listei lst sunt prime
    :param lst - lista de numere:
    :return True sau False:
    """
    for x in lst:
        if NrPrim(x) is False:
            return False
    return True


def get_longest_all_primes(lst: list[int]):
    """
    Determina cea mai lunga subsecventa de numere prime
    :param lst - lista de numere:
    :return lista cu cea mai lunga subsecventa de numere prime din lst:
    """
    subsecventaMax1 = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if toateElementelePrime(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax1):
                subsecventaMax1 = lst[i:j + 1]
    return subsecventaMax1


def test_get_longest_all_primes():
    assert get_longest_all_primes([12, 7, 3, 5, 6]) == [7, 3, 5]
    assert get_longest_all_primes([2, 4, 6]) == [2]
    assert get_longest_all_primes([8, 4, 6]) == []


test_get_longest_all_primes()

test_get_longest_all_primes()

while True:
    printMenu()
    optiune = input("Dati optiunea: ")
    if optiune == "1":
        l = citire_lista()
    elif optiune == "2":
        l1 = get_longest_all_palindromes(l)
        print(l1[:])
    elif optiune == "3":
        l2 = get_longest_all_primes(l)
        print(l2[:])
    elif optiune == "x":
        break
