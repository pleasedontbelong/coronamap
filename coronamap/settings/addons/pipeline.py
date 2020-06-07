# full configuration https://django-pipeline.readthedocs.io/en/latest/configuration.html
from os.path import dirname, join

INSTALLED_APPS += ('pipeline',)  # NOQA

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'JAVASCRIPT': {
        'main': {
            'source_filenames': (
            ),
            'output_filename': 'js/script.js',
        },
    },
    'STYLESHEETS': {
        'main': {
            'source_filenames': (
            ),
            'output_filename': 'css/main.css',
            'extra_context': {
                'media': 'screen',
            },
        },
    },
    'CSS_COMPRESSOR': None,
    'JS_COMPRESSOR': None,
    'MIMETYPES': (
        ('text/coffeescript', '.coffee'),
        ('text/less', '.less'),
        ('text/javascript', '.js'),
        ('text/x-sass', '.sass'),
        ('text/x-scss', '.scss')
    ),
}
