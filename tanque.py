"""Esse módulo tem as classes que representam o problema do tanque."""

import tanque_visual

class Torneira:
    """Essa classe representa uma torneira do mundo real, tendo com atributos a vazão e um nome para identificar ela."""
    def __init__(self, nome: str, vazao: float):
        self.vazao = vazao
        self.nome = nome

    def modificar_nome(self, novo_nome):
        """Modifica o nome da torneira.

        Args: 
            novo_nome (str): Novo nome da torneira.
        """
        self.nome = novo_nome

    def modificar_vazao(self, nova_vazao):
        """Modifica a vazão da torneira.

        Args: 
            nova_vazao (str): Nova vazão da torneira.
        """
        self.vazao = nova_vazao

    def get_vazao(self):
        pass


#classe filha que herda de Torneira
class TorneiraSaida(Torneira):
        
    def __init__(self, nome, vazao):
        super().__init__(nome, vazao)

    def get_vazao(self):
        super().get_vazao()
        return self.vazao * -1

#classe filha que herda de Torneira
class TorneiraEntrada(Torneira):

    def __init__(self, nome, vazao):
        super().__init__(nome, vazao)
    
    def get_vazao(self):
        super().get_vazao()
        return self.vazao * 1



class Tanque:
    """Classe que representa um tanque do mundo real, ele tem como atributos: capacidade_max, capacidade_atual, torneiras_saida e 
    torneiras_entrada.
    """

    def __init__(self, capacidade_maxima, capacidade_atual):
        """Cria uma instância de um objeto da classe Tanque.

        Args:
            capacidade (float): Capacidade atual do tanque.
            capacidade_maxima (float) Capacidade máxima do tanque.
        """
        self.capacidade_maxima = capacidade_maxima
        self.capacidade_atual = capacidade_atual
        
        self.torneiras_saida = []
        self.torneiras_entrada = []


    def instalar_torneira(self, torneira: Torneira, nova_torneira: Torneira):
        """Adiciona uma torneira ao tanque.

            Adiciona uma torneira ao Tanque, ela pode ser de saida ou entrada.
        Args:
            nova_torneira (Torneira): Nova torneira a ser adicionada.
            saida (bool, optional): Indica se a torneira será de entrada ou saída, por padrão é de saida.

        Returns:
            bool: True se a torneira tiver sido instalada com sucesso!
        """
        saida_entrada = str(input("Sua torneira é de saída ou de entrada? (e/s): "))
        saida_entrada.lower()
        if saida_entrada == "s":
            for torneira in self.torneiras_saida:
                if nova_torneira.nome == torneira.nome:
                    print("Torneira já instalada!")
                    return False
            nova_torneira.get_vazao()
            self.torneiras_saida.append(nova_torneira)
            print(f'Nova torneira de saída com o nome {nova_torneira.nome} e vazão {nova_torneira.vazao}/s adicionada com sucesso!')
        
        elif saida_entrada == "e":
            for torneira in self.torneiras_entrada:
                if nova_torneira.nome == torneira.nome:
                    print("Torneira já instalada!")
                    return False
            nova_torneira.get_vazao()
            self.torneiras_entrada.append(nova_torneira)
            print(f'Nova torneira de entrada com o nome {nova_torneira.nome} e vazão {nova_torneira.vazao}/s adicionada com sucesso!')
            return True

        else:
            print("Você digitou um caracter inválido :( ")

    def abrir_torneira(self, torneira: Torneira):
        """Abre uma torneira de entrada ou saída.

        A torneira fica aberta de acordo com o tempo que o usuário solicitar.

        Args: 
            torneira (Torneira): Representa uma torneira com nome, vazão e tipo.

        Returns:
            bool: True se a torneira tiver sido aberta.
        """
        torneira.nome = input("Qual torneira você deseja abrir? ")
        tempo_segundos = float(input("Quantos segundos você deseja deixar ela aberta? "))
        for torneira in self.torneiras_saida:
            if torneira.nome == torneira.nome:
                if self.capacidade_atual >= torneira.vazao*tempo_segundos:
                    self.capacidade_atual -= torneira.vazao*tempo_segundos
                    print("Água retirada do reservatório :)")
                    return True
                else:
                    self.capacidade_atual = 0
                    print("A água acabou antes do tempo :(")
                    return True
        for torneira in self.torneiras_entrada:
            if torneira.nome == torneira.nome:
                if self.capacidade_atual + torneira.vazao*tempo_segundos <= self.capacidade_maxima:
                    self.capacidade_atual += torneira.vazao*tempo_segundos
                    print("Água adicionada ao reservatório :)")
                    return True
                else:
                    self.capacidade_atual = self.capacidade_maxima
                    print("A água acabou transbordando, você desperdiçou água!")
                    return True
        return False

    def recarregar_reservatorio(self):
        """Recarrega o reservatório.

        Returns:
            boolean: False se o tanque estiver cheio e True se ele for recarregado.
        """
        if self.capacidade_atual == self.capacidade_maxima:
            print("O tanque já está cheio!")
            return False
        elif self.capacidade_atual < self.capacidade_maxima:
            self.capacidade_atual = 100
            print("Tanque recarregado com sucesso!")
            return True

    def imprimir_nome_torneiras(self, nova_torneira: Torneira):
        """Imprime o nome das torneiras de entrada e saída existentes.

        Args:
            nova_torneira (Torneira): Representa uma torneira com nome, vazão e tipo.

        Returns:
            boolean: False se a letra digitada não for e ou s.
        """
        pergunta = input("Você deseja imprimir o nome da(s) torneiras(s) de entrada ou saída? (e/s) ")
        if pergunta == "s":
            if self.torneiras_saida == []:
                print("Não há torneiras de saída instaladas!")
            else:
                print("Aqui estão a(s) torneira(s) de saída instalada(s):")
                for i in range(len(self.torneiras_saida)):
                    print("→",self.torneiras_saida[i].nome)
        elif pergunta == "e":
            if self.torneiras_entrada == []:
                print("Não há torneiras de entrada instaladas!")
            else: 
                print("Aqui estão a(s) torneira(s) de entrada instalada(s):")
                for i in range(len(self.torneiras_entrada)):
                    print("→",self.torneiras_entrada[i].nome)
        else: 
            print("Você digitou uma letra inválida!")
            return False
        return True

    def remover_torneira(self, nova_torneira:Torneira):
        """Remove uma torneira de entrada ou saída.

        Args:
            nova_torneira (Torneira): Representa uma torneira com nome, vazão e tipo.

        Returns:
            boolean: False se a torneira for removida ou se não existir uma torneira com o nome informado.
        """
        pergunta_e_s = input("Você deseja remover uma torneira de entrada ou saída? (e/s) ")
        if pergunta_e_s == "s":
            torneira_para_remover = input("Qual torneira de saída você deseja remover? ")
            for i in range(len(self.torneiras_saida)):
                if torneira_para_remover == self.torneiras_saida[i].nome:
                    del(self.torneiras_saida[i])
                    print("Torneira removida!")
                    return False
                else: 
                    print("Não há nenhuma torneira de saída com esse nome!")
                    return False
        elif pergunta_e_s == "e":
            torneira_para_remover = input("Qual torneira de entrada você deseja remover? ")
            for i in range(len(self.torneiras_entrada)):
                if torneira_para_remover == self.torneiras_entrada[i].nome:
                    del(self.torneiras_entrada[i])
                    print("Torneira removida!")
                    return False
                else: 
                    print("Não há nenhuma torneira de entrada com esse nome!")
                    return False
        else: 
            print("Você digitou algo inválido!")
            return False

    def calcular_tempo_esvaziamento(self, nova_torneira: Torneira):
        """Calcula o tempo de esvaziamento do tanque.

        Args:
            nova_torneira (Torneira): Representa uma torneira com nome, vazão e tipo.

        Returns:
            boolean: False se não há torneiras de saída instaladas.
        """
        vazao_das_torneiras = 0
        if self.torneiras_saida == []:
            print("Não é possível calcular o tempo de esvaziamento pois não há torneiras de saída instaladas!")
            return False
        elif self.capacidade_atual == 0:
            print("O tanque já está vazio!")
        else:
            for nova_torneira in self.torneiras_saida:
                vazao_das_torneiras += nova_torneira.vazao
            tempo_de_esvaziamento =  self.capacidade_atual / vazao_das_torneiras
            print("O tempo de esvaziamento é", tempo_de_esvaziamento, "segundos!")

    def atualizar_torneira(self, nova_torneira: Torneira):
        """Atualiza o nome ou a vazão de uma torneira, conforme o usuário quiser.

        Args:
            nova_torneira (Torneira): Representa uma torneira com nome, vazão e tipo.

        Returns:
            boolean: False se o nome ou vazão for atualizado.
            boolean: False se a torneira não existir.
        """
        pergunta_e_s_2 = input("Você deseja atualizar uma torneira de entrada ou saída? (e/s) ")
        if pergunta_e_s_2 == "s":
            pergunta1 = input("Você deseja atualizar o nome ou a vazão da torneira? (n/v) ")
            if pergunta1 == "n":
                pergunta2 = input("Qual o nome da torneira de saída que você deseja atualizar? ")
                for i in range(len(self.torneiras_saida)):
                    if pergunta2 == self.torneiras_saida[i].nome:
                        novo_nome = input("Digite o novo nome da sua torneira de saída: ")
                        self.torneiras_saida[i].modificar_nome(novo_nome)
                        print("Nome atualizado com sucesso!")
                        return False
                    else: 
                        print("Torneira de saída não existente!")
                        return False
            elif pergunta2 == "v":
                pergunta2 = input("Qual o nome da torneira de saída que você deseja atualizar? ")
                for i in range(len(self.torneiras_saida)):
                    if pergunta2 == self.torneiras_saida[i].nome:
                        nova_vazao = input("Digite a nova vazão da sua torneira de saída: ")
                        self.torneiras_saida[i].modificar_vazao(nova_vazao)
                        print("Vazão atualizada com sucesso!")
                        return False
                    else: 
                        print("Torneira de saída não existente!")
                        return False
            elif pergunta2 != "n" and pergunta2 != "v":
                print("Você digitou uma letra inválida!")
                return False
        elif pergunta_e_s_2 != "s" and pergunta_e_s_2 != "e":
            print("Você digitou uma letra inválida!")
            return False

        if pergunta_e_s_2 == "e":
            pergunta1 = input("Você deseja atualizar o nome ou a vazão da torneira? (n/v) ")
            if pergunta1 == "n":
                pergunta2 = input("Qual o nome da torneira de entrada que você deseja atualizar? ")
                for i in range(len(self.torneiras_entrada)):
                    if pergunta2 == self.torneiras_entrada[i].nome:
                        novo_nome = input("Digite o novo nome da sua torneira de entrada: ")
                        self.torneiras_entrada[i].modificar_nome(novo_nome)
                        print("Nome atualizado com sucesso!")
                        return False
                    else: 
                        print("Torneira de entrada não existente!")
                        return False
            elif pergunta2 == "v":
                pergunta2 = input("Qual o nome da torneira de saída que você deseja atualizar? ")
                for i in range(len(self.torneiras_entrada)):
                    if pergunta2 == self.torneiras_entrada[i].nome:
                        nova_vazao = input("Digite a nova vazão da sua torneira de saída: ")
                        self.torneiras_entrada[i].modificar_vazao(nova_vazao)
                        print("Vazão atualizada com sucesso!")
                        return False
                    else: 
                        print("Torneira de entrada não existente!")
                        return False
            elif pergunta2 != "n" and pergunta2 != "v":
                print("Você digitou uma letra inválida!")
                return False
        elif pergunta_e_s_2 != "s" and pergunta_e_s_2 != "e":
            print("Você digitou uma letra inválida!")
            return False

