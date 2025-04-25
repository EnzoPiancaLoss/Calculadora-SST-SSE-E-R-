import math

def exportar_para_txt(texto, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(texto)

    print("Arquivo criado")


def somarArray(arr):
    final = 0
    for i in arr:
        final += i
    return final 
    pass

def Media(Array):
    total = 0
    for i in Array:
        total += i
    
    return total/len(Array)
    pass

def CalcularSEE(ArrValores, ArrPrevisao):
    
    if len(ArrValores) != len(ArrPrevisao):
        return "Error"

    arryNovo = []

    for i in range(len(ArrValores)):
        #Primeiramente você ve a diferencia entre 'Valor' e previsão para cada item
        h = ArrValores[i] - ArrPrevisao[i]

        #Segundamente você eleva ao quadrado
        #Ai você tem que fazer algo tipo assim: (h²).
        #Pois se o numero for negativo, o valor de h fica positivo no final

        j = math.pow(h,2) 
        arryNovo.append(j)
    
    #Ai é só somar todos os itens
    valor_final = somarArray(arryNovo)
    return valor_final
    pass

def CalcularSST(valoresA):

    #Calcular media
    mediaA = Media(valoresA)
    
    #Calcular diferença entre valor e media 
    arrayNew = []
    for i in range(len(valoresA)):
        g = valoresA[i] - mediaA

        #Depois de calcular a diferença, eleve ao quadrado
        #(g)²
        
        f = math.pow(g,2)
        arrayNew.append(f)
    
    #Some tudo
    valor_final = somarArray(arrayNew)

    return valor_final
    pass

def Rquadrado(SST,SSE):
    #r² = 1 - (SSE/SST)
    return 1 - (SSE/SST)
    pass



def main():
    ##########################
    print("Hora de inserir as informações :)")
    print("Exemplo de formatação: 10 20 30 40\n")
    valores = [int(x) for x in input("Digite valores dos itens: ").split()]
    previsao = [int(x) for x in input("Digite as previsões: ").split()]
    ##########################
    #
    #
    #



    Sse = CalcularSEE(valores,previsao)

    if Sse == "Error":
        print("valores e previsão devem ter a mesma quantidade de item nos arrays")
        return
        pass

    Sst = CalcularSST(valores)

    media = Media(valores)

    RMinecraft = Rquadrado(Sst,Sse)

    

    # print("#Valores: ", valores)
    # print("#Previsão: ", previsao)

    # print("Media dos valores: ", media)

    # print("=====\nSEE\n=====\n", Sse)
    # print("\n")
    # print("=====\nSST\n=====\n", Sst)
    # print("\n")
    # print("=====\nR²\n=====\n",RMinecraft)

    string_de_saida = "---------------------------------------\n"
    string_de_saida += "INPUTS;\n"
    string_de_saida += "Valores:" + str(valores) + "\n"
    string_de_saida += "Previsão:" + str(previsao) + "\n"
    string_de_saida += "Media(Valores):" + str(media) + "\n"
    string_de_saida += "---------------------------------------\n"
    string_de_saida += "RESULTADOS;\n"
    string_de_saida += "SSE:" + str(Sse) + "\n"
    string_de_saida += "SST:" + str(Sst) + "\n"
    string_de_saida += "R²:" + str(RMinecraft) + "\n"

    print(string_de_saida)

    exportar_para_txt(string_de_saida, "Resultados_r².txt")
    pass


#Só para o script ter uma função main :P
if __name__ == "__main__":
    main()
