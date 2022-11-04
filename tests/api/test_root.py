from fastapi.testclient import TestClient

def test_get_root(client: TestClient) -> None: #declarando o tipo do client
    response = client.get('/')
    body = response.json()
    #assert verifica se os valores bate, caso sim ele nao faz nada
    # caso nao, ele avisa o erro
    assert response.status_code == 200
    assert body['mensagem'] == 'api de papeis'