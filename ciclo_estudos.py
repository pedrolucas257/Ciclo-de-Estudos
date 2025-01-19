import datetime as dt 

materias = []

def AdicionarMateriasAoCicloDeEstudos():
    if len(materias) == 0:
        quantidade_de_materias = int(input("Quantas Matérias você quer adicionar no ciclo de estudos?"))
        for i in range(0, quantidade_de_materias):
            nome_materia = input(f"{i + 1} materia: ")
            objetivo = input(f"Qual é o Objetivo da Materia {nome_materia}? ")
            materia = {
                "Nome": nome_materia,
                "Dificuldade": 0,
                "Horas": 0,
                "Estudadas": 0,
                "Objetivo": objetivo
            }
            materias.append(materia)
    else:
        nomedamateria = input("Nome da nova materia: ")
        objetivodamateria = input(f"Qual o objetivo da materia {nomedamateria}: ")
        materia = {
            "Nome": nomedamateria,
            "Dificuldade": 0,
            "Horas": 0,
            "Estudadas": 0,
            "Objetivo": objetivodamateria
        } 
        materias.append(materia)

def AdicionarDificuldadeNaMateria():
    if len(materias) > 0:
        print("Dificuldades: 1[Otimo], 2[Bom], 3[Ruim], 4[Pessimo]")
        for i in range(0,len(materias)):
            if materias[i]["Dificuldade"] == 0:
                materias[i]["Dificuldade"] = int(input(f"Qual a Dificuldade da Materia {materias[i]['Nome']}: "))

def SomarOsValoresDasDificuldades():
    global total_soma_dificuldades
    total_soma_dificuldades = 0 
    for i in range(0,len(materias)):
        dificuldade_atual = materias[i]["Dificuldade"]
        total_soma_dificuldades += dificuldade_atual

def CalcularTempoDeEstudoBaseadoEmDiasEHoras():
    global calculo_horas_materia, calculo_horas_semanais
    dias = int(input("Quantos Dias você quer estudar por semana: "))
    horas = int(input("Quantas Horas por dia você quer estudar: "))
    calculo_horas_semanais = dias * horas
    calculo_horas_materia = round(calculo_horas_semanais / total_soma_dificuldades)

def AdicionarHorasDeEstudoACadaMateria():
    calculo_horas_materia = round(calculo_horas_semanais / total_soma_dificuldades)
    for i in range(0,len(materias)):
        materias[i]["Horas"] = materias[i]["Dificuldade"] * calculo_horas_materia

def VerificarQuantidadeDeHorasEstudadasPorMateria(): ##Concertar isso aqui
    quadradinhos = ""
    for i in range(0,len(materias)):
        if materias[i]["Estudadas"] > 0:
            quadradinhos = "[x]" * materias[i]["Estudadas"]
    return quadradinhos


def CriarTabelaDeHorasDeCadaMateria():
    for i in range(0,len(materias)):
        quantidade_de_horas = materias[i]["Horas"] - materias[i]["Estudadas"]
        quadradinhos = "[]" * quantidade_de_horas
        print(f"{materias[i]['Nome']}: {quadradinhos}")

def AdicionarHoraEstudada():
    nome_daMateria = input("Qual o Nome da materia que você quer concluir? ")
    quantidade_de_horas = int(input("Quantas horas você quer concluir? "))
    for i in range(0,len(materias)):
        if nome_daMateria == materias[i]["Nome"]:
            materias[i]["Estudadas"] = quantidade_de_horas

def AlterarDificuldadeDeMateria():
    nome_materia = input("Qual Materia você quer alterar: ")
    for i in range(0,len(materias)):
        if materias[i]["Nome"] == nome_materia:
            materias[i]["Dificuldade"] = int(input(f"Qual a Dificuldade da Materia {materias[i]['Nome']}: "))

def AlterarHorasDeEstudoDeMateria():
    nome_materia = input("Qual Materia você quer alterar: ")
    for i in range(0,len(materias)):
            if materias[i]["Nome"] == nome_materia:
                materias[i]["Horas"] = int(input(f"Quantas Horas você quer estudar a Materia {materias[i]['Nome']}: "))

def AlterarObjetivoDaMateria():
    nome_materia = input("Digite o Nome da materia que você quer Alterar: ")
    for i in range(0,len(materias)):
        if materias[i]["Nome"] == nome_materia:
            materias[i]["Objetivo"] = input(f"Qual o objetivo da materia {nome_materia}: ")

def ConcluirObjetivoDaMateria():
    nome_materia = input("Digite o Nome da materia que você quer Concluir: ")
    escolha = int(input("Você quer Alterar o objetivo ou concluir a Materia? [1]- Alterar [2]- Concluir"))
    if escolha == 1:
        AlterarObjetivoDaMateria()
    else:
        for i in range(0,len(materias)):
            if materias[i]["Nome"] == nome_materia:
                materias.pop(i)

def ExcluirMateria():
    nome_materia = input("Digite o Nome da materia que você quer excluir: ")
    for i in range(0,len(materias)):
        if nome_materia == materias[i]["Nome"]:
            materias.pop(i)
    print(f"Materia Excluida {nome_materia}")



AdicionarMateriasAoCicloDeEstudos()
AdicionarDificuldadeNaMateria()
SomarOsValoresDasDificuldades()
CalcularTempoDeEstudoBaseadoEmDiasEHoras()
AdicionarHorasDeEstudoACadaMateria()
CriarTabelaDeHorasDeCadaMateria()

ativo = True
while (ativo):
    print("==================== MENU ====================")
    print("1. Adicionar Materia ao Ciclo de Estudos") 
    print("2. Excluir Materia")
    print("3. Exibir Materia")
    print("4. Alterar Objetivo da materia")
    print("5. Alterar Horas de Estudo de uma materia")
    print("6. Concluir Hora")
    print("7. Concluir Objetivo")
    print("8. Alterar Tempo de Estudo")
    print("9. Sair")
    escolha = int(input("Opção: "))
    print("================================================")
    match(escolha):
        case 1:
            AdicionarMateriasAoCicloDeEstudos()
            AdicionarDificuldadeNaMateria()
            AdicionarHorasDeEstudoACadaMateria()
            SomarOsValoresDasDificuldades()
            AdicionarHorasDeEstudoACadaMateria()
            CriarTabelaDeHorasDeCadaMateria()
        case 2:
            ExcluirMateria()
            SomarOsValoresDasDificuldades()
            AdicionarHorasDeEstudoACadaMateria()
        case 3:
            CriarTabelaDeHorasDeCadaMateria() 
        case 4: 
            AlterarObjetivoDaMateria()
        case 5:
            AlterarHorasDeEstudoDeMateria()
        case 6: 
            AdicionarHoraEstudada()
        case 7:
            ConcluirObjetivoDaMateria()
        case 8:
            CalcularTempoDeEstudoBaseadoEmDiasEHoras()
            SomarOsValoresDasDificuldades()
            AdicionarHorasDeEstudoACadaMateria()
        case 9:
            print("Encerrando Sistema")
            ativo = False
        case _:
            print("Opção Invalida")