from django.contrib import admin

from ulsosite.models.budget import Account, Transaction



class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 1
    exclude = ['modified']

class AccountAdmin(admin.ModelAdmin):
    readonly_fields=['balance']
    inlines = [TransactionInline]


#--------Registrations ---------
admin.site.register(Account, AccountAdmin)


