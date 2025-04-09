from persistent import Persistent
from persistent.list import PersistentList


class Produto(Persistent):
    def __init__(self, nome, validade, estoque):
        self.nome = nome
        self.validade = validade
        self.estoque = estoque

    def aumentar_Estoque(self, estoque):
        self.estoque += estoque
        self._p_changed = 1

    def diminuir_Estoque(self, estoque):
        self.estoque -= estoque
        self._p_changed = 1

    def checar(self):
        if self.validade < 8:
            print(f'O produto está com uma semana ou menos de validade')
        else: print(f'O produto está com mais de uma semana de validade')

class Carrinhos_Loja(Persistent):
    def __init__(self, carrinho):
        self.carrinho = carrinho
        self.itens_No_Carrinho = PersistentList()


class Loja(Persistent):
    def __init__(self):
        self.Carrinhos = PersistentList()
    
    def adicionar_Item_Carrinho(self, novo_Item):
        self.itens_No_Carrinho.append(novo_Item)
        self._p_changed = 1 
        print("Item adicionado ao carrinho")

    
class Livro_Biblioteca(Persistent):
    def __init__(self, livro, status_Emprestado):
        self.livro = livro
        self.status_Emprestado = status_Emprestado

    
class Registro_Escola(Persistent):
    def __init__(self, aluno, frequencia):
        self.aluno = aluno
        self.frequencia = frequencia
        
        
class Tarefa(Persistent):
    """Representa uma tarefa individual."""

    def __init__(self, descricao, concluida=False):
        """
        Inicializa uma nova tarefa.

        Args:
            descricao (str): A descrição da tarefa.
            concluida (bool): Indica se a tarefa está concluída (padrão: False).
        """
        self.descricao = descricao
        self.concluida = concluida

    def concluir(self):
        """Marca a tarefa como concluída."""
        self.concluida = True

    def reabrir(self):
        """Marca a tarefa como não concluída."""
        self.concluida = False

    def __repr__(self):
        """Retorna uma representação string da tarefa."""
        status = "Concluída" if self.concluida else "Não concluída"
        return f"{self.descricao} - {status}"

class ListaDeTarefas(Persistent):
    """Gerencia uma lista de objetos Tarefa."""

    def __init__(self):
        """Inicializa uma nova lista de tarefas."""
        self.tarefas = PersistentList()

    def adicionar_tarefa(self, descricao):
        """
        Adiciona uma nova tarefa à lista.

        Args:
            descricao (str): A descrição da nova tarefa.
        """
        tarefa = Tarefa(descricao)
        self.tarefas.append(tarefa)
        self._p_changed = 1  # Notifica o ZODB sobre a mudança

    def remover_tarefa(self, indice):
        """
        Remove uma tarefa da lista pelo seu índice.

        Args:
            indice (int): O índice da tarefa a ser removida.
        """
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            self._p_changed = 1  # Notifica o ZODB sobre a mudança
        else:
            print("Índice inválido.")

    def concluir_tarefa(self, indice):
        """
        Marca uma tarefa como concluída pelo seu índice.

        Args:
            indice (int): O índice da tarefa a ser concluída.
        """
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
            self._p_changed = 1  # Notifica o ZODB sobre a mudança
        else:
            print("Índice inválido.")

    def reabrir_tarefa(self, indice):
        """
        Marca uma tarefa como não concluída pelo seu índice.

        Args:
            indice (int): O índice da tarefa a ser reaberta.
        """
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].reabrir()
            self._p_changed = 1  # Notifica o ZODB sobre a mudança
        else:
            print("Índice inválido.")

    def __repr__(self):
        """Retorna uma representação string da lista de tarefas."""
        return "\n".join([str(tarefa) for tarefa in self.tarefas])