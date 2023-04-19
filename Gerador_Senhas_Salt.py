import random # Importa a biblioteca para escolher numeros, letras e caracteres aleatórios
import string # Importa a biblioteca que contém um conjunto de strings, maiúsculas, minúsculas, digitos...
import hashlib # Importa a biblioteca necessária para gerar o SHA512
import time # Importa a biblioteca tempo para calcular o tempo necessário para realizar uma operação

punctuation = '#$%^&*()[/\\]' # Define os caracteres especiais aceitos na senha

# Função para criar hash da senha

def criar_hash(senha):
    return hashlib.sha512(senha.encode('utf-8')).hexdigest() # Converte uma senha em hash

# Função para salvar as senhas, recebe o nome do arquivo que será salvo, o tamanho da senha e a quantidade de senhas

def salvar_senhas(dicionario):

    with open("usuarios.txt", "r") as arquivo5: # Abrir o arquivo usuarios.txt em formato de leitura
        for linha in arquivo5: # Para cada linha do aquivo cria uma variavel string com o Salted salvo do usuário + .txt
            nome_salvo, email_salvo, saltedSenha_salvo, hash_senha_salvo = linha.strip().split(",")
            arquivo6 = saltedSenha_salvo + ".txt"
            with open(dicionario, "r") as arquivo2: # Abrir o arquivo com o dicionario de senhas informado pelo usuário no inicío da aplicação em formato de leitura
                for linha in arquivo2: # Para cada linha do aquivo uma senha é selecionada
                    senha_salvo = linha.strip()
                    with open(arquivo6, 'a') as f: # Abrir/Criar o arquivo com o nome da variável criada anteriormente em formato de append (adicionar)                     
                        senha = saltedSenha_salvo + senha_salvo # Adiciona o salted do dicionário com a senha do arquivo usuários.txt 
                        hash_senha = criar_hash(senha) # Calcula o hash dessa senha
                        f.write(f"{saltedSenha_salvo},{senha_salvo},{hash_senha}\n") # Escreve o salted do usuário, a senha do dicionário e o hash do salt+senha
                                

# Função para gerar todas as senhas desejadas

def gerar():

    dicionario = input('Digite o nome do arquivo com o dicionário de senhas("lembre de digitar .txt no final"):')
    
    inicio = time.time() # Função para marcar o início do processo de geração de senhas
    salvar_senhas(dicionario) # Gera todas as senhas do dicionário com os salts de cada usuário e salva em x arquivos, onde x é a quantidade de usuários, cada arquivo terá como nome o salt de cada usuário
    fim = time.time() # Função para marcar o fim do processo de geração de senhas
    tempo_total = fim - inicio # Calculo para o tempo total do processo de geração de senhas
    print("Tempo de execução: {:.2f} segundos".format(tempo_total)) # Imprimi quanto tempo levou para gerar as senhas


# Menu principal

while True:
    print("Bem vindo ao gerador de senhas!")
    print("Digite 1 para gerar senhas.")
    print("Digite 2 para sair.")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        gerar() # Função para gerar todas as senhas desejadas
    elif opcao == "2":
        break # Finaliza o programa
    else:
        print("Opção inválida. Tente novamente.")

