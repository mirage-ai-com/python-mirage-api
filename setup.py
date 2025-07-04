# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='mirage-api',
    version='1.9.0',
    author=u'Valerian Saliou',
    author_email='valerian@valeriansaliou.name',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/mirage-ai-com/python-mirage-api',
    license='MIT - http://opensource.org/licenses/mit-license.php',
    description='Mirage API Python wrapper.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
