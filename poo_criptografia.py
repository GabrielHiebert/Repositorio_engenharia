"""Esse módulo contém as classes do problema de criptografia.

Nesse arquivo encontraremos a implementação de três classes: Mensagem, Criptografador, e Interface.

Autores: Gabriel Hiebert e Maria Fernanda Scaburri.
"""

import os
import platform

class Mensagem:
    """Essa classe gerencia as operações com a mensagem.

    Args:
        texto (str): Texto da mensagem digitada pelo usuário.
        nome_arquivo(.txt): Arquivo onde a mensagem é armazenada.
    """
    def __init__(self, texto: str, nome_arquivo: str):
        """Cria as variáveis texto e nome_arquivo. 

        Args:
            texto (str): Texto da mensagem digitada pelo usuário.
            nome_arquivo(.txt): Arquivo onde a mensagem é armazenada.
        """
        self.texto = texto
        self.nome_arquivo = nome_arquivo

    def salvar_mensagem(self):
        """Salva a mensagem no arquivo.
        """
        arquivo = open(self.nome_arquivo, "w")
        arquivo.write(self.texto)
        arquivo.close()

    def recuperar_do_arquivo(self):
        """Recupera a mensagem do arquivo.

        Returns: 
            texto (str): Texto da mensagem digitada pelo usuário.
        """
        arquivo = open(self.nome_arquivo, "r")
        self.texto = arquivo.read()
        arquivo.close()
        return(self.texto)

    def recuperar_mensagem(self, nome_arquivo):
        """Chama a função recuperar_do_arquivo(), que recupera a mensagem do arquivo.

        Args: 
            nome_arquivo: nome_arquivo(.txt): Arquivo onde a mensagem é armazenada.

        Returns: 
            texto (str): Texto da mensagem digitada pelo usuário.
        """
        self.texto = (self.recuperar_do_arquivo())
        return(self.texto)

    def exibir(self):
        """Exibe a mensagem e o nome do arquivo no terminal.
        """
        print("Texto: " + self.texto)
        print("Arquivo: " + self.nome_arquivo)


class Criptografador:
    """Essa classe criptografa e descriptografa a mensagem.

    Args:
        dicionario (dict): Dicionário que substitui as letras do alfabeto português para números binários. 
    """
    def __init__(self):
        """Cria um dicionário substituindo as letras do alfabeto português para números binários. 
        """
        self.dicionario = {'A':'01000001', 'B':'01000010','C':'01000011','D':'01000100','E':'01000101',
            'F':'01000110','G':'01000111','H':'01001000','I':'01001001','J':'01001010','K':'01001011',
            'L':'01001100','M':'01001101','N':'01001110','O':'01001111','P':'01010000','Q':'01010001',
            'R':'01010010','S':'01010011','T':'01010100','U':'01010101','V':'01010110','W':'01010111',
            'X':'01011000','Y':'01011001','Z':'01011010',' ':'00100000',
            'a':'01100001','b':'01100010','c':'01100011','d':'01100100','e':'01100101','f':'01100110',
            'g':'01100111','h':'01101000','i':'01101001','j':'01101010','k':'01101011','l':'01101100',
            'm':'01101101','n':'01101110','o':'01101111','p':'01110000','q':'01110001','r':'01110010',
            's':'01110011','t':'01110100','u':'01110101','v':'01110110','w':'01110111','x':'01111000',
            'y':'01111001','z':'01111010'}

    def criptografar(self, texto:str):
        """Criptografa a mensagem em binário. 

        Args: 
            texto (str): Texto da mensagem digitada pelo usuário.
        
        Returns: 
            mensagem_criptografada (str): Mensagem criptografada.
        """
        lista = []
        for letra in texto:
            transforma_binario = self.dicionario[letra]
            lista.append(transforma_binario)
    
        mensagem_criptografada = ""
        for elemento in lista:
            mensagem_criptografada = mensagem_criptografada + elemento
        return(mensagem_criptografada)
        

    def descriptografar(self, texto: str):
        """Descriptografa a mensagem para o alfabeto português.

        Args: 
            texto (str): Texto da mensagem digitada pelo usuário.
        
        Returns: 
            mensagem_decriptografada (str): Mensagem descriptografada.
        """
        inicio_bits = 0
        fim_bits = 8
        lista = []
        for s in range(0, len(texto), 8):

            for chave, valor in self.dicionario.items():
                fatia_bits = texto[inicio_bits:fim_bits]
                if valor == fatia_bits:
                    transforma_letra = chave
                    lista.append(transforma_letra)
            inicio_bits = inicio_bits + 8
            fim_bits = fim_bits + 8

        mensagem_descriptografada = ""
        for elemento in lista:
            mensagem_descriptografada = mensagem_descriptografada + elemento
        return(mensagem_descriptografada)

