from flask import Flask, render_template, request
from model import produtos

app = Flask(__name__)


@app.route('/') #basicamente paginação
def index():
    pagina = request.args.get('page', 1, type=int) #pegando argumentos da url
    por_pagina = 3
    comeco = (pagina - 1) * por_pagina
    final = comeco + por_pagina
    totalPaginas = (len(produtos)+ por_pagina -1) // por_pagina

    produtosPagina = produtos[comeco:final] #mostra os produtos no intervalo q eu escolhi

    return render_template('index.html', produtosPagina = produtosPagina, produtos = produtos, page = pagina, totalPaginas = totalPaginas) # indo pro html

if __name__ =='__main__':
    app.run(debug=True)