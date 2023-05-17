####### Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho #######
####### em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos   #######
####### para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e   #######
####### de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do #######
####### ano.                                                                                                    #######

####### Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e  #######
####### que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a    #######
####### porcentagem de acordo com cada nível de assinatura.                                                     #######
# --------------------------------------------------//

print(" ******************************************* ")
print(" ********* CÁLCULE O BÔNUS A PAGAR ********* ")
print(" ******************************************* ")

# variáveis das opções de planos
plano_basic = "Basic"
plano_silver = "Silver"
plano_gold = "Gold"
plano_platium = "Platium"

# porcentagem de planos sobre o faturamento
porc_plano_basic = 0.3
porc_plano_silver = 0.2
porc_plano_gold = 0.1
porc_plano_platium = 0.05

assinatura = -1
while assinatura != 4:
    # exibição das opções de planos
    print("Tipos de Assinaturas\n1 - Basic\n2 - Silver\n3 - Gold\n4 - Platium")

    # verifica se a entrada do usuário é um número inteiro
    try:
        assinatura = int(input("Informe sua assinatura: "))
    except ValueError:
        print("Opção inválida. Por favor, digite um número inteiro de 1 a 4.")
        continue

    if assinatura >= 1 and assinatura <= 4:
        # solicitação de faturamento anual
        while True:
            try:
                faturamento_anual = float(input("Informe seu faturamento anual: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
                continue
            else:
                break

        if assinatura == 1:
             bonus_basic = faturamento_anual * porc_plano_basic
             print("Sua assinatura é: {}\nO valor do bônus a ser pago é: R$ {:.2f}". format(plano_basic, bonus_basic))
        elif assinatura == 2:
            bonus_silver = faturamento_anual * porc_plano_silver
            print("Sua assinatura é: {}\nO valor do bônus a ser pago é: R$ {:.2f}". format(plano_silver, bonus_silver))
        elif assinatura == 3:
            bonus_gold = faturamento_anual * porc_plano_gold
            print("Sua assinatura é: {}\nO valor do bônus a ser pago é: R$ {:.2f}". format(plano_gold, bonus_gold))
        elif assinatura == 4:
            bonus_platium = faturamento_anual * porc_plano_platium
            print("Sua assinatura é: {}\nO valor do bônus a ser pago é: R$ {:.2f}". format(plano_platium, bonus_platium))
        break
    else:
        print("Opção inválida. Por favor, digite um número inteiro de 1 a 4.")

