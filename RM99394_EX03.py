####### Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito       #######
####### grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por    #######
####### 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor     #######
####### deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e      #######
####### depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir  #######
####### a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.              #######
####### Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma #######
####### das notas, deve ser exibida uma mensagem no seguinte padrão:                                             #######

####### VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

####### POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.
# --------------------------------------------------//------------------------------------------------------

print("*********************************************************************************************")
print("************************ BEM-VINDO AO PROGRAMA DE LANÇAMENTO DE NOTAS ***********************")
print("*********************************************************************************************")

notas_impares = []
notas_pares = []

# alunos de números ímpares
for x in range (1, 50, 2):
    while True:
        nota = input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.\nPOR FAVOR, INSIRA A NOTA DO ALUNO Nº {}: ".format(x))
        try:
            nota_float = float(nota)
            if 0 <= nota_float <= 10:
                notas_impares.append(nota_float)
                print("****************************************************************")
                break
            else:
                print("Você digitou uma nota inválida, tente novamente (digite uma nota entre 0 e 10).")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")

# alunos de números pares
for y in range (2, 51, 2):
    while True:
        nota = input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.\nPOR FAVOR, INSIRA A NOTA DO ALUNO Nº {}: ".format(y))
        try:
            nota_float = float(nota)
            if 0 <= nota_float <= 10:
                notas_pares.append(nota_float)
                print("****************************************************************")
                break
            else:
                print("Entrada inválida. Insira um número entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Insira um número válido.")

# calcula, exibe a média e o resultado final
media_impares = sum(notas_impares) / len(notas_impares)
media_pares = sum(notas_pares) / len(notas_pares)

print("A MÉDIA DE NOTA DOS ALUNOS ÍMPARES FOI {:.2f}".format(media_impares))
print("A MÉDIA DE NOTAS PARA OS ALUNOS PARES FOI {:.2f}".format(media_pares))

if media_impares > media_pares:
    print("A METADE DOS ALUNOS ÍMPARES TEVE A MAIOR NOTA.")
elif media_pares > media_impares:
    print("A METADE DOS ALUNOS PARES TEVE A MAIOR NOTA.")
else:
    print("AS DUAS METADES TIVERAM A MESMA MÉDIA")