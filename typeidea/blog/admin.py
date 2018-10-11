# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Category, Tag

from typeidea.custom_site import custom_site

from django.utils.html import format_html

from django.core.urlresolvers import reverse
# Register your models here.

@admin.register(Post,site=custom_site)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'owner', 'created_time', 'operator']
    list_filter = ['category', 'owner']
    search_fields = ['title', 'category__name', 'owner__username']
    show_full_result_count = False
    list_display_links = ['category', 'owner', 'title']

    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'created_time'
    #list_editable = ('title', 'status')

    #编辑页面配置
    save_on_top = True
    fields = (
        ('title', 'category'),
        'content'
    )
    exclude = ('owner',)

    '''fieldsets = (  # 跟fields互斥

        ('基础配置', {

            'fields': (('category', 'title'), 'content')

        }),

        ('高级配置', {

            'classes': ('collapse', 'addon'),

            'fields': ('tags',),

        }),

    )
    filter_horizontal = ('tag')
    filter_vertical = ('tags')'''

    #自定义字段展示
    def operator(self, obj):
        return format_html(

            '<a href="{}">编辑</a>',

            reverse('cus_admin:blog_post_change', args=(obj.id,))

        )

    operator.show_description = '操作'
    # operator.allow_tags = True  # 用format_html替代


@admin.register(Category,site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass




