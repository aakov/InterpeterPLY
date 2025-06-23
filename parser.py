import ply.yacc as yacc
from lexer import tokens

class Number:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Variable:      # NAZWA
    def __init__(self, name):
        self.name = name

class BinOp:         # operatory
    def __init__(self, left, op, right):
        self.left, self.op, self.right = left, op, right

class UnOp:          # negacja
    def __init__(self, op, operand):
        self.op, self.operand = op, operand

class Assignment:
    def __init__(self, name, value):
        self.name, self.value = name, value

class Declaration:
    def __init__(self, name, value):
        self.name, self.value = name, value

class Print:
    def __init__(self, expression):
        self.expression = expression

class IfElse:
    def __init__(self, condition, true_block, false_block):
        self.condition, self.true_block, self.false_block = condition, true_block, false_block

class Block:
    def __init__(self, statements):
        self.statements = statements

# === GRAMATYKA ===

precedence = (
    ('left', 'LUB'),
    ('left', 'I'),
    ('left', 'ROWNE', 'ROZNE'),
    ('left', 'MNIEJSZE', 'MNIEJSZE_ROWNE', 'WIEKSZE', 'WIEKSZE_ROWNE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'RAZY', 'DZIEL'),
    ('right', 'NEGACJA'),
)

def p_program(p):
    'program : statements'
    p[0] = Block(p[1])


def p_block(p):
    'block : LBRACE statements RBRACE'
    p[0] = Block(p[2])

def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    'statements : statement'
    p[0] = [p[1]]

def p_statement_declaration(p):
    '''statement : CALKOWITA NAZWA SREDNIK
                 | CALKOWITA NAZWA PRZYPISZ expression SREDNIK'''
    if len(p) == 4:
        p[0] = Declaration(p[2], Number(0))
    else:
        p[0] = Declaration(p[2], p[4])


def p_statement_assignment(p):
    'statement : NAZWA PRZYPISZ expression SREDNIK'
    p[0] = Assignment(p[1], p[3])

def p_statement_print(p):
    'statement : WYPISZ expression SREDNIK'
    p[0] = Print(p[2])

def p_statement_if(p):
    'statement : JEZELI LNAWIAS expression PNAWIAS block'
    p[0] = IfElse(p[3], p[5], None)

def p_statement_if_else(p):
    'statement : JEZELI LNAWIAS expression PNAWIAS block INACZEJ block'
    p[0] = IfElse(p[3], p[5], p[7])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression RAZY expression
                  | expression DZIEL expression
                  | expression ROWNE expression
                  | expression ROZNE expression
                  | expression MNIEJSZE expression
                  | expression MNIEJSZE_ROWNE expression
                  | expression WIEKSZE expression
                  | expression WIEKSZE_ROWNE expression
                  | expression I expression
                  | expression LUB expression'''
    p[0] = BinOp(p[1], p[2], p[3])

def p_expression_unary(p):
    'expression : NEGACJA expression'
    p[0] = UnOp(p[1], p[2])

def p_expression_group(p):
    'expression : LNAWIAS expression PNAWIAS'
    p[0] = p[2]

def p_expression_number(p):
    'expression : LICZBA'
    p[0] = Number(p[1])

def p_expression_variable(p):
    'expression : NAZWA'
    p[0] = Variable(p[1])

def p_error(p):
    if p:
        print(f"Błąd składniowy przy tokenie {p.type} ({p.value}) w linii {p.lineno}")
    else:
        print("Błąd składniowy przy końcu wejścia")

parser = yacc.yacc()

# === INTERPRETACJA ===

def interpret(node, env):
    if isinstance(node, Block):
        for stmt in node.statements:
            interpret(stmt, env)

    elif isinstance(node, Declaration):
        if node.name in env:
            raise Exception(f"Zmienna '{node.name}' już zadeklarowana")
        env[node.name] = interpret(node.value, env)

    elif isinstance(node, Assignment):
        if node.name not in env:
            raise Exception(f"Nieznana zmienna '{node.name}'")
        env[node.name] = interpret(node.value, env)

    elif isinstance(node, Print):
        value = interpret(node.expression, env)
        print(value)

    elif isinstance(node, IfElse):
        condition = interpret(node.condition, env)
        if condition:
            interpret(node.true_block, env)
        elif node.false_block:
            interpret(node.false_block, env)

    elif isinstance(node, Number):
        return node.value

    elif isinstance(node, Variable):
        if node.name not in env:
            raise Exception(f"Nieznana zmienna '{node.name}'")
        return env[node.name]

    elif isinstance(node, BinOp):
        left = interpret(node.left, env)
        right = interpret(node.right, env)
        op = node.op
        if op == '+': return left + right
        if op == '-': return left - right
        if op == '*': return left * right
        if op == '/': return left // right
        if op == '==': return left == right
        if op == '!=': return left != right
        if op == '<': return left < right
        if op == '<=': return left <= right
        if op == '>': return left > right
        if op == '>=': return left >= right
        if op == '_i': return bool(left) and bool(right)
        if op == '_lub': return bool(left) or bool(right)

    elif isinstance(node, UnOp):
        value = interpret(node.operand, env)
        if node.op == '!':
            return not value

    else:
        raise Exception(f"Nieobsługiwany typ węzła: {type(node)}")