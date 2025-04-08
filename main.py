from ZODB import FileStorage, DB
from models import ListaDeTarefas
from transaction import commit
import os
import time

def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Função principal para gerenciar a lista de tarefas."""
    # Configuração do banco de dados
    storage = FileStorage.FileStorage('tarefas.fs')
    db = DB(storage)
    connection = db.open()
    root = connection.root

    # Crie uma lista de tarefas se ela não existir
    if not hasattr(root, 'tarefas'):
        root.tarefas = ListaDeTarefas()
        commit()
    else:
        print("Lista de tarefas já existe.")

    # Acessa a lista de tarefas
    lista_de_tarefas = root.tarefas

    # Loop principal do programa
    while True:
        limpar_tela()

        # Exibir lista de tarefas
        if not lista_de_tarefas.tarefas:
            print("\nNão há tarefas.")
        else:
            print("\nTarefas:")
            for indice, tarefa in enumerate(lista_de_tarefas.tarefas):
                print(f"{indice}: {tarefa}")

        # Exibir menu
        print("\n1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Concluir tarefa")
        print("4. Reabrir tarefa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            lista_de_tarefas.adicionar_tarefa(descricao)
            commit()
            print("Tarefa adicionada com sucesso!")
            time.sleep(1)
        elif escolha == '2':
            if not lista_de_tarefas.tarefas:
                print("Não há tarefas para remover.")
                time.sleep(1)
            else:
                try:
                    indice = int(input("\nDigite o índice da tarefa para remover: "))
                    lista_de_tarefas.remover_tarefa(indice)
                    commit()
                    print("Tarefa removida com sucesso!")
                    time.sleep(1)
                except ValueError:
                    print("Índice inválido. Digite um número.")
                    time.sleep(1)
                except IndexError:
                    print("Índice fora do alcance.")
                    time.sleep(1)
        elif escolha == '3':
            if not lista_de_tarefas.tarefas:
                print("Não há tarefas para concluir.")
                time.sleep(1)
            else:
                try:
                    indice = int(input("\nDigite o índice da tarefa para concluir: "))
                    lista_de_tarefas.concluir_tarefa(indice)
                    commit()
                    print("Tarefa concluída com sucesso!")
                    time.sleep(1)
                except ValueError:
                    print("Índice inválido. Digite um número.")
                    time.sleep(1)
                except IndexError:
                    print("Índice fora do alcance.")
                    time.sleep(1)
        elif escolha == '4':
            if not lista_de_tarefas.tarefas:
                print("Não há tarefas para reabrir.")
                time.sleep(1)
            else:
                try:
                    indice = int(input("\nDigite o índice da tarefa para reabrir: "))
                    lista_de_tarefas.reabrir_tarefa(indice)
                    commit()
                    print("Tarefa reaberta com sucesso!")
                    time.sleep(1)
                except ValueError:
                    print("Índice inválido. Digite um número.")
                    time.sleep(1)
                except IndexError:
                    print("Índice fora do alcance.")
                    time.sleep(1)
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")
            time.sleep(1)

    connection.close()

if __name__ == "__main__":
    main()