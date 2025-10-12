import requests
import json

# URL base da API
BASE_URL = "http://localhost:5000/api"

def testar_api():
    print("=== Testando API de Registro de Usuários ===\n")
    
    # 1. Testar endpoint de teste
    print("1. Testando endpoint de teste...")
    try:
        response = requests.get(f"{BASE_URL}/teste")
        print(f"Status: {response.status_code}")
        print(f"Resposta: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    except Exception as e:
        print(f"Erro: {e}\n")
    
    # 2. Registrar um usuário
    print("2. Registrando usuário...")
    dados_usuario = {
        "nome": "João Silva",
        "curso": "Engenharia de Software"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/registrar", json=dados_usuario)
        print(f"Status: {response.status_code}")
        print(f"Resposta: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
        
        if response.status_code == 201:
            usuario_id = response.json()['usuario']['id']
            print(f"Usuário criado com ID: {usuario_id}\n")
        else:
            usuario_id = 1  # Para testes subsequentes
    except Exception as e:
        print(f"Erro: {e}\n")
        usuario_id = 1
    
    # 3. Registrar outro usuário
    print("3. Registrando segundo usuário...")
    dados_usuario2 = {
        "nome": "Maria Santos",
        "curso": "Ciência da Computação"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/registrar", json=dados_usuario2)
        print(f"Status: {response.status_code}")
        print(f"Resposta: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    except Exception as e:
        print(f"Erro: {e}\n")
    
    # 4. Listar todos os usuários
    print("4. Listando todos os usuários...")
    try:
        response = requests.get(f"{BASE_URL}/usuarios")
        print(f"Status: {response.status_code}")
        print(f"Resposta: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    except Exception as e:
        print(f"Erro: {e}\n")
    
    # 5. Buscar usuário específico
    print(f"5. Buscando usuário com ID {usuario_id}...")
    try:
        response = requests.get(f"{BASE_URL}/usuarios/{usuario_id}")
        print(f"Status: {response.status_code}")
        print(f"Resposta: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    except Exception as e:
        print(f"Erro: {e}\n")
    
    # 6. Atualizar usuário
    print(f"6. Atualizando usuário com ID {usuario_id}...")
    dados_atualizacao = {
        "nome": "João Silva Atualizado",
        "curso": "Engenharia de Software - Especialização"
    }
    
    try:
        response = requests.put(f"{BASE_URL}/usuarios/{usuario_id}", json=dados_atualizacao)
        print(f"Status: {response.status_code}")
        print(f"Resposta: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    except Exception as e:
        print(f"Erro: {e}\n")
    
    # 7. Testar validação (dados inválidos)
    print("7. Testando validação com dados inválidos...")
    dados_invalidos = {
        "nome": "",  # Nome vazio
        "curso": "A"  # Curso muito curto
    }
    
    try:
        response = requests.post(f"{BASE_URL}/registrar", json=dados_invalidos)
        print(f"Status: {response.status_code}")
        print(f"Resposta: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    except Exception as e:
        print(f"Erro: {e}\n")

if __name__ == "__main__":
    print("Para executar este teste, certifique-se de que o servidor Flask está rodando!")
    print("Execute: python usuarios/register.py")
    print("Depois execute: python exemplo_uso_api.py\n")
    
    testar_api()
