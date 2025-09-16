# Interpreter project made with PLY in Python
An interpreter for my custom small programing languade which has instructions in Polish as well as a few other quirks

## Run
Use it by running a main.py file or a run.bat script

## Features
Current capabilities:
- All keywords are in Polsih
- Tokenization via PLY’s `lex` module
- Grammar rules via PLY’s `yacc`
- Declaration and assignment of variables
- Text output
- Comparison operators
- Logical operators (in Polish ex. "_lub" serving as the "or" logical operator)
- Arithmetic expressions: `+ - * / ` and parentheses
- If/else statements 
- Basic error reporting with token position info
- Comments

##Example
Small example of how the language looks. More in program.txt

całkowita x = 10;
całkowita y = 5;

jeżeli (x > y _i y != 0) {
    wypisz x;
}

jeżeli (x < y _lub y == 5) {
    wypisz y;
}