class Interface:
    """Essa classe contém a interface com o usuário.
    """
    def __init__(self):
        """Cria as variáveis criptografador e mensagem.

        A variável criptografador contém a classe criptografador().
        """
        self.criptografador = Criptografador()
        self.mensagem = None

    def exibir_mensagem(self):
        """Chama a função exibir() da classe Mensagem, que exibe a mensagem e o nome do arquivo.

        Returns:
            boolean: False se a mensagem for None.
            boolean: True se a mensagem não for None e for exibida.
        """
        #Verifica se a mensagem existe
        if self.mensagem is None:
            print("Nenhuma mensagem detectada...")
            return False
        else:
            self.mensagem.exibir()
            return True
    
    def salvar_mensagem(self):
        """Chama a função salvar_no_arquivo() da classe Mensagem, que salva a mensagem no arquivo.

        Returns:
            boolean: False se a mensagem for None.
            boolean: True se a mensagem não for None e for salva no arquivo.
        """
        #Verifica se a mensagem existe
        if self.mensagem is None:
            print("Nenhuma mensagem carregada")
            return False
        else:
            self.mensagem.salvar_no_arquivo()
            return True

    def exibir_menu(self):
        """Exibe o menu.

        Returns: 
            boolean: False se o usuário quiser parar o programa.
            boolean: True para continuar imprimindo o menu.
        """
        #Limpa o terminal
        system = {
            'Windows':'cls',
            'Linux':'clear',
            'Darwin':'clear'
            }
        clear_command = system[platform.system()]
        os.system(clear_command)
        print("--------------------------------")
        #Verifica se a mensagem existe
        if self.mensagem is None:
            print("Nenhuma mensagem em edição...")
        else:
            self.exibir_mensagem()
        print("--------------------------------")

        print("1 - Criar mensagem")
        print("2 - Recuperar mensagem")
        print("3 - Criptografar mensagem")
        print("4 - Descriptografar mensagem")
        print("5 - Sair")
        
        pergunta_opcao = int(input("Digite a opção que você deseja utilizar: "))
        if pergunta_opcao == 1:
            texto = input("Digite o texto da mensagem: ")
            nome_arquivo = input("Digite o nome do arquivo que você deseja gravar sua mensagem (coloque o .txt): ")
            self.mensagem = Mensagem(texto, nome_arquivo)
            self.salvar_mensagem()
        elif pergunta_opcao == 2:
            nome_arquivo = input("Em qual arquivo sua mensagem estava armazenada? (coloque o .txt): ")
            self.texto = ""
            self.classe_mens = Mensagem(self.texto, nome_arquivo)
            self.mensagem = Mensagem(self.classe_mens.recuperar_mensagem(nome_arquivo), nome_arquivo)
        elif pergunta_opcao == 3:
            self.mensagem.texto = self.criptografador.criptografar(self.mensagem.texto) 
            self.salvar_mensagem()
        elif pergunta_opcao == 4:
            self.mensagem.texto = self.criptografador.descriptografar(self.mensagem.recuperar_do_arquivo())
            self.salvar_mensagem()
        elif pergunta_opcao == 5:
            print("Obrigada por utilizar o programa!")
            return False
        else:
            print("Opção inválida :(")
            input("Pressione uma tecla para continuar ")
        return True

interface = Interface()
while interface.exibir_menu():
    pass