from django.core.management.base import BaseCommand
from json import dump
from os import path, mkdir, listdir
# from shutil import copy2, move
from django.conf import settings


JSON_PATH = 'mainapp/json'
if not path.exists(JSON_PATH):
    mkdir(JSON_PATH)


def create_from_json(data):
    with open(path.join(JSON_PATH, 'data.json'), 'w', encoding="utf-8") as f:
        dump(data, f, ensure_ascii=False)
        print('ok')

def open_file():
    with open(path.join(JSON_PATH, 'data.txt'), 'r') as f:
        tehs = f.readlines()
    return tehs


class Command(BaseCommand):
    def handle(self, *args, **options):

        tehnologii = open_file()
        data = []
        for teh in tehnologii:
            line = {}
            teh = teh.replace('\n', '')
            line['name'] = teh
            data.append(line)

        create_from_json(data)

