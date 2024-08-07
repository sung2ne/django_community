from django.contrib import admin
from board.models import Board

class BoardAdmin(admin.ModelAdmin):   
    list_display = ["title", "created_at", "updated_at"] 
    list_filter = ["created_at"]
    
    search_fields = ["title", "content"]
    
    ordering = ['-created_at']
    
    fieldsets = [
        (
            "제목", 
            {"fields": ["title"]}
        ),
        (
            "내용", 
            {"fields": ["content"]}
        ),
    ]
    
admin.site.register(Board, BoardAdmin)
