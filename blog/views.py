from django.http import Http404
from django.shortcuts import render
from butter_cms import ButterCMS

client = ButterCMS('3af08233eb3984f6590f8cd06f6eca9b86e95c42')


def home(request, page=1):
    response = client.posts.all({'page_size': 10, 'page': page})
    categories = client.categories.all()
    tags = client.tags.all()

    try:
        recent_posts = response['data']
    except:
        # In the event we request an invalid page number, no data key will exist in response.
        raise Http404('Page not found')

    next_page = response['meta']['next_page']
    previous_page = response['meta']['previous_page']

    return render(request, 'blog/blog_base.html', {
        'recent_posts': recent_posts,
        'next_page': next_page,
        'previous_page': previous_page
    })


def post(request, slug):
    try:
        response = client.posts.get(slug)
    except:
        raise Http404('Post not found')

    post = response['data']
    return render(request, 'blog/blog_post.html', {
        'post': post
    })


# def author(request, slug):
#     response = client.posts.all({'author_slug': slug})
#     recent_posts = response['data']
#
#     return render(request, 'blog/author.html', {
#         'recent_posts': recent_posts
#     })
#
#
# def category(request, slug):
#     response = client.posts.all({'category_slug': slug})
#     recent_posts = response['data']
#
#     return render(request, 'blog/category.html', {
#         'recent_posts': recent_posts
#     })
