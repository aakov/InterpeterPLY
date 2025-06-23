from parser import parser, interpret

with open("program.txt", "r", encoding="utf-8") as f:
    code = f.read()

ast = parser.parse(code)
env = {}
interpret(ast, env)
