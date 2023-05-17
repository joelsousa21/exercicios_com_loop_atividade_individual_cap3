
####### Um grande cliente seu sofreu um ataque hacker: o servidor foi sequestrado por um software malicioso que #######
####### criptografou todos os discos e pede a digitação de uma senha para a liberação da máquina. E é claro que #######
####### os criminosos exigem um pagamento para informar a senha.                                                #######

####### Ao analisar o código do programa deles, porém, você descobre que a senha é composta pela palavra        #######
####### “LIBERDADE” seguida do fatorial dos minutos que a máquina estiver marcando no momento da digitação da   #######
####### senha (se a máquina estiver marcando 5 minutos, a senha será LIBERDADE120). Crie um programa que receba #######
####### do usuário os minutos atuais e exiba na tela a senha necessária para desbloqueio. ATENÇÃO: seu programa #######
####### não pode utilizar funções prontas para o cálculo do fatorial. Ele deve obrigatoriamente utilizar loop.  #######
# -----------------------------------------------------------//

# solicita ao usuário os minutos atuais
while True:
    try:
        minutos = int(input("Digite o número de minutos atuais: "))
        if minutos >= 0:
            break
        else:
            print("Valor inválido. Digite um numero inteiro maior ou igual a zero.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro maior ou igual a zero.")

senha = "LIBERDADE"
fatorial = 1

# Calcula o fatorial usando loop
for x in range(1, minutos + 1):
    fatorial *= x

senha += str(fatorial)

print("A senha para desbloqueio é: ", senha)
