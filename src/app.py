import requests

API_URL = "http://127.0.0.1:8000"


# ------ USUARIOS ------
def listar_usuarios():
    resp = requests.get(f"{API_URL}/usuarios")
    if resp.ok:
        for user in resp.json():
            print(f"{user['id']}: {user['nome']} ({user['email']}) - Pontos: {user['pontuacao']}")
    else:
        print("Erro ao buscar usuários.")


def criar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    novo_user = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    resp = requests.post(f"{API_URL}/usuarios", json=novo_user)
    if resp.ok:
        print("Usuário criado com sucesso!")
    else:
        print("Erro ao criar usuário:", resp.json())


def editar_usuario():
    usuario_id = input("ID do usuário: ")
    print("Deixe os campos em branco para não alterar.")
    nome = input("Novo nome: ")
    email = input("Novo email: ")
    senha = input("Nova senha: ")
    nivel = input("Novo nível: ")
    pontuacao = input("Nova pontuação: ")

    novo_user = {}
    if nome: novo_user["nome"] = nome
    if email: novo_user["email"] = email
    if senha: novo_user["senha"] = senha
    if nivel: novo_user["nivel"] = int(nivel)
    if pontuacao: novo_user["pontuacao"] = int(pontuacao)

    resp = requests.put(f"{API_URL}/usuarios/{usuario_id}", json=novo_user)
    if resp.ok:
        print("Usuário atualizado com sucesso!")
    else:
        print("Erro ao editar usuário:", resp.json())


def deletar_usuario():
    usuario_id = input("ID do usuário a deletar: ")
    resp = requests.delete(f"{API_URL}/usuarios/{usuario_id}")
    if resp.ok:
        print(f"Usuário {usuario_id} deletado com sucesso.")
    else:
        print("Erro ao deletar usuário:", resp.json())





# ------ ATIVIDADES ------
def listar_atividades():
    resp = requests.get(f"{API_URL}/atividades")
    for a in resp.json():
        print(f"{a['id']} - {a['nome']} ({a['pontuacao']} pts)")


def criar_atividade():
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    categoria = input("Categoria: ")
    pontuacao = int(input("Pontuação: "))
    atividade = {
        "nome": nome,
        "descricao": descricao,
        "categoria": categoria,
        "pontuacao": pontuacao
    }
    resp = requests.post(f"{API_URL}/atividades", json=atividade)
    print(resp.json())





# ------ DESAFIOS ------

def listar_desafios():
    resp = requests.get(f"{API_URL}/desafios")
    for d in resp.json():
        print(f"{d['id']} - {d['nome']} ({d['status']})")


def criar_desafio():
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    data_inicio = input("Data início (YYYY-MM-DD): ")
    data_fim = input("Data fim (YYYY-MM-DD): ")
    desafio = {
        "nome": nome,
        "descricao": descricao,
        "data_inicio": data_inicio,
        "data_fim": data_fim
    }
    resp = requests.post(f"{API_URL}/desafios", json=desafio)
    print(resp.json())





# ------ MENU PRINCIPAL ------

def menu_usuarios():
    while True:
        print("\n--- Usuários ---")
        print("1. Listar")
        print("2. Criar")
        print("3. Editar")
        print("4. Deletar")
        print("0. Voltar")
        op = input("Escolha: ")
        if op == "1": listar_usuarios()
        elif op == "2": criar_usuario()
        elif op == "3": editar_usuario()
        elif op == "4": deletar_usuario()
        elif op == "0": break
        else: print("Inválido.")


def menu_atividades():
    while True:
        print("\n--- Atividades ---")
        print("1. Listar")
        print("2. Criar")
        print("0. Voltar")
        op = input("Escolha: ")
        if op == "1": listar_atividades()
        elif op == "2": criar_atividade()
        elif op == "0": break
        else: print("Inválido.")


def menu_desafios():
    while True:
        print("\n--- Desafios ---")
        print("1. Listar")
        print("2. Criar")
        print("0. Voltar")
        op = input("Escolha: ")
        if op == "1": listar_desafios()
        elif op == "2": criar_desafio()
        elif op == "0": break
        else: print("Inválido.")


def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Usuários")
        print("2. Atividades")
        print("3. Desafios")
        print("0. Sair")
        op = input("Escolha: ")
        if op == "1": menu_usuarios()
        elif op == "2": menu_atividades()
        elif op == "3": menu_desafios()
        elif op == "0": break
        else: print("Inválido.")


if __name__ == "__main__":
    main()