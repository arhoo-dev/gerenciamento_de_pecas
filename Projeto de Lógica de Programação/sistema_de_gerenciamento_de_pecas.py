"""Este programa é um sistema de controle de qualidade para peças 
produzidas em uma fábrica."""

"""Essa função é responsável por avaliar se uma peça atende aos critérios
de qualidade. Ela recebe o peso, cor e comprimento da peça e retorna uma 
mensagem."""

def avaliar_peca(peso, cor, comprimento):
    motivos = []

    if not (95 <= peso <= 105):
        motivos.append("peso fora da faixa (95g a 105g)")
    if cor.lower() not in ["azul", "verde"]:
        motivos.append("cor inválida (somente azul ou verde)")
    if not (10 <= comprimento <= 20):
        motivos.append("comprimento fora da faixa (10cm a 20cm)")

    if len(motivos) == 0:
        return "aprovada", ""
    else:
        # Junta todos os motivos em uma string só
        return "reprovada", "; ".join(motivos)


"""Essa função é responsável por cadastrar uma nova peça
Solicita ao usuário as informações necessárias para o cadastro da peça."""
    
def cadastrar_peca(pecas, caixa_atual, caixas_fechadas):
    print("\n--- Cadastro de Nova Peça ---")
    id_peca = input("ID da peça: ")
    peso = float(input("Peso (em gramas): "))
    cor = input("Cor (azul ou verde): ")
    comprimento = float(input("Comprimento (em cm): "))

    status, motivo = avaliar_peca(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": status,
        "motivo_reprovacao": motivo
    }

    pecas.append(peca)

    # Se for aprovada, enviar para o controle de caixas
    if status == "aprovada":
        adicionar_em_caixa(peca, caixa_atual, caixas_fechadas)

    print(f"\nPeça {id_peca} cadastrada como {status.upper()}.")
    if motivo:
        print("Motivo(s) da reprovação:", motivo)

 
"""Essa função é responsável por adicionar uma peça aprovada à caixa atual.
Ela verifica se a caixa atingiu a capacidade máxima de 10 peças. Se sim, a 
caixa é fechada e uma nova caixa é iniciada.""" 
        
def adicionar_em_caixa(peca, caixa_atual, caixas_fechadas):
    caixa_atual.append(peca)

    if len(caixa_atual) == 10:
        print("\n>>> Caixa atingiu capacidade máxima (10 peças). Fechando caixa...")
        caixas_fechadas.append(caixa_atual.copy())
        caixa_atual.clear()
        
"""Essa função é responsável por listar todas as peças aprovadas no 
sistema."""
    
