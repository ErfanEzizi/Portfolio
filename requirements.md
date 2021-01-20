(most part is already done for you but just incase <3)



First after open folder on your cmd/terminal type :

1."cd Portfolio"

2."python manage.py makemigrations","python manage.py migrate".

3."python manage.py collectstatic"

4.i used django-crispy-forms for the bootsrape compnent so type "pip install django-crispy-forms" and go settings.py in folder Portfolio to add 'crispy-forms' to INSTALLED_APPS.

5."pip install django-filter" and same step as last one go to settings.py and add to INSTALLED_APPS.

6."pip install pillow" for image processing. you dont need to add this to settings.py.

7.Your settings.py should look something like this:

INSTALLED_APPS = [

    'base.apps.BaseConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_filters'
]

8.And for static files and email components:

STATIC_URL = '/static/'

MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'erfanazizitd@gmail.com'

EMAIL_HOST_PASSWORD = 'qsydimasccwxybmm'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

9. Make sure to create a super user to see more featurs of the site "python manage.py createsuperuser"

(IF you have any problems feel free to email me to the address above <3)
