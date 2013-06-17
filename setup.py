import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-spokeaboutus',
    version='0.2',
    packages=['spokeaboutus', 'spokeaboutus.migrations',
              'spokeaboutus.contrib',
              'spokeaboutus.contrib.twitter',
              'spokeaboutus.contrib.facebook',
              'spokeaboutus.contrib.instagram',
              'spokeaboutus.management',
              'spokeaboutus.management.commands'],
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to store and display what social media talk about site',
    long_description=README,
    url='https://github.com/tomaszroszko/django-spokeaboutus',
    author='Tomasz Roszko',
    author_email='tomaszroszko@gmail.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    install_requires = ['facebook-sdk == 0.4.0'],
    dependency_links = [
        "git+https://github.com/tweepy/tweepy.py#tweepy-dev"
    ],
)