class Interface: 
    """Essa classe realiza a interface com o usuário, tendo com atributos a classe do Tanque e nova_torneira."""
    def __init__(self):
        self.tanque = Tanque(100, 0)
        self.nova_torneira = None

    def exibir_menu(self):
        """Exibe o menu.

        Returns:
            boolean: False se o usuário quiser parar o programa ou digitar uma opção inexistente.
        """
        print("--------------------------------")
        print("\033[1;35mRepresentação do Tanque\033[m")
        tanque_visual.x(self.tanque.capacidade_atual)
        print("--------------------------------")
        print("\033[1;35mMenu\033[m")
        print("O que você deseja fazer?")
        print("1 - Instalar uma nova torneira")
        print("2 - Abrir uma torneira")
        print("3 - Recarregar o reservatório")
        print("4 - Ver o nome das torneiras já existentes")
        print("5 - Remover uma torneira")
        print("6 - Calcular o tempo de esvaziamento")
        print("7 - Atualizar alguma torneira")
        print("8 - Parar o código")
        pergunta_menu = int(input("Qual módulo você deseja utilizar? (Digite apenas números): "))
            
        print()
            
        if pergunta_menu == 1:
            nome = str(input("Qual o nome da torneira? "))
            vazao = float(input("Quantos ml de água deve sair da torneira por segundo? "))
            self.torneira = Torneira(vazao, nome)
            self.nova_torneira = Torneira(nome, vazao)
            self.tanque.instalar_torneira(self.torneira, self.nova_torneira)

        elif pergunta_menu == 2:
            if self.torneira is None:
                print("Não há nenhuma torneira instalada!")
                return False
            self.tanque.abrir_torneira(self.torneira)

        elif pergunta_menu == 3:
            self.tanque.recarregar_reservatorio()
            
        elif pergunta_menu == 4:
            self.tanque.imprimir_nome_torneiras(self.nova_torneira)
            
        elif pergunta_menu == 5:
            self.tanque.remover_torneira(self.nova_torneira)
            
        elif pergunta_menu == 6:
            self.tanque.calcular_tempo_esvaziamento(self.nova_torneira)

        elif pergunta_menu == 7:
            self.tanque.atualizar_torneira(self.nova_torneira)

        elif pergunta_menu == 8:
            print("Obrigada por usar o programa!")
            return False

        else:
            print("Você digitou um módulo inexistente :(")
        return True 

interface = Interface()
while interface.exibir_menu():
    pass