numero = int(input("Informe o número que deseja consultar:"))
calculo = 0
fibonacci = [0,1]
contador = 0

while numero > fibonacci[1 + contador]:
    calculo = fibonacci[0 + contador] + fibonacci[1 + contador]
    fibonacci.append(calculo)
    contador += 1

print(fibonacci)
if numero in fibonacci:
    print("O número ",numero," está dentro da sequência de Fibonacci.")
else:
    print("O número ",numero," não está dentro da sequência de Fibonacci.")
