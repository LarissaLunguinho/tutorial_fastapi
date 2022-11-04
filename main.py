from fastapi import FastAPI
from rotas import router

app = FastAPI()

@app.get('/')
def get_root():
    return {"mensagem": "api de papeis"}

app.include_router(router, prefix='')

# ---------------------------------------

""" @app.post('/item')
def add_item(item: Item):
    db.append(item)
    return item

@app.get('/item')
def list_item():
    return db

@app.get('/item/valor_total')
def get_valor_total():
    valor_total = sum([item.valor * item.quantidade for item in db])

    return{'valor total': valor_total} """

# ---------------------------------------

""" @app.get('/')
def read_root(user_agent: Optional[str] = Header('123')):
    #header pra atribuir valor padrao
    return{'user-agent':user_agent}

@app.get('/cookie')
def cookie(response: Response):
    response.set_cookie(key='meucookie', value='123456')
    return{'cookie': True}

@app.get('/get-cookie')
def get_cookie(meucookie: Optional[str] = Cookie(None)):
    return {'Cookie': meucookie}

@app.get('/items/{item_id}')
def read_item(item_id: int, p: bool, q: Optional[str] = None):
    return {'item_id': item_id, 'q':q, 'p':p}

@app.post('/item')
def add_item(novo_item: Item, outro_item: Item):
    return [novo_item, outro_item]
 """