import json

def extract_route(string): # Função que extrai a rota da requisição
    f = string.find('/')
    l = string.find('HTTP')
    return string[f+1:l-1]

def read_file(arquivo): # Função que lê o arquivo do tipo Path e retorna o conteúdo em binário
    with open(arquivo,'rb') as formatado:
        conteudo = formatado.read()
    return conteudo

def load_data(arquivo): # Recebe um arquivo json e devolve o conteúdo em formato de dicionário
    dir = 'data/'+str(arquivo)
    with open(dir,'r') as arquivo_json:
        conteudo = arquivo_json.read()
    dicionario = json.loads(conteudo)
    return dicionario

def load_template(arquivo): # Recebe o nome de um arquivo de template e devolve uma string com o conteúdo desse arquivo
    dir = 'templates/'+str(arquivo)
    with open(dir,'r',encoding='utf-8') as arquivo_html:
        conteudo = arquivo_html.read()
    return conteudo

def save_note(params): # Função que salva uma nova anotação no arquivo json
    notas = load_data("notes.json")
    notas.append(params)

    with open("data/notes.json","w") as arquivo:
        json.dump(notas,arquivo,ensure_ascii=False,indent=4)

def build_response(body='',code=200,reason='OK',headers=''):
    if headers == "":
        response = f"HTTP/1.1 {code} {reason}\n\n{body}"
    else:
        response = f"HTTP/1.1 {code} {reason}\n{headers}\n\n{body}"
    return response.encode()