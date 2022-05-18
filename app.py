from bottle import run,jinja2_view,request,response,TEMPLATE_PATH,route
from settings import TEMPLATES

TEMPLATE_PATH.append(TEMPLATES)


@route('/')
@jinja2_view('index.html')
def index():
    info = {'titulo': 'Bienvenido.',
            'contenido':'Esta es tu primera visita'
        }

    num_visitas = request.get_cookie('visitas')
    if num_visitas:
        num_visitas = int(num_visitas) + 1
        info['mensaje'] = f'Has entrado {num_visitas} veces.'
    else:
        num_visitas = 1
        info['mensaje'] = 'Has entrado 1 vez'

    response.set_cookie('visitas',str(num_visitas),samesite=True,secure=True)

    return info

run(host='localhost',port=8000,debug=True,reloader=True)