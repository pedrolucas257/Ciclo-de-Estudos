import datetime as dt 
import mysql.connector
import json

materias = []
ultima_atualizacao = None

with open("config_db.json", "r") as config_file:
    config = json.load(config_file)

# Conectar ao banco de dados usando os dados do JSON
conexao = mysql.connector.connect(
    host=config["host"],
    user=config["user"],
    password=config["password"],
    database=config["database"]
)

if conexao.is_connected():
    print("Conexão estabelecida")

cursor = conexao.cursor()

def CarregarMateriasDoBancoDeDados():
    cursor.execute("SELECT * FROM materias")
    resultados = cursor.fetchall()
    materias.clear()
    for resultado in resultados:
        materia = {
            "Nome": resultado[1],
            "Dificuldade": resultado[2],
            "Horas": resultado[3],
            "Estudadas": resultado[4],
            "Objetivo": resultado[5],
            "Concluida": resultado[6]
        }
        materias.append(materia)

CarregarMateriasDoBancoDeDados()

def AdicionarMateriaAoBancoDeDados(materia):
    sql = """
    INSERT INTO materias (nome, dificuldade, horas, estudadas, objetivo, concluida)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        materia["Nome"],
        materia["Dificuldade"],
        materia["Horas"],
        materia["Estudadas"],
        materia["Objetivo"],
        materia["Concluida"]
    )
    cursor.execute(sql, valores)
    conexao.commit()

def AtualizarMateriaNoBancoDeDados(materia):
    sql = """
    UPDATE materias
    SET dificuldade = %s, horas = %s, estudadas = %s, objetivo = %s, concluida = %s
    WHERE nome = %s
    """
    valores = (
        materia["Dificuldade"],
        materia["Horas"],
        materia["Estudadas"],
        materia["Objetivo"],
        materia["Concluida"],
        materia["Nome"]
    )
    cursor.execute(sql, valores)
    conexao.commit()

def ExcluirMateriaDoBancoDeDados(nome_materia):
    sql = "DELETE FROM materias WHERE nome = %s"
    cursor.execute(sql, (nome_materia,))
    conexao.commit()


def ChecandoDiaDaSemana():
    hoje = dt.datetime.now().date()
    dia_da_semana = hoje.weekday()
    if dia_da_semana == 0 and ultima_atualizacao != hoje:
        for i in range(0,len(materias)):
            materias[i]["Estudadas"] = 0
            #AtualizarMateriaNoBancoDeDados(materias[i])

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
                "Objetivo": objetivo,
                "Concluida": False
            }
            materias.append(materia)
            #AdicionarMateriaAoBancoDeDados(materia)
    else:
        nomedamateria = input("Nome da nova materia: ")
        objetivodamateria = input(f"Qual o objetivo da materia {nomedamateria}: ")
        materia = {
            "Nome": nomedamateria,
            "Dificuldade": 0,
            "Horas": 0,
            "Estudadas": 0,
            "Objetivo": objetivodamateria,
            "Concluida": False
        } 
        materias.append(materia)
        #AdicionarMateriaAoBancoDeDados()

def AdicionarDificuldadeNaMateria():
    if len(materias) > 0:
        print("Dificuldades: 1[Otimo], 2[Bom], 3[Ruim], 4[Pessimo]")
        for i in range(0,len(materias)):
            if materias[i]["Dificuldade"] == 0:
                materias[i]["Dificuldade"] = int(input(f"Qual a Dificuldade da Materia {materias[i]['Nome']}: "))
                #AtualizarMateriaNoBancoDeDados(materias[i])

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
        #AtualizarMateriaNoBancoDeDados(materias[i])

def CriarTabelaDeHorasDeCadaMateria():
    for i in range(0, len(materias)):
        if materias[i]["Concluida"] == False:
            horas_estudadas = materias[i]["Estudadas"]
            horas_totais = materias[i]["Horas"]
            quadradinhos = "[x]" * horas_estudadas + "[]" * (horas_totais - horas_estudadas)
            print(f"{materias[i]['Nome']}: {quadradinhos}")
        else:
            print(f"{materias[i]['Nome']}: Concluída")

def ExibirObjetivos():
    if len(materias) > 0:
        for i in range(len(materias)):
            print(f"{materias[i]['Nome']}: {materias[i]['Objetivo']}")
    else:
        print("Você não tem Materias")

def AdicionarHoraEstudada():
    nome_daMateria = input("Qual o Nome da materia que você quer concluir? ")
    for i in range(0,len(materias)):
        if nome_daMateria == materias[i]["Nome"]:
            if materias[i]["Concluida"] == True:
                print("Você ja conclui todas as Horas dessa materia")
    quantidade_de_horas = int(input("Quantas horas você quer concluir? "))
    for i in range(0,len(materias)):
        if nome_daMateria == materias[i]["Nome"]:
            materias[i]["Estudadas"] = quantidade_de_horas
            #AtualizarMateriaNoBancoDeDados(materias[i])

def AlterarDificuldadeDeMateria():
    nome_materia = input("Qual Materia você quer alterar: ")
    for i in range(0,len(materias)):
        if materias[i]["Nome"] == nome_materia:
            materias[i]["Dificuldade"] = int(input(f"Qual a Dificuldade da Materia {materias[i]['Nome']}: "))
            #AtualizarMateriaNoBancoDeDados(materias[i])

def AlterarHorasDeEstudoDeMateria():
    print("Atenção: Alterar o tempo de estudo de uma materia zera as horas estudadas desta materia automaticamente")
    reposta = int(input("Tem certeza que quer Alterar? [1]- Sim [2]- Não"))
    if reposta == 1:
        nome_materia = input("Qual Materia você quer alterar: ")
        for i in range(0,len(materias)):
            if materias[i]["Nome"] == nome_materia:
                materias[i]["Horas"] = int(input(f"Quantas Horas você quer estudar a Materia {materias[i]['Nome']}: "))
                materias[i]["Estudadas"] = 0
                #AtualizarMateriaNoBancoDeDados(materias[i])

def AlterarObjetivoDaMateria():
    nome_materia = input("Digite o Nome da materia que você quer Alterar: ")
    for i in range(0,len(materias)):
        if materias[i]["Nome"] == nome_materia:
            materias[i]["Objetivo"] = input(f"Qual o objetivo da materia {nome_materia}: ")
            #AtualizarMateriaNoBancoDeDados(materias[i])

def ConcluirObjetivoDaMateria():
    nome_materia = input("Digite o Nome da materia que você quer Concluir: ")
    escolha = int(input("Você quer Alterar o objetivo ou concluir a Materia? [1]- Alterar [2]- Concluir"))
    if escolha == 1:
        AlterarObjetivoDaMateria()
        for i in range(0,len(materias)):
            if materias[i]["Nome"] == nome_materia:
                pass
                #AtualizarMateriaNoBancoDeDados(materias[i])
    else:
        for i in range(len(materias) -1, -1,-1):
            if materias[i]["Nome"] == nome_materia:
                materias.pop(i)
                #ExcluirMateriaDoBancoDeDados(materias[i])

def ExcluirMateria():
    nome_materia = input("Digite o Nome da materia que você quer excluir: ")
    for i in range(0,len(materias)):
        if nome_materia == materias[i]["Nome"]:
            materias.pop(i)
            #ExcluirMateriaDoBancoDeDados(materias[i])
    print(f"Materia Excluida {nome_materia}")



AdicionarMateriasAoCicloDeEstudos()
AdicionarDificuldadeNaMateria()
SomarOsValoresDasDificuldades()
CalcularTempoDeEstudoBaseadoEmDiasEHoras()
AdicionarHorasDeEstudoACadaMateria()
CriarTabelaDeHorasDeCadaMateria()

ativo = True
while (ativo):
    ChecandoDiaDaSemana()
    print("==================== MENU ====================")
    print("1. Adicionar Materia ao Ciclo de Estudos") 
    print("2. Excluir Materia")
    print("3. Exibir Materia")
    print("4. Exibir Objetivos")
    print("5. Alterar Objetivo da materia")
    print("6. Alterar Horas de Estudo de uma materia")
    print("7. Alterar Dificuldade da Materia")
    print("8. Concluir Hora")
    print("9. Concluir Objetivo")
    print("10. Alterar Tempo de Estudo")
    print("11. Sair")
    escolha = int(input("Opção: "))
    print("===============================================")
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
            ExibirObjetivos()
        case 5: 
            AlterarObjetivoDaMateria()
        case 6:
            AlterarHorasDeEstudoDeMateria()
        case 7:
            AlterarDificuldadeDeMateria()
        case 8:
            AdicionarHoraEstudada()
        case 9:
            ConcluirObjetivoDaMateria()
        case 10:
            CalcularTempoDeEstudoBaseadoEmDiasEHoras()
            SomarOsValoresDasDificuldades()
            AdicionarHorasDeEstudoACadaMateria()
        case 11:
            print("Encerrando Sistema")
            cursor.close()
            conexao.close()
            ativo = False
        case _:
            print("Opção Invalida")