
materias = []

def AdicionarMateriasAoCicloDeEstudos():
    quantidade_de_materias = int(input("Quantas Matérias você quer adicionar no ciclo de estudos?"))
    for i in range(0, quantidade_de_materias):
        nome_materia = input(f"{i + 1} materia: ")
        materia = {
            "Nome": nome_materia,
            "Dificuldade": 0,
            "Horas": 0
        }
        materias.append(materia)

def AdicionarDificuldadeNaTarefa():
    if len(materias) > 0:
        print("Dificuldades: 1[Otimo], 2[Bom], 3[Ruim], 4[Pessimo]")
        for i in range(0,len(materias)):
            materias[i]["Dificuldade"] = int(input(f"Qual a Dificuldade da Materia {materias[i]['Nome']}: "))

def SomarOsValoresDasDificuldades():
    global total_soma_dificuldades
    total_soma_dificuldades = 0 
    for i in range(0,len(materias)):
        dificuldade_atual = materias[i]["Dificuldade"]
        total_soma_dificuldades += dificuldade_atual

def CalcularTempoDeEstudoBaseadoEmDiasEHoras():
    global calculo_horas_materia
    dias = int(input("Quantos Dias você quer estudar por semana: "))
    horas = int(input("Quantas Horas por dia você quer estudar: "))
    calculo_horas_semanais = dias * horas
    calculo_horas_materia = calculo_horas_semanais / total_soma_dificuldades

def AdicionarHorasDeEstudoACadaMateria():
    for i in range(0,len(materias)):
        materias[i]["Horas"] = round(materias[i]["Dificuldade"] * calculo_horas_materia)

def CriarTabelaDeHorasDeCadaMateria():
    for i in range(0,len(materias)):
        quantidade_de_horas = materias[i]["Horas"]
        quadradinhos = "[]" * quantidade_de_horas
        print(f"{materias[i]['Nome']}: {quadradinhos}")




AdicionarMateriasAoCicloDeEstudos()
AdicionarDificuldadeNaTarefa()
SomarOsValoresDasDificuldades()
CalcularTempoDeEstudoBaseadoEmDiasEHoras()
AdicionarHorasDeEstudoACadaMateria()
CriarTabelaDeHorasDeCadaMateria()
