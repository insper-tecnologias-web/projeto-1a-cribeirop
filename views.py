from utils import load_data, load_template, save_note, build_response
from urllib.parse import unquote_plus

# def index():
#     # Cria uma lista de <li>'s para cada anotação
#     # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
#     note_template = load_template('components/note.html')
#     notes_li = [
#         note_template.format(title=dados['titulo'], details=dados['detalhes'])
#         for dados in load_data('notes.json')
#     ]
#     notes = '\n'.join(notes_li)

#     return load_template('index.html').format(notes=notes).encode()

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            # AQUI É COM VOCÊ
            print(chave_valor)
            chave, valor = chave_valor.split('=')
            params[chave] = unquote_plus(valor)
        save_note(params)

    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    # if not request.startswith('POST'):
        # return build_response(code=303)+load_template('index.html').format(notes=notes).encode()
    return build_response()+load_template('index.html').format(notes=notes).encode()