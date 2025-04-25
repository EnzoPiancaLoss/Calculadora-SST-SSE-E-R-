#                   #Realidade positivo     #Realidade negativo
#-------------------#-----------------------#---------------------
#Previsão (positivo)# TP (Verda.Positivo)   # FP (Falso Positivo)
#Previsão (Negativo)# Fn (Falso.Negativo)   # TN (Verdadeiro negativo)
#                   #                       #


# TP: O item é positivo, e o sistema diz que é positivo
# TN: O item é negativo, e o sistema diz que é negativo

# FN: O item é positivo, e o sistema diz que é negativo
# FP: O item é negativo, e o sistema diz que é positivo

def CalcularF1Score(Sen,Esp):
    Sen = float(Sen)
    Esp = float(Esp)
    return 2 * ((Sen * Esp) / (Sen + Esp))


def exportar_para_txt(texto, nome_arquivo):

    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(texto)

    print("Arquivo criado")

def converterParaPorcentagem(x):
    return str(x * 100) + "%"
    pass

def returnTotal(arr):
    f = 0
    for i in arr:
        f += i
    return f
    pass

#Calcula a habilidade em achar corretamente casos que são postivos
def Sensitividade(true_p, false_n):
    return true_p / (true_p + false_n)
    pass

#Calcula a habilidade em achar casos que são negativos
def Especifidade(true_n, false_p):
    return true_n / (true_n + false_p)
    pass

#Retorna o desenpenho em achar os itens que relamentes são verdadeiros e negativos
def Acuracia(tp,tn,fp,fn):
    return (tp + tn) / returnTotal([tp,tn,fp,fn])
    pass



def calculo(TrueN, FalseP, FalseN, TrueP):
    
    #Em codigo é diferente a posição
    Previsao_Negativo = [TrueN,FalseP] 
    Previsao_Positivo = [FalseN,TrueP] 

    totalDeItens = returnTotal([TrueP,TrueN,FalseN,FalseP])

    MatrizDeConfusao = [
        Previsao_Negativo,
        Previsao_Positivo
    ]

    sen = Sensitividade(TrueP,FalseN)
    esp = Especifidade(TrueN,FalseP)
    
    f1score = converterParaPorcentagem(CalcularF1Score(sen,esp))

    sen = converterParaPorcentagem(sen)
    esp = converterParaPorcentagem(esp)

    Acc = converterParaPorcentagem(Acuracia(TrueP,TrueN,FalseP,FalseN))

    String_output = "\nCalculando....\n"
    String_output += "------------------------\n"
    String_output += "ACERTOS CORRETOS: \n------------------------\n" 
    String_output += "Verdadeiro Positivo: " + str( MatrizDeConfusao[int(True)][int(True)] ) + "\n"
    String_output += "Verdadeiro Negativo: " + str( MatrizDeConfusao[int(False)][int(False)] ) + "\n"

    String_output += "\n------------------------\nACERTOS INCORRETOS: \n------------------------\n"
    String_output += "Falso negativo: " + str( MatrizDeConfusao[int(True)][int(False)] ) + "\n"
    String_output += "Falso Positivo: " + str( MatrizDeConfusao[int(False)][int(True)] ) + "\n"
    String_output += "\nDADOS\nTotal de unidades: " + str(totalDeItens) + "\n"
    String_output += "Sensitividade: " + str(sen) + "\n"
    String_output += "Especifidade: " + str(esp) + "\n"
    String_output += "Acuracia: " + str(Acc) + "\n"
    String_output += "F1Score: " + str(f1score) + "\n"
    print(String_output)
    exportar_para_txt(String_output, "Resultados matriz.txt")
    pass

def main():
    a = int(input("Verdadeiro positivo: "))
    b = int(input("Verdadeiro negativo: "))
    c = int(input("Falso negativo: "))
    d = int(input("Falso Positivo: "))

    calculo(b,d,c,a)
    pass



if __name__ == "__main__":
    main()