def listar_pecas_aprovadas(pecas):
    print("\n--- Peças Aprovadas ---")
    encontradas = False
    for peca in pecas:
        if peca["status"] == "aprovada":
            encontradas = True
            print(f"ID {peca['id']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
    if not encontradas:
        print("Nenhuma peça aprovada encontrada.")

"""Essa função é responsável por listar todas as peças reprovadas no
sistema."""
        
def listar_pecas_reprovadas(pecas):
    print("\n--- Peças Reprovadas ---")
    encontradas = False
    for peca in pecas:
        if peca["status"] == "reprovada":
            encontradas = True
            print(f"ID {peca['id']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
            print(f"Motivo(s) da reprovação: {peca['motivo_reprovacao']}")
    if not encontradas:
        print("Nenhuma peça reprovada encontrada.")


"""Essa função é responsável por exibir um menu para o usuário escolher como deseja listar as peças cadastradas, permitindo listar apenas as 
aprovadas, apenas as reprovadas ou todas as peças de uma vez."""
        
def menu_listar_pecas(pecas):
    while True:
        print("\n--- Listar Peças ---")
        print("1. Listar peças aprovadas")
        print("2. Listar peças reprovadas")
        print("3. Listar todas as peças")
        print("0. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_pecas_aprovadas(pecas)
        elif opcao == "2":
            listar_pecas_reprovadas(pecas)
        elif opcao == "3":
            listar_pecas_aprovadas(pecas)
            listar_pecas_reprovadas(pecas)
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida. Tente novamente.")

"""Essa função é responsável por remover uma peça cadastrada no sistema,
solicitando ao usuário o ID da peça a ser removida. Ela remove a peça da 
lista geral de peças e, se a peça for aprovada, também a remove da caixa 
atual ou das caixas fechadas onde ela possa estar presente."""
            
def remover_peca(pecas, caixa_atual, caixas_fechadas):
    print("\n--- Remover Peça Cadastrada ---")
    id_peca = input("Digite o ID da peça a ser removida: ")
    
    #Remover da lista geral de peças
    peca_encontrada = None
    for peca in pecas:
        if peca["id"] == id_peca:
            peca_encontrada = peca
            break
    
    if peca_encontrada is None:
        print(f"\nPeça com ID {id_peca} não encontrada.")
        return
    
    pecas.remove(peca_encontrada)
    
    #Se aprovada, remover da caixa
    if peca_encontrada["status"] == "aprovada":
        caixa_atual.remove(peca_encontrada)
        
    for caixa in caixas_fechadas:
        if peca_encontrada in caixa:
            caixa.remove(peca_encontrada)
            
    print(f"\nPeça com ID {id_peca} removida com sucesso.")
    
"""Essa função é responsável por listar todas as caixas que foram fechadas,
mostrando as peças contidas em cada caixa."""    

def listar_caixas_fechadas(caixas_fechadas):
    print("\n--- Caixas Fechadas ---")
    if len(caixas_fechadas) == 0:
        print("Nenhuma caixa foi fechadas ainda.")
        return
    
    for indice, caixa in enumerate(caixas_fechadas, start = 1):
        print(f"\nCaixa {indice}:")
        print(f"Quantidade de peças: {len(caixa)}")
        ids = [peca["id"] for peca in caixa]
        print("IDs das peças:", ", ".join(ids))
        
        
def gerar_relatorio(pecas, caixas_fechadas, caixa_atual):
    print("\n--- Relatório Final ---")
    
    total_aprovadas = sum(1 for peca in pecas if peca["status"] == "aprovada")
    total_reprovadas = sum(1 for peca in pecas if peca["status"] == "reprovada")
    
    print(f"Total de peças cadastradas: {len(pecas)}")
    print(f"Total de peças aprovadas: {total_aprovadas}")
    print(f"Total de peças reprovadas: {total_reprovadas}")
    
    if total_reprovadas > 0:
        print("\nMotivos de Reprovação:")
        for peca in pecas:
            if peca["status"] == "reprovada":
                print(f"ID {peca['id']}: {peca['motivo_reprovacao']}")
                
    qtd_caixas = len(caixas_fechadas)
    if len(caixa_atual) > 0:
        qtd_caixas += 1
        
    print(f"\nQuantidade de caixas utilizadas: {qtd_caixas}")
    print(f"Quantidade de caixas fechadas: {len(caixas_fechadas)}")
    print(f"Peças na caixa atual (aberta): {len(caixa_atual)}")

"""A função exibir_menu é responsável por mostrar as opções disponíveis 
para o usuário no sistema de controle de qualidade. Ela apresenta um menu
com as seguintes opções:

1. Cadastrar nova peça: Permite ao usuário cadastrar uma nova peça, 
solicitando informações como ID, peso, cor e comprimento.

2. Listar peças aprovadas/reprovadas: Exibe uma lista de todas as peças 
cadastradas, indicando se foram aprovadas ou reprovadas, juntamente com 
as razões de reprovação, se aplicável.

3. Remover peça cadastrada: Permite ao usuário remover uma peça específica
do sistema, solicitando o ID da peça a ser removida.

4. Listar caixas fechadas: Exibe uma lista de todas as caixas que foram 
fechadas, mostrando as peças contidas em cada caixa.

5. Gerar relatório final: Gera um relatório final com um resumo das peças
cadastradase das caixas fechadas, incluindo estatísticas como o número 
total de peças, número de peças aprovadas e reprovadas, e o número de 
caixas fechadas.

0. Sair: Encerra o programa."""
        
def exibir_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")
    
    
def main():
    pecas = []
    caixas_fechadas = []
    caixa_atual = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_peca(pecas, caixa_atual, caixas_fechadas)
        elif opcao == "2":
            menu_listar_pecas(pecas)
        elif opcao == "3":
            remover_peca(pecas, caixa_atual, caixas_fechadas)
        elif opcao == "4":
            listar_caixas_fechadas(caixas_fechadas)
        elif opcao == "5":
            gerar_relatorio(pecas, caixas_fechadas, caixa_atual)
        elif opcao == "0":
            print("\nEncerrando o programa...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

