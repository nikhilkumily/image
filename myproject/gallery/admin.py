# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Gallery, Photos ,UserContinuation
# Register your models here.

admin.site.register(Gallery)
admin.site.register(Photos)
admin.site.register(UserContinuation)