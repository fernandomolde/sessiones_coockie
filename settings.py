import os
BASE_DIR = os.path.dirname(__file__)
BD = os.path.join(BASE_DIR, 'sesiones.sqlite')
numero_preguntas = 10

TEMPLATES = os.path.join(BASE_DIR, 'templates')
#STATIC_FILES = os.path.join(BASE_DIR, 'static')