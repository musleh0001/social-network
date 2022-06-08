from django.contrib import admin
from django.contrib.auth.models import Group, User

from dwitter.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]


# admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Remove 'Group' from admin
admin.site.unregister(Group)
