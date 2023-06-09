# 1

def pertenece(c: list, z: int) -> bool:
    res: bool = c.__contains__(z)
    return res


def pertenece2(c: list, z: int) -> bool:
    res: bool = False
    for j in c:
        if (j == z):
            res = True
            break
    return res


def perteneceGenerico(c: list, z: any) -> bool:
    res: bool = False
    for j in c:
        if (j == z):
            res = True
            break
    return res

# 2


def divideATodos(c: list, z: int) -> bool:
    res: bool
    for j in c:
        print(j)
        if (j % z == 0):
            res = True
        else:
            res = False
            break
    return res

# 3


def sumaTotal(s: list) -> int:
    res: int = 0
    for j in s:
        res += j
    return res

# 4


def ordenados(s: list) -> bool:
    res: bool = False
    aux: int = s[0]
    for j in s:
        if (j >= aux):
            aux = j
            res = True
            continue
        else:
            res = False
            break
    return res

# 5


def palabrasMayorA7(s: str) -> bool:
    res: bool = (len(s) > 7)
    return res

# 6


def esPalindromo(s: str) -> bool:
    res: bool = (s[::-1] == s)  # el operador [::-1] me da la lista invertida
    return res

# 7

# Funciones auxiliares


def palabrasMayorA(z: int, s: str) -> bool:
    res: bool = (len(s) > z)
    return res


def contieneUnaMayuscula(s: str) -> bool:
    res: bool = False
    for letter in s:
        if (letter.upper == letter):
            res = True
            break
    return res


def contieneUnaMinuscula(s: str) -> bool:
    res: bool = False
    for letter in s:
        if (letter.upper != letter):
            res = False
            break
    return res

# Funcion del ejercicio


def seguridadContrasena(password: str) -> str:
    res: str
    if (palabrasMayorA(8, password) and contieneUnaMayuscula(password) and contieneUnaMinuscula(password)):
        res = 'VERDE'
    if (not (palabrasMayorA(6, password))):
        res = 'ROJA'
    else:
        res = 'AMARILLA'
    return res
