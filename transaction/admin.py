from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'nonce', 'type', 'timestamp', 'hash')

admin.site.register(Transaction, TransactionAdmin)


# Register your models here.
