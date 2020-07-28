import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.landlordLetter',
      version='0.01',
      description=(''),
      long_description='# docassemble.landlordLetter\n\n\n\n## Author\n\njrjflei@gmail.com\n\n',
      long_description_content_type='text/markdown',
      author='',
      author_email='jrjflei@gmail.com',
      license='',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['3to2', 'Babel', 'CherryPy', 'Click', 'Cython', 'Flask', 'Flask-Babel', 'Flask-Cors', 'Flask-Login', 'Flask-Mail', 'Flask-SQLAlchemy', 'Flask-SocketIO', 'Flask-User', 'Flask-WTF', 'Jinja2', 'Mako', 'Markdown', 'MarkupSafe', 'Pattern', 'Pillow', 'PyJWT', 'PyLaTeX', 'PyPDF2', 'PySocks', 'PyYAML', 'Pygments', 'Pyphen', 'SQLAlchemy', 'SocksiPy-branch', 'WTForms', 'Werkzeug', 'XlsxWriter', 'airtable-python-wrapper', 'alembic', 'amqp', 'asn1crypto', 'astunparse', 'atomicwrites', 'attrs', 'azure-common', 'azure-nspkg', 'azure-storage', 'backports.csv', 'bcrypt', 'beautifulsoup4', 'billiard', 'bleach', 'blinker', 'boto', 'boto3', 'botocore', 'cachetools', 'celery', 'certifi', 'cffi', 'chardet', 'cheroot', 'convertapi', 'cryptography', 'dnspython', 'docassemble.demo', 'docassemblekvsession', 'docutils', 'docxcompose', 'docxtpl', 'et-xmlfile', 'eventlet', 'fdfgen', 'feedparser', 'future', 'gcs-oauth2-boto-plugin', 'geographiclib', 'geopy', 'google-api-core', 'google-api-python-client', 'google-auth', 'google-auth-httplib2', 'google-auth-oauthlib', 'google-cloud-core', 'google-cloud-storage', 'google-cloud-translate', 'google-i18n-address', 'google-reauth', 'google-resumable-media', 'googleapis-common-protos', 'greenlet', 'grpcio', 'gspread', 'guess-language-spirit', 'httplib2', 'humanize', 'idna', 'importlib-metadata', 'iso8601', 'itsdangerous', 'jaraco.functools', 'jdcal', 'jellyfish', 'jmespath', 'joblib', 'kombu', 'links-from-link-header', 'lxml', 'mdx-smartypants', 'minio', 'mod-wsgi', 'monotonic', 'more-itertools', 'namedentities', 'netifaces', 'nltk', 'numpy', 'oauth2client', 'oauthlib', 'openpyxl', 'ordered-set', 'packaging', 'pandas', 'passlib', 'pathlib', 'pdfminer.six', 'phonenumbers', 'pip', 'pkginfo', 'pluggy', 'ply', 'portend', 'protobuf', 'psutil', 'psycopg2-binary', 'py', 'pyOpenSSL', 'pyPdf', 'pyasn1', 'pyasn1-modules', 'pycountry', 'pycparser', 'pycryptodome', 'pycryptodomex', 'pycurl', 'pyotp', 'pyparsing', 'pypdftk', 'pypng', 'pytest', 'python-dateutil', 'python-docx', 'python-editor', 'python-engineio', 'python-http-client', 'python-ldap', 'python-socketio', 'pytz', 'pyu2f', 'pyzbar', 'qrcode', 'rauth', 'readme-renderer', 'redis', 'repoze.lru', 'requests', 'requests-oauthlib', 'requests-toolbelt', 'retry-decorator', 'rfc3339', 'rsa', 'ruamel.yaml', 'ruamel.yaml.clib', 's3transfer', 's4cmd', 'scikit-learn', 'scipy', 'sendgrid', 'setuptools', 'simplekv', 'six', 'sklearn', 'sortedcontainers', 'soupsieve', 'tailer', 'tempora', 'textstat', 'titlecase', 'tqdm', 'twilio', 'twine', 'tzlocal', 'uWSGI', 'ua-parser', 'uritemplate', 'urllib3', 'us', 'user-agents', 'vine', 'wcwidth', 'webencodings', 'wheel', 'xlrd', 'xlwt', 'zc.lockfile', 'zipp'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/landlordLetter/', package='docassemble.landlordLetter'),
     )

