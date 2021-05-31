import sys

def verificaA():
    global a
    a = int(input("Informe o número corresponde ao a na equação de 2º grau: "))
    if a == 0:
        print("Essa equação não é de 2º grau!")
        sys.exit(0)

def equacaoSegundoGrau():
    verificaA()

    b = int(input("Informe o número corresponde ao b na equação de 2º grau: "))
    c = int(input("Informe o número corresponde ao c na equação de 2º grau: "))

    delta = (b**2 - 4*a*c)
    x1 = (-b + (delta**0.5))/(2*a)
    x2 = (-b - (delta**0.5))/(2*a)

    if delta < 0:
        print("O delta é igual a zero, portanto a equação não possui raízes reais.")
    elif delta == 0:
        print("A equação só possui uma raiz real: ", x1)
    elif delta > 0:
        print("As duas raízes dessa equação de segundo grau são", x1, "e", x2)

equacaoSegundoGrau()