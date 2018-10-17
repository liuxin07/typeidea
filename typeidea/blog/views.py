# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import Http404

from .models import Post, Tag, Category
from config.models import SideBar
from comment.models import Comment

def post_list(request, category_id=None, tag_id=None):
    queryset = Post.objects.all()

    page = request.GET.get('page', 1)
    page_size = 4

    try:
        page = int(page)

    except TypeError:
        page = 1

    if category_id:
        queryset = queryset.filter(category_id=category_id)

    elif tag_id:

        try:
            tag = Tag.objects.get(id=tag_id)

        except TagDoesNotExist:
            queryset = []

        else:
            queryset = tag.posts.all()

    paginator = Paginator(queryset, page_size)



    try:
        posts = paginator.page(page)

    except:
        posts = paginator.page(paginator.num_pages)


    categories = Category.objects.filter(status=1)

    nav_cates = []
    cates = []
    for cate in categories:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            cates.append(cate)

    sidebars = SideBar.objects.filter(status=1)

    recently_posts = Post.objects.filter(status=1)[:10]
    #hot_posts = Post.objects.filter(status=1).order_by('views')[:10]
    recently_comments = Comment.objects.filter(status=1)[:10]

    context = {
        'posts': posts,
        'nav_cates': nav_cates,
        'cates': cates,
        'sidebars': sidebars,
        'recently_posts': recently_posts,
        'recently_comments': recently_comments,
    }
    return render(request, 'blog/list.html', context=context)

def post_detail(request, pk=None):

    try:
        post = Post.objects.get(pk=pk)

    except DoesNotExist:
        raise Http404('Post does not exist')



    context = {
        'posts': posts,
    }
    return render(request, 'blog/detail.html', context=context)

# Create your views here.
