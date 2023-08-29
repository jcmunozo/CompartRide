"""Circles admin"""

# Django
from django.contrib import admin

# Model
from cride.circles.models import Circle

@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    """Circle admin"""
    list_display = (
        'slug_name',
        'name',
        'is_public',
        'verified',
        'is_limited',
        'members_limit'
    )

    search_fields = ('circle__slug_name', 'name')
    list_filter = (
        'is_public',
        'verified',
        'is_limited'
    )

    fieldsets = (
    ('Circle', {
      'fields': (
        ('name', 'slug_name'),
        ('picture'),
        ('about'),
      )
    }),
    ('Stats', {
      'fields': (
        ('rides_taken', 'rides_offered'),
      )
    }),
    ('state', {
      'fields': (
          ('verified'),
          ('is_public'),
          ('is_limited'),
      ),
    }),
    ('members',{
        'fields':(
            ('members_limit'),
        ),
    })
    )

    readonly_fields = ('created', 'modified')

