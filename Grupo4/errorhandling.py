import json

def e400():
    return json.dumps({"code": 400,
                       "description": "os campos não foram preenchidos corretamente"}, ensure_ascii=False)
def e401():
    return json.dumps({"code": 401,
                       "description": "usuáro não existe"}, ensure_ascii=False)

def e405():
    return json.dumps({"code": 405,
                       "description": "método de request não aceito"}, ensure_ascii=False)
def e500(msg=""):
    return json.dumps({"code": 500,
                       "description": "erro no banco de dados " + msg}, ensure_ascii=False)