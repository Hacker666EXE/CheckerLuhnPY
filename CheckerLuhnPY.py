import os

# Cores
R = '\033[1;31m'  # Vermelho
G = '\033[1;32m'  # Verde
B = '\033[1;34m'  # Azul
Y = '\033[1;33m'  # Amarelo
RT = '\033[0;1m'  # Reset
C = '\033[1;90m'  # Cinza
W = '\033[0m'     # Branco (Reset)

# Banner
cc = f"""
{C}.-----------------------.
|{RT} {R}elo{B}card        {C}.-----.{RT}{C}|{RT} Autor:   {C}zBLACKHAT
{C}|{RT} {Y}Classic        {C}{C}|{RT}     {C}|{RT}{RT}{C}|{RT} GitHub:  {C}https://github.com/Hacker666EXE
{C}|{RT}                {C}'-----'{RT}{C}|{RT} Email:   {C}zBLACKHAT_OFC@proton.me
{C}|{RT}                       {C}|{RT} Contato: {C}https://t.me/zBL4CKHATOFICIAL
{C}|{RT} 5067 75xx xxxx xxxx   {C}|{RT}
{C}|{RT} {C}09/2024{RT}               {C}|{RT} Verificar,16 Digitos
{C}|{RT} zBLACKHAT      {R}credito{RT}{C}|{RT}        de cartoes!
{C}'-----------------------'
"""

def luhn_check(card_number):
    card_number = str(card_number)
    total = 0
    reverse_digits = card_number[::-1]
    
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    
    return total % 10 == 0

def get_card_type(card_number):
    if card_number.startswith('4'):
        return 'Visa'
    elif card_number.startswith('5'):
        return 'Mastercard'
    elif card_number.startswith('3'):
        if card_number.startswith(('34', '37')):
            return 'American Express'
        return 'Outros'
    elif card_number.startswith('6'):
        return 'Elo'
    return 'Desconhecido'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(cc)

def main():
    while True:
        clear_screen()
        print_banner()
        card_number = input(f"{G}Digite os 16 números do cartão para verificar (ou 'sair' para terminar): {W}")
        if card_number.lower() == 'sair':
            break
        elif card_number.isdigit() and len(card_number) in [13, 15, 16, 19]:
            is_valid = luhn_check(card_number)
            card_type = get_card_type(card_number)
            if is_valid:
                print(f"{G}O cartão {card_number} é válido e do tipo {card_type}.{W}")
            else:
                print(f"{R}O cartão {card_number} é inválido.{W}")
        else:
            print(f"{Y}Por favor, insira um número de cartão válido.{W}")
        input(f"{C}Pressione Enter para continuar...{W}")

if __name__ == "__main__":
    main()
