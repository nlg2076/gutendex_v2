import os
import json
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Load initial data from index.json'

    def handle(self, *args, **kwargs):
        index_file_path = '/app/catalog_files/index.json'
        with open(index_file_path, 'r') as f:
            data = json.load(f)
            for item in data:
                Book.objects.create(
                    title=item['title'],
                    author=item['author'],
                    published_date=item['published_date'],
                    isbn=item['isbn'],
                    page_count=item['page_count'],
                    cover=item['cover'],
                    language=item['language']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))
