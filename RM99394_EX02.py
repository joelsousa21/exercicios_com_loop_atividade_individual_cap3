####### Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização #######
####### das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias  #######
####### da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e  #######
####### exiba qual dia foi o escolhido.                                                                          #######
# --------------------------------------------------//

# Função para validação de entrada do usuário

def receber_voto(mensagem):
    while True:
        try:
            voto = int(input(mensagem))
            if voto < 0:
                print("Digite um número inteiro positivo.")
            else:
                return voto
        except ValueError:
            print("Digite um número inteiro positivo.")

print("******************************************************************")
print("******** BEM VINDO À APURAÇÃO DE VOTOS PARA O DIA DA LIVE ********")
print("******************************************************************")

# solicita ao usuário que informe a quantidade de votos para cada dia da semana
seg = receber_voto("Informe a quantidade de votos que teve a SEGUNDA-FEIRA: ")
ter = receber_voto("Informe a quantidade de votos que teve a TERÇA-FEIRA: ")
qua = receber_voto("Informe a quantidade de votos que teve a QUARTA-FEIRA: ")
qui = receber_voto("Informe a quantidade de votos que teve a QUINTA-FEIRA: ")
sex = receber_voto("Informe a quantidade de votos que teve a SEXTA-FEIRA: ")

# verifica qual dia da semana obteve mais votos e o exibe na tela
if seg > ter and seg > qua and seg > qui and seg > sex:
    print("O dia mais votado para realização da live foi SEGUNDA-FEIRA")
elif ter > seg and ter > qua and ter > qui and ter > sex:
    print("O dia mais votado para realização da live foi TERÇA-FEIRA")
elif qua > seg and qua > ter and qua > qui and qua > sex:
    print("O dia mais votado para realização da live foi QUARTA-FEIRA")
elif qui > seg and qui > ter and qui > qua and qui > sex:
    print("O dia mais votado para realização da live foi QUINTA-FEIRA")
elif sex > seg and sex > ter and sex > qua and sex > qui:
    print("O dia mais votado para realização da live foi SEXTA-FEIRA")
else:
    print("Houve empate, procure a coordenação.")

