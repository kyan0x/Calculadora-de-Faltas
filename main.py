try:
    from rich import print
except:
    system('pip install -r requirements.txt')

import ctypes
from os import system, name

class Functions:
    @staticmethod
    def calculoFaltas(aulas, porcentagem):
        aulas_faltantes = aulas * (1 - (porcentagem / 100))
        print(f'Você pode faltar {aulas_faltantes:.1f} dias')
        input('Continuar...')

    @staticmethod
    def verificarSistemaOperacional():
        os = name
        
        if os == 'posix':
            return system('clear')
        
        elif os == 'nt':
            return system('cls && title [BETA] Asterix Software - "Nossas chaves abriram os baús da tecnologia"')
        
        else:
            return '[ERROR] Sistema operacional desconhecido'

    @staticmethod
    def ajustarExibicao():
        largura = 100
        altura = 50
        console_hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.MoveWindow(console_hwnd, 0, 0, largura * 8, altura * 12, True)

class Init:
    @staticmethod
    def menuExibicao1():
        Functions.ajustarExibicao()
        Functions.verificarSistemaOperacional()

        print('\n                     ________________________________________________')
        print('                    /                                                \ ')
        print("                   |    _________________________________________     |")
        print("                   |   |                                         |    |")
        print("                   |   |  C:\\> cat socialmedias.txt              |    |  ┏┓┏┳┓┳┳┳┓┓┏┳┳┓┏┓")
        print("                   |   |                                         |    |  ┗┓ ┃ ┃┃┃┃┗┫┃┃┃┃┓")
        print('                   |   |   [cyan][Twitter][/] @cahh46                     |    |  ┗┛ ┻ ┗┛┻┛┗┛┻┛┗┗┛')
        print('                   |   |   [blue][Discord][/] @satanizaram                |    |  ┳┓┏┓┓┏┏┓')
        print('                   |   |                                         |    |  ┣┫┃┃┗┫┏┛')
        print('                   |   |                                         |    |  ┻┛┗┛┗┛┗┛')
        print('                   |   | Insira o número de dias letivos         |    |')
        print('                   |   |                                         |    |')
        print('                   |   |                                         |    |')
        print('                   |   |                                         |    |')
        print('                   |   |                                         |    |')
        print('                   |   |                                         |    |')
        print('                   |   |_________________________________________|    |')
        print('                   |                                                  |')
        print('                    \_________________________________________________/')
        print('                          \___________________________________/')
        print('                       ___________________________________________')
        print("                    _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_")
        print("                 _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_")
        print("              _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_")
        print("            _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_")
        print("          _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_")
        print("         :-------------------------------------------------------------------------:")
        print("        `---._.-------------------------------------------------------------._.---'\n")
        
        try:
            aulas = int(input('C:\\> '))
            return aulas
        except ValueError:
            print("Por favor, insira um número inteiro.")
            return Init.menuExibicao1()

    @staticmethod
    def menuExibicao2():
        Functions.ajustarExibicao()
        Functions.verificarSistemaOperacional()

        print('\n                     ________________________________________________')
        print('                    /                                                \ ')
        print("                   |    _________________________________________     |")
        print("                   |   |                                         |    |")
        print("                   |   |  C:\\> cat socialmedias.txt              |    |  ┏┓┏┳┓┳┳┳┓┓┏┳┳┓┏┓")
        print("                   |   |                                         |    |  ┗┓ ┃ ┃┃┃┃┗┫┃┃┃┃┓")
        print('                   |   |   [cyan][Twitter][/] @cahh46                     |    |  ┗┛ ┻ ┗┛┻┛┗┛┻┛┗┗┛')
        print('                   |   |   [blue][Discord][/] @satanizaram                |    |  ┳┓┏┓┓┏┏┓')
        print('                   |   |                                         |    |  ┣┫┃┃┗┫┏┛')
        print('                   |   |                                         |    |  ┻┛┗┛┗┛┗┛')
        print('                   |   | Insira a porcentagem de presença que    |    |')
        print('                   |   | você precisa                            |    |')
        print('                   |   |                                         |    |')
        print('                   |   |                                         |    |')
        print('                   |   |                                         |    |')
        print('                   |   |                                         |    |')
        print('                   |   |_________________________________________|    |')
        print('                   |                                                  |')
        print('                    \_________________________________________________/')
        print('                          \___________________________________/')
        print('                       ___________________________________________')
        print("                    _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_")
        print("                 _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_")
        print("              _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_")
        print("            _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_")
        print("          _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_")
        print("         :-------------------------------------------------------------------------:")
        print("        `---._.-------------------------------------------------------------._.---'\n")
        
        try:
            porcentagem = float(input('C:\\> '))
            return porcentagem
        except ValueError:
            print("Por favor, insira uma porcentagem válida.")
            return Init.menuExibicao2()

    @staticmethod
    def menuExibicao3():
        Functions.ajustarExibicao()
        Functions.verificarSistemaOperacional()

        print('\n                     ________________________________________________')
        print('                    /                                                \ ')
        print("                   |    _________________________________________     |")
        print("                   |   |                                         |    |")
        print("                   |   |  C:\\> cat socialmedias.txt              |    |  ┏┓┏┳┓┳┳┳┓┓┏┳┳┓┏┓")
        print("                   |   |                                         |    |  ┗┓ ┃ ┃┃┃┃┗┫┃┃┃┃┓")
        print('                   |   |   [cyan][Twitter][/] @cahh46                     |    |  ┗┛ ┻ ┗┛┻┛┗┛┻┛┗┗┛')
        print('                   |   |   [blue][Discord][/] @satanizaram                |    |  ┳┓┏┓┓┏┏┓')
        print('                   |   |                                         |    |  ┣┫┃┃┗┫┏┛')
        print('                   |   |                                         |    |  ┻┛┗┛┗┛┗┛')
        print('                   |   |           Qual série você está          |    |')
        print('                   |   | Coloque só o número se for ensino médio |    |')
        print('                   |   | coloque "[red]e[/]" no final do número          |    |')
        print('                   |   |                                         |    |')
        print('                   |   |                                         |    |')
        print('                   |   |                                         |    |')
        print('                   |   |_________________________________________|    |')
        print('                   |                                                  |')
        print('                    \_________________________________________________/')
        print('                          \___________________________________/')
        print('                       ___________________________________________')
        print("                    _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_")
        print("                 _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_")
        print("              _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_")
        print("            _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_")
        print("          _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_")
        print("         :-------------------------------------------------------------------------:")
        print("        `---._.-------------------------------------------------------------._.---'\n")
        
        try:
            serie = int(input('C:\\> '))
            return serie
        except ValueError:
            print("Por favor, insira um número inteiro.")
            return Init.menuExibicao3()

    def iniciar(self):
        aulas = self.menuExibicao1()
        porcentagem = self.menuExibicao2()
        serie = self.menuExibicao3()

        Functions.calculoFaltas(aulas, porcentagem)

init_instance = Init()
init_instance.iniciar()