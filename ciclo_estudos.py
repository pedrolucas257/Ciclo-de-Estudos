
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
    global tempo_de_estudo_em_horas
    dias = int(input("Quantos Dias você quer estudar por semana: "))
    horas = int(input("Quantas Horas por dia você quer estudar: "))
    calculo_de_tempo = dias * horas
    tempo_de_estudo_em_horas = calculo_de_tempo

def AdicionarTempoDeEstudoACadaMateria():
    total_da_divisao = tempo_de_estudo_em_horas / total_soma_dificuldades
    for i in range(0,len(materias)):
        pass



AdicionarMateriasAoCicloDeEstudos()
AdicionarDificuldadeNaTarefa()
SomarOsValoresDasDificuldades()
CalcularTempoDeEstudoBaseadoEmDiasEHoras()
print(tempo_de_estudo_em_horas)

