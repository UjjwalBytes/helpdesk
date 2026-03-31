from django.contrib import admin
from .models import Ticket
from .models import Ticket, FAQ

admin.site.register(FAQ)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'priority', 'created_at')
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description')