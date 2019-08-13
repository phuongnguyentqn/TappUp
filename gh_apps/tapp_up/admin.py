from django.contrib import admin

from tapp_up import models


class UserAdmin(admin.ModelAdmin):
    pass


class ExpenseAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Grasshopper, UserAdmin)
admin.site.register(models.Expense, ExpenseAdmin)
admin.site.register(models.Category, ExpenseAdmin)
