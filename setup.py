import os
from codecs import open

from setuptools import setup, find_packages


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = __import__('django_exporter').__version__


with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-exporter',
    version=VERSION,
    description='Extensible helper to export Django QuerySets and other data to CSV and Excel.',
    long_description=long_description,
    url='https://github.com/moccu/django-exporter',
    project_urls={
        'Bug Reports': 'https://github.com/moccu/django-exporter/issues',
        'Source': 'https://github.com/moccu/django-exporter',
    },
    author='Moccu GmbH & Co. KG',
    author_email='info@moccu.com',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=['openpyxl'],
    include_package_data=True,
    keywords='django',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
