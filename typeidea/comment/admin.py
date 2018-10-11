
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Comment



# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'nickname', 'content', 'website', 'email', 'created_time']
    list_filter = ['post', 'content']
    search_fields = ['content']
    list_display_links = ['content']


    date_hierarchy = 'created_time'
    # list_editable = ('title', 'status')

    # 编辑页面配置
    save_on_top = True
    '''fields = (
        ('title', 'category'),

        'content'
    )
    exclude = ('owner',)
    '''

    fieldsets = (  # 跟fields互斥

        ('基础配置', {

            'fields': (('post', 'nickname'), 'content')

        }),

    )


# Register your models here.

