import csv
from environs import Env


def grava_usuario(nome, email, idade, filename=None):
    env = Env()
    env.read_env()
    filename = filename if filename is not None else env('USUARIOS_FILE')
    with open(filename, 'a') as f:
        csv.DictWriter(
            f, fieldnames=['nome', 'email', 'idade']
        ).writerow({
            'nome': nome,
            'email': email,
            'idade': idade
        })
