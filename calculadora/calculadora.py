def soma (a, b):
	return a + b 

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

operacao = input("+ : Soma\n- : Subtração\n* : Multiplicação\n/ : Divisão\n ** : Exponenciação\n ")
if operacao == '+':
	resultado = soma(a, b)
elif operacao == '-':
	resultado = a - b
elif operacao == '*':
	resultado = a * b
elif operacao == '/':
	resultado = a / b
else:
	resultado = a ** b
print(resultado)
 