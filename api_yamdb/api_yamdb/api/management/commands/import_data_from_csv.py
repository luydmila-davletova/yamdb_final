import csv

from django.core.management.base import BaseCommand
from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title
from users.models import User


class Command(BaseCommand):
    help = 'Импорт данных из csv файлов в базу данных'

    def handle(self, *args, **options):
        with open('static/data/genre.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                data = {
                    'pk': row['id'], 'name': row['name'], 'slug': row['slug']
                }
                genre = Genre(**data)
                genre.save()

        with open('static/data/category.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                data = {
                    'pk': row['id'], 'name': row['name'], 'slug': row['slug']
                }
                category = Category(**data)
                category.save()

        with open('static/data/users.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                data = {
                    'pk': row['id'],
                    'username': row['username'],
                    'email': row['email'],
                    'role': row['role'],
                    'bio': row['bio'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                }
                users = User(**data)
                users.save()

        with open('static/data/genre_title.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
#            pk = list()
#            title_id = list()
#            genre_id = list()
            data = {'pk': [], 'title': [], 'genre': []}
            for row in csv_reader:
                data = {
                    'pk': row['id'],
                    'title_id': row['title_id'],
                    'genre_id': row['genre_id'],
                }
                genre_title = GenreTitle(**data)
                genre_title.save()

        with open('static/data/titles.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                data = {
                    'pk': row['id'],
                    'name': row['name'],
                    'year': row['year'],
                    'category_id': row['category'],
                }
                title = Title(**data)
                title.save()

        with open('static/data/review.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                data = {
                    'pk': row['id'],
                    'title_id': row['title_id'],
                    'text': row['text'],
                    'author_id': row['author'],
                    'score': row['score'],
                    'pub_date': row['pub_date'],
                }
                reviews = Review(**data)
                reviews.save()

        with open('static/data/comments.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                data = {
                    'pk': row['id'],
                    'review_id': row['review_id'],
                    'text': row['text'],
                    'author_id': row['author'],
                    'pub_date': row['pub_date'],
                }
                comments = Comment(**data)
                comments.save()
