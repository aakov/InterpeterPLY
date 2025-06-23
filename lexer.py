import ply.lex as lex

# Lista tokenów
tokens = (
    'CALKOWITA',      # słowo kluczowe 'całkowita'
    'NAZWA',          # identyfikatory
    'PRZYPISZ',       # znak równa się =
    'LICZBA',         # liczby całkowite
    'SREDNIK',        # średnik ;
    'WYPISZ',         # wypisz
    'PLUS',           # +
    'MINUS',          # -
    'RAZY',          # *
    'DZIEL',         # /
    'ROWNE',         # ==
    'ROZNE',         # !=
    'MNIEJSZE',      # <
    'WIEKSZE',       # >
    'MNIEJSZE_ROWNE', # <=
    'WIEKSZE_ROWNE',  # >=
    'JEZELI',        # jeżeli
    'INACZEJ',       # inaczej
    'LNAWIAS',        # (
    'PNAWIAS',        # )
    'LBRACE',        # {
    'RBRACE',        # }
    'I',
    'LUB',
    'NEGACJA',
    'KOMENATRZ',
)

# Reguły wyrażeń regularnych dla prostych tokenów
t_PRZYPISZ = r'='
t_SREDNIK = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_RAZY = r'\*'
t_DZIEL = r'/'
t_ROWNE = r'=='
t_ROZNE = r'!='
t_MNIEJSZE = r'<'
t_WIEKSZE = r'>'
t_MNIEJSZE_ROWNE = r'<='
t_WIEKSZE_ROWNE = r'>='
t_LNAWIAS = r'\('
t_PNAWIAS = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_I = r'_i'
t_LUB = r'_lub'
t_NEGACJA = r'_nie'

# Ignorowanie białych znaków i tabulatorów
t_ignore = ' \t'

def t_CALKOWITA(t):
    r'całkowita'
    return t

def t_JEZELI(t):
    r'jeżeli'
    return t

def t_INACZEJ(t):
    r'inaczej'
    return t

def t_WYPISZ(t):
    r'wypisz'
    return t

def t_NAZWA(t):
    r'[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ][a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ0-9]*'
    return t

def t_LICZBA(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Błąd: Nieznany znak '{t.value[0]}' w linii {t.lineno}")
    t.lexer.skip(1)

def t_KOMENATRZ(t):
    r'//.*'
    pass  # Ignoruj


# Budowanie leksera
lexer = lex.lex()