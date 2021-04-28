import os
import platform

class Mensagem:
    def __init__(self, texto: str, nome_arquivo: str):
        self.texto = texto
        self.nome_arquivo = nome_arquivo

    def salvar_no_arquivo(self):
        arquivo = open(self.nome_arquivo, "w")
        arquivo.write(self.texto)
        arquivo.close()

    def recuperar_do_arquivo(self):
        arquivo = open(self.nome_arquivo, "r")
        self.texto = arquivo.read()
        arquivo.close()

    def exibir(self):
        print("texto: " + self.texto)
        print("arquivo: " + self.nome_arquivo)


class Criptografador:
    def __init__(self):
        self.dicionatio = {}

    def codificar(self, mensagem: Mensagem):
        lista = []
        for letra in mensagem:
            transforma_binario = dicionario[letra]
            lista.append(transforma_binario)

        mensagem_criptografada = ""
        for elemento in lista:
            mensagem_criptografada = mensagem_criptografada + elemento
        #manda a mensagem codificada para a função que colocará ela dentro do arquivo
        return(mensagem_criptografada)

    def decodificar(self, mensagem: Mensagem):
        arqu = open(nome_arquivo, "r")
        texto = arqu.read()
        arqu.close()

        inicio_bits = 0
        fim_bits = 8
        lista = []
        for s in range(0, len(texto), 8):

            for chave, valor in dicionario.items():
                fatia_bits = texto[inicio_bits:fim_bits]
                if valor == fatia_bits:
                    transforma_letra = chave
                    lista.append(transforma_letra)
            inicio_bits = inicio_bits + 8
            fim_bits = fim_bits + 8

        mensagem_descriptografada = ""
        for elemento in lista:
            mensagem_descriptografada = mensagem_descriptografada + elemento

        return (mensagem_descriptografada)


class Aplicacao:
    def __init__(self):
        self.criptografador = Criptografador()
        self.mensagem = None

    def criar_mensagem(self):
        texto = input("digite o texto da mensagem: ")
        arquivo = input("digite o arquivo da mensagem: ")
        self.mensagem = Mensagem(texto, arquivo)
        self.salvar_mensagem()

    def exibir_mensagem(self):
        if self.mensagem is None:
            print("nenhuma mensagem carregada")
        else:
            self.mensagem.exibir()
    
    def salvar_mensagem(self):
        if self.mensagem is None:
            print("nenhuma mensagem carregada")
        else:
            self.mensagem.salvar_no_arquivo()

    def recuperar_mensagem(self):
        nome_arquivo = input("informe o nome do arquivo: ")
        # verificar se o arquivo existe...
        self.mensagem = Mensagem("",nome_arquivo)
        self.mensagem.recuperar_do_arquivo()

    def codificar_mensagem(self):
        self.mensagem.texto = self.criptografador.codificar(self.mensagem)
        
    def decodificar_mensagem(self):
        self.mensagem.texto = self.criptografador.decodificar(self.mensagem)

    def exibir_menu(self):
        system = {
            'Windows' : 'cls',
            'Linux' : 'clear',
            'Darwin' : 'clear'
            }
        clear_command = system[platform.system()]
        os.system(clear_command)
        print("--------------------------------")
        if self.mensagem is None:
            print("nenhuma mensagem em edição")
        else:
            self.exibir_mensagem()
        print("--------------------------------")
        print("1 - criar mensagem")
        print("2 - recuperar mensagem ")
        print("3 - codificar mensagem ")
        print("4 - decodificar mensagem ")
        print("5 - sair")
        print("--------------------------------")
        opcao = int(input("opção:"))
        if opcao == 1:
            self.criar_mensagem()
        elif opcao == 2:
            self.recuperar_mensagem()
        elif opcao == 3:
            self.codificar_mensagem()
        elif opcao == 4:
            self.decodificar_mensagem()
        elif opcao == 5:
            return False
        else:
            print("opção inválida")
            input("Pressione uma tecla para continuar")
        return True


app = Aplicacao()
while app.exibir_menu():
    pass
