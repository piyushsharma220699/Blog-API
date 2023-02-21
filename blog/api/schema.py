import strawberry
import typing
import strawberry_django
from . import models
from strawberry_django import mutations


@strawberry.django.type(models.Blog)
class Blog:
    id: strawberry.auto
    title: strawberry.auto
    content: strawberry.auto
    author: strawberry.auto
    created_at: strawberry.auto
    updated_at: strawberry.auto


@strawberry_django.input(models.Blog)
class BlogInput:
    id: strawberry.auto
    title: strawberry.auto
    content: strawberry.auto
    author: strawberry.auto
    created_at: strawberry.auto
    updated_at: strawberry.auto


@strawberry.type
class Query:
    getAllBlogs: typing.List[Blog] = strawberry.django.field()


@strawberry.type
class Mutation:
    createBlog: Blog = mutations.create(BlogInput)


schema = strawberry.Schema(query=Query, mutation=Mutation)

# ADD A BLOG
#     mutation {
#       createBlog(data:{
#             title: "Wings of Fire"
#             content: "The Best Book Ever"
#             author: "APJ Abdul Kalam"
#         })
#         {
#             id
#             title
#             content
#             author
#             createdAt
#             updatedAt
#         }
#     }

# GET ALL BLOGS
# query {
#   getAllBlogs {
#     id
#     title
#     content
#     author
#     createdAt
#     updatedAt
#   }
# }
