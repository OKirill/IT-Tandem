from django.core.management.base import BaseCommand
from tagapp.models import Stack
from shutil import copy2, move
from json import load
from os import path, mkdir
from django.conf import settings

JSON_PATH = 'mainapp/json'


def load_from_json():
    with open(path.join(JSON_PATH, 'data.json'), 'r', encoding="utf-8") as file:
        return load(file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = load_from_json()

        for tag in data:
            new_tag = Stack(**tag)
            new_tag.save()
