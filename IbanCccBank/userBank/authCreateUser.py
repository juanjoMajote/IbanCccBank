from django.contrib.auth.models import User

USER_FIELDS = ['username', 'email']

def create_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    fields = dict((name, kwargs.get(name, details.get(name)))
                  for name in backend.setting('USER_FIELDS', USER_FIELDS))
    if not fields:
        return
    username =(fields.get('username'))
    print(fields.get('email'))
    user=User.objects.all().filter(email=fields.get('email'))
    print(user)
    if user[0].username in username:
        fields['username'] = user.username
    if not User.objects.filter(username=fields.get('username'), email=fields.get('email')):
        return
    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }