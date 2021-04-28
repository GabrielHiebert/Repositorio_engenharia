def tanque_vazio():
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|____________________|")

def tanque_dez():
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|████████████████████|")

def tanque_vinte():
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|████████████████████|")
    print("|████████████████████|")

def tanque_trinta():
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")

def tanque_quarenta():
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")

def tanque_cinquenta():
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")

def tanque_sessenta():
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")

def tanque_setenta():
    print("|                    |")
    print("|                    |")
    print("|                    |")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")

def tanque_oitenta():
    print("|                    |")
    print("|                    |")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")

def tanque_noventa():
    print("|                    |")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")

def tanque_cem():
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")
    print("|████████████████████|")

def x(capacidade_atual):

    if capacidade_atual == 0:
        tanque_vazio()

    elif capacidade_atual > 0 and capacidade_atual <= 10:
        tanque_dez()

    elif capacidade_atual > 10 and capacidade_atual <= 20:
        tanque_vinte()

    elif capacidade_atual > 20 and capacidade_atual <= 30:
        tanque_trinta()
        
    elif capacidade_atual > 30 and capacidade_atual <= 40:
        tanque_quarenta()
        
    elif capacidade_atual > 40 and capacidade_atual <=50:
        tanque_cinquenta()

    elif capacidade_atual > 50 and capacidade_atual <= 60:
        tanque_sessenta()
        
    elif capacidade_atual > 60 and capacidade_atual <= 70:
        tanque_setenta()
        
    elif capacidade_atual > 70 and capacidade_atual <= 80:
        tanque_oitenta()
        
    elif capacidade_atual > 80 and capacidade_atual <= 90:
        tanque_noventa()
        
    elif capacidade_atual > 90 and capacidade_atual <= 100:
        tanque_cem()

    elif capacidade_atual > 100:
        print("O tanque transbordou :(")

    else:
        print("Você digitou um número baixo :(")
