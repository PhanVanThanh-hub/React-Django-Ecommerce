from django.http import HttpResponse

def admin_only(user):
    group = None
    if user.groups.exists():
        group = user.groups.all()[0].name
        print('group', group)

    if group == 'admin':
        print("abc")


