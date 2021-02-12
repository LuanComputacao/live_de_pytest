import csv
import os
from datetime import datetime
from random import randint

from faker import Faker
from pytest import fixture


@fixture
def usuario_fake():
    def closure():
        fake = Faker()
        return {
            'nome': fake.name(),
            'email': fake.email(),
            'idade': randint(1, 90)
        }

    return closure


@fixture(scope='function')
def arquivo_de_usuarios():
    timestamp = datetime.now().timestamp()
    filename = f'test_usuarios{timestamp}.csv'
    with open(filename, 'w') as f:
        csv.DictWriter(f, fieldnames=['nome', 'email', 'idade']).writeheader()

    yield filename

    os.remove(filename)
