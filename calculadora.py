#!/usr/bin/env python3

def main():
    while True:
        n1 = input("Digite o primeiro número: ").strip()
        operador = input("Digite um operador '+, -, * ou /': ").strip()
        n2 = input("Digite o segundo número: ").strip()

        if not n1:
            print("Você precisa digitar o primeiro número...")
            continue
        if not operador:
            print("Você precisa digitar um operador...")
            continue
        if not n2:
            print("Você precisa digitar o segundo número...")
            continue

        try:
            n1_float = float(n1)
            n2_float = float(n2)
        except ValueError:
            print("Digite apenas números...")
            continue

        if len(operador) != 1:
            print("Você deve digitar apenas um operador...")
            continue
        if operador not in "+-/*":
            print("Você precisa digitar apenas um dos seguintes operadores (+, -, / ou *)")
            continue
        if operador == "/" and n2_float == 0:
            print("Não é permitido divisão por 0...")
            continue

        if operador == "+":
            resultado = n1_float + n2_float
        elif operador == "-":
            resultado = n1_float - n2_float
        elif operador == "/":
            resultado = n1_float / n2_float
        elif operador == "*":
            resultado = n1_float * n2_float

        print(f"{n1_float} {operador} {n2_float} = {resultado}")

        sair = input("Quer [s]air?: ").lower().startswith("s")
        if sair:
            print("Você saiu")
            break

if __name__ == "__main__":
    main()
