import strawberry
import typing
import strawberry_django
from . import models
from django.contrib.auth import get_user_model
from strawberry_django import mutations


@strawberry.django.type(models.Blog)
class Blog:
    id: strawberry.auto
    title: strawberry.auto
    author: strawberry.auto


@strawberry_django.input(models.Blog)
class BlogInput:
    id: strawberry.auto
    title: strawberry.auto
    author: strawberry.auto


@strawberry.type
class Query:
    getBlog: Blog = strawberry.django.field()
    getAllBlogs: typing.List[Blog] = strawberry.django.field()


@strawberry.type
class Mutation:
    createBlog: Blog = mutations.create(BlogInput)


schema = strawberry.Schema(query=Query, mutation=Mutation)
