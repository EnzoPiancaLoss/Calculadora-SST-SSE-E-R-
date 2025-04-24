import math

def exportar_para_txt(texto, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(texto)

    print("Arquivo criado")


def CalcularPropocao(arr):
    total = 0
    arrNew = []
    for i in arr:
        total += i
    
    for y in arr:
        arrNew.append(y/total)
    return arrNew

def FormulaGini(arr):
    d = 0
    for i in arr:
        d += math.pow(i,2)
    
    return 1 - d
    pass

def main():
    ClassLen = int(input("Numero de classes: "))
    arry = []
    for i in range(ClassLen):
        print("Inisra a quantidade de itens da classe", str(i + 1))
        arry.append(int(input(": ")))
        pass

    Stringg = str(arry) + "\n"
    
    s = CalcularPropocao(arry)
    Gini = FormulaGini(s)
    Stringg += str(s) + "\n" + "Formula gini:" + "\n" + str(Gini)
    print(Stringg)
    exportar_para_txt(Stringg, "Gini.txt")
    pass

if __name__ == "__main__":
    main()
