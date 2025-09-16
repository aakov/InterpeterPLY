# Interpreter Project Made with PLY in Python

An interpreter for my custom small programming language which has instructions in Polish as well as a few other quirks.

## Run

You can run the interpreter in two ways:
- Execute the `main.py` file directly  
- Use the provided `run.bat` script  

## Features

Current capabilities:

- All keywords are in **Polish**  
- Tokenization via PLY’s **`lex`** module  
- Grammar rules via PLY’s **`yacc`** module  
- Declaration and assignment of variables  
- Text output (`wypisz`)  
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)  
- Logical operators in Polish (e.g. `_lub` = OR, `_i` = AND)  
- Arithmetic expressions: `+ - * /` and parentheses  
- If/else statements (`jeżeli` / `inaczej`)  
- Basic error reporting with token position info  
- Comments  

## Example

Here’s a small example of how the language looks (see more in `program.txt`):

```text
całkowita x = 10;
całkowita y = 5;

jeżeli (x > y _i y != 0) {
    wypisz x;
}

jeżeli (x < y _lub y == 5) {
    wypisz y;
}
-
