import ply.yacc as yacc
from lexer import tokens
execution_enabled = True

# Słownik do przechowywania zmiennych
variables = {}

def p_program(p):
    '''
    program : statement
            | program statement
    '''
    pass

def p_statement(p):
    '''
    statement : declaration
              | assignment
              | print_stmt
              | if_stmt
    '''
    pass

def p_declaration(p):
    '''
    declaration : CALKOWITA NAZWA SREDNIK
                | CALKOWITA NAZWA PRZYPISZ expression SREDNIK
    '''
    if len(p) == 4:
        variables[p[2]] = 0
    else:
        variables[p[2]] = p[4]

def p_assignment(p):
    '''
    assignment : NAZWA PRZYPISZ expression SREDNIK
    '''
    if p[1] not in variables:
        print(f"Błąd: Zmienna '{p[1]}' nie została zadeklarowana")
    else:
        variables[p[1]] = p[3]

def p_if_stmt(p):
    '''
    if_stmt : JEZELI LNAWIAS condition PNAWIAS LBRACE statement RBRACE
            | JEZELI LNAWIAS condition PNAWIAS LBRACE statement RBRACE INACZEJ LBRACE statement RBRACE
    '''

    print("trigger")
    if len(p) == 8:
        p[0] = ("if", p[3], p[6], None)
    else:
        p[0] = ("if", p[3], p[6], p[10])

def p_do(p):
    '''
    do : LBRACE statement RBRACE
    '''

def p_condition(p):
    '''
    condition : expression ROWNE expression
              | expression ROZNE expression
              | expression MNIEJSZE expression
              | expression WIEKSZE expression
              | expression MNIEJSZE_ROWNE expression
              | expression WIEKSZE_ROWNE expression
    '''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]

def p_expression(p):
    '''
    expression : term
               | expression PLUS term
               | expression MINUS term
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_term(p):
    '''
    term : factor
         | term RAZY factor
         | term DZIEL factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            print("Błąd: Dzielenie przez zero!")
            p[0] = 0
        else:
            p[0] = p[1] / p[3]

def p_factor(p):
    '''
    factor : LICZBA
           | NAZWA
           | LNAWIAS expression PNAWIAS
    '''
    if len(p) == 2:
        if isinstance(p[1], int):
            p[0] = p[1]
        else:
            if p[1] in variables:
                p[0] = variables[p[1]]
            else:
                print(f"Błąd: Niezadeklarowana zmienna '{p[1]}'")
                p[0] = 0
    else:
        p[0] = p[2]

def p_print_stmt(p):
    '''
    print_stmt : WYPISZ NAZWA SREDNIK
    '''
    global execution_enabled
    if execution_enabled == True:
        if p[2] not in variables:
            print(f"Błąd: Zmienna '{p[2]}' nie została zadeklarowana")
        else:
            print(variables[p[2]])

def p_error(p):
    if p:
        print(f"Błąd składni w linii {p.lineno}: Nieoczekiwany token '{p.value}'")
    else:
        print("Błąd składni: Nieoczekiwany koniec pliku")

# Budowanie parsera
parser = yacc.yacc()