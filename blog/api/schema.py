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


@strawberry.django.filters.filter(models.Blog)
class BlogFilter:
    id: strawberry.auto


@strawberry_django.input(models.Blog)
class BlogPartialFilter(BlogInput):
    pass


@strawberry.type
class Query:
    getAllBlogs: typing.List[Blog] = strawberry.django.field()
    getBlogByID: Blog = strawberry.django.field()
    # @strawberry.field
    # def get_blog(self, info, blog_id: int) -> Blog:
    #     try:
    #         blog = models.Blog.objects.get(pk=blog_id)
    #         return blog
    #     except models.Blog.DoesNotExist:
    #         raise ValueError(f"Blog with ID {blog_id} does not exist.")


@strawberry.type
class Mutation:
    createBlog: Blog = mutations.create(BlogInput)
    deleteBlogById: typing.List[Blog] = mutations.delete(filters=BlogFilter)
    updateBlogByID: typing.List[Blog] = mutations.update(BlogPartialFilter, filters=BlogFilter)


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

# GET BLOG BY ID
# query {
#   getBlogByID(pk:1) {
#     id
#     title
#     author
#   }
# }

# DELETE BLOG BY ID
# mutation{
#   deleteBlogById(filters:{
#     id:1
#   })
#   {
#     id
#     title
#     content
#   }
# }

# UPDATE BY ID
# mutation{
#   updateBlogByID(filters: {
#     id: 2
#   }data: {
#     title: "Hello Piyush"
#     content: "We did it"
#   }){
#     id
#     content
#     title
#     author
#   }
# }