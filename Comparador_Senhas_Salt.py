import time # Importa a biblioteca tempo para calcular o tempo necessário para realizar uma operação

# Função que recebe dois arquivos .txt e compara cada linha para encontrar hashs iguais

def comparador(nome1): # Função que recebe um arquivo .txt e compara cada linha com os dicionários salvos para encontrar hashs iguais

    with open(nome1, "r") as arquivo2: # Abrir o arquivo onde os usuários estão salvos
        for linha in arquivo2: # Para cada linha do arquivo com os usuários
            nome, email_salvo, saltedSenha_salvo, hash_senha_salvo = linha.strip().split(",") # Tranforma a linha em um array, cada elemento dentro do array é separado por vírgula
            nome2 = saltedSenha_salvo + ".txt" # Cria uma variável com o salt de cada usuário + .txt
            with open(nome2, "r") as arquivo: # Abrir o arquivo onde cada dicionário com as senhas geradas estão
                    for linha2 in arquivo: # Para cada linha do aquivo com as senhas
                        salt_salvo,senha,hash_senha_salvo_2 = linha2.strip().split(",") # Tranforma a linha em um array, cada elemento dentro do array é separado por vírgula
                        if salt_salvo == saltedSenha_salvo: # Caso os saltes sejão iguais 
                            if hash_senha_salvo_2 == hash_senha_salvo: # Verifica se o hash salvo na linha usuário é igual ao hash da linha com as senhas geradas
                                print("Senha encontrada!")
                                print("Email:", email_salvo, "Senha:", senha) # Imprimi na tela o Email salvo no arquivo dos usuarios e a senha salva no arquivo senhas geradas

# Menu principal

while True:
    print("Bem vindo ao comparador de senhas!")
    print("Digite 1 para comparar as senhas.")
    print("Digite 2 para sair.")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome1 = input("Digite o nome do arquivo com os dados do cadastro salvo (Lembre de digitar a extensão .txt no fim):")
        inicio = time.time() # Função para marcar o início do processo de geração de senhas
        comparador(nome1) # Compara as linhas do arquivo nome1 com os dicionários salvos
        fim = time.time() # Função para marcar o fim do processo de geração de senhas
        tempo_total = fim - inicio # Calculo para o tempo total do processo de geração de senhas
        print("Tempo de execução: {:.2f} segundos".format(tempo_total)) # Imprimi quanto tempo levou para gerar as senhas
    elif opcao == "2":
        break # Finaliza o programa
    else:
        print("Opção inválida. Tente novamente.")
