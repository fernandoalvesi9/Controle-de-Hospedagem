# Fernando Alves
# Projeto Final
# Controle de hospedagem
# Cores ANSI

import os

RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[96m"
YELLOW  = "\033[93m"
GREEN   = "\033[92m"
RED     = "\033[91m"
WHITE   = "\033[97m"

#Tabela de diárias
DIARIAS = {
    1: {1: 20.00, 2: 25.00},
    2: {1: 28.00, 2: 34.00},
    3: {1: 35.00, 2: 42.00},
    4: {1: 42.00, 2: 50.00},
    5: {1: 48.00, 2: 57.00},
    6: {1: 53.00, 2: 63.00},}

# Comando para o tipo de Apartamento
TIPOS = {1: "Basic", 2: "Luxo"}

# Comando Limpar Console  

def limpar_console():
    os.system ('cls' if os.name == 'nt' else 'clear')

# Titulo ASCII feito no site: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+Something+&x=none&v=4&h=4&w=80&we=false
def exibir_titulo():
    print(CYAN + BOLD)

    print("================================================================")
    print("  ██████╗ ██████╗ ██╗      ██████╗ ███╗  ██╗██╗ █████╗  ")
    print(" ██╔════╝██╔═══██╗██║     ██╔═══██╗████╗ ██║██║██╔══██╗ ")
    print(" ██║     ██║   ██║██║     ██║   ██║██╔██╗██║██║███████║ ")
    print(" ██║     ██║   ██║██║     ██║   ██║██║╚████║██║██╔══██║  ")
    print(" ╚██████╗╚██████╔╝███████╗╚██████╔╝██║ ╚███║██║██║  ██║ ")
    print("  ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚══╝╚═╝╚═╝  ╚═╝")
    print("================================================================")
    print("      SISTEMA DE CONTROLEE HOSPEDAGEM  ")
    print("       GERENCIA: FERNANDO ALVES    ")
    print("================================================================")
    print(RESET)
    
# Entrada de Nome
def ler_inteiro (Mensagem, Minimo, Maximo):
    while True:
        Valor = input(WHITE + Mensagem + RESET).strip()
        if Valor.isdigit() and Minimo <= int(Valor) <= Maximo:
            return int(Valor)
        print(RED + f" Valor Inválido! Digite um Número entre {Minimo} e {Maximo}." + RESET)

# Validando as Infos
def ler_nome (Mensagem):
    while True:
        Nome = input(WHITE + Mensagem + RESET).strip()
        if Nome and all(c.isalpha() or c.isspace() for c in Nome):
            return Nome
        print(RED + "Nome Inválido! Use apenas Letras." + RESET)

# Entrada de Dados
def entrada_dados():
    print(YELLOW + BOLD + " DADOS DA RESERVA" + RESET)
    print(YELLOW + " " + "---------------------------------------------------------------"  + RESET)
    
    Nome = ler_nome(" Nome do Funcionário:  ")
    Apto = ler_inteiro(" Número do Apartamento: ", 1, 99)
    print(GREEN + " Tipo do Apartamento: 1- Basic | 2- Luxo" + RESET)
    Tipo = ler_inteiro(" Digite o Tipo:  ", 1, 2)
    Pessoas = ler_inteiro(" Quantidade de Pessoas (1 a 6):  ", 1, 6)
    Dias = ler_inteiro (" Dias de Permanencia:  ", 1, 365)
    
    return Nome, Apto, Tipo, Pessoas, Dias
    
# Cálculos

def calcular(Pessoas, Tipo, Dias):
    diaria_por_pessoa = DIARIAS[Pessoas][Tipo]
    total_diaria = diaria_por_pessoa * Pessoas
    total_geral = total_diaria * Dias
    return diaria_por_pessoa, total_diaria, total_geral
    
# Relátorio Final 

def exibir_relatorio(Nome, Apto, Tipo, Pessoas, Dias, diaria_pp, total_dia, total):
    print()
    print(CYAN + BOLD + " " + "===============================================================" + RESET)
    print(CYAN + BOLD +  "      RELATÓRIO DE HOSPEDAGEM"   + RESET)
    print(CYAN + BOLD + " " + "===============================================================" + RESET)
    print(CYAN + f"  {'Funcionário':<22}: " + YELLOW + BOLD + f" {Nome} " + RESET)
    print(CYAN + f"  {'Apartamento N.':<22}: " + WHITE + f" {Apto} " + RESET)
    print(CYAN + f"  {'Tipo do Apartamento':<22}: " + WHITE + f" {Tipo} " + RESET)
    print(CYAN + f"  {'Número de Pessoas':<22}: " + WHITE + f"({Pessoas})" + RESET)
    print(CYAN + f"  {'Dias de Permanencia':<22}: " + WHITE + f" {Dias} " + RESET)
    print(CYAN + " " + "---------------------------------------------------------------" + RESET)
    print(CYAN + f"  {'Diaria por Pessoa':<22}: " + WHITE + f"R$ {diaria_pp:>8.2f}" + RESET)
    print(CYAN + f"  {'Total Diario':<22}: " + WHITE + f"R$ {total_dia:>8.2f}" + RESET)
    print(CYAN + BOLD + " " + "===============================================================" + RESET)
    print(CYAN + BOLD + f"  {'TOTAL A PAGAR':<22}: " + GREEN + BOLD + f"R$ {total:>8.2f}" + RESET)
    print(CYAN + BOLD + " " + "===============================================================" + RESET)
    print()
    print(YELLOW + BOLD+ " Reserva Registrada com Sucesso!" + RESET)
    print(YELLOW + BOLD+ "   UM NOVO LUGAR PARA RELAXAR!" + RESET)
    print()
    
# Final
def main():
    while True:
        limpar_console()
        exibir_titulo()
        Nome, Apto, Tipo, Pessoas, Dias = entrada_dados()
        diaria_pp, total_dia, total = calcular(Pessoas, Tipo, Dias)
        limpar_console()
        exibir_titulo()
        exibir_relatorio(Nome, Apto, Tipo, Pessoas, Dias, diaria_pp, total_dia, total)
        while True:
            Continuar = input(YELLOW + BOLD + " Deseja Registrar outra Reserva? (S/N): " + RESET).strip().upper()
            if Continuar in ("S", "N"):
                break
            print(RED + " Opção Inválida, Digite apenas S ou N." + RESET)
        if Continuar != "S":
            limpar_console()
            print(GREEN + BOLD)
            print("================================================================")
            print("         Sistema Encerrado! Até a Próxima Reserva!              ")
            print("================================================================")
            print(RESET)
            break
    
if __name__ == "__main__":
    main()
    
# Projeto feito por Fernando Alves
