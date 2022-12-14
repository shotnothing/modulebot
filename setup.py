#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="shotnothing and eeyain",
    author_email='dont@emailme.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="ModuleBot is yet another telegram bot that helps send reminders, announcements and simple answer questions.",
    entry_points={
        'console_scripts': [
            'modulebot=modulebot.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n',
    include_package_data=True,
    keywords='modulebot',
    name='modulebot',
    packages=find_packages(include=['modulebot', 'modulebot.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/shotnothing/modulebot',
    version='0.1.0',
    zip_safe=False,
)
