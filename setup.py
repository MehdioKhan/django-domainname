import os
from setuptools import find_packages, setup

version = "0.1"
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-domainname',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    license='GNU License',
    description='Domain name model field and form field for Django.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/MehdioKhan/django-domainname',
    author='Mahdi Khanmohammadi',
    author_email='mehdiokhan@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
