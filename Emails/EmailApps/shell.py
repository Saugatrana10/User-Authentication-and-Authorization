from django.contrib.auth.models import User, Permission

user = User.objects.get(username='saugat')
perm = Permission.objects.get(codename='protected_view')
user.user_permissions.add(perm)