def imprimir_dados(numero, texto):
    print("Dentro da funcao:")
    print("Número vinculado ao parametro 'numero':", numero)
    print("Texto vinculado ao parametro 'texto':", texto)

numero_exemplo = 42
texto_exemplo = "Python e incrivel!"

print("Fora da funcao:")
print("Número antes da chamada da funcao:", numero_exemplo)
print("Texto antes da chamada da funcao:", texto_exemplo)
imprimir_dados(numero_exemplo, texto_exemplo)
print("Fora da funcao apos a chamada:")
print("Numero apos a chamada da funcao:", numero_exemplo)
print("Texto apos a chamada da funcao:", texto_exemplo)