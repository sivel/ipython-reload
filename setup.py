from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ipython-reload',
    version='0.0.1',
    description='IPython magic command to reload modules on demand',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sivel/ipython-reload',
    author='Matt Martz',
    author_email='matt@sivel.net',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='ipython magic',
    py_modules=['ipython_reload'],
    python_requires='>=3.5, <4',
    project_urls={
        'Bug Reports': 'https://github.com/sivel/ipython-reload/issues',
        'Source': 'https://github.com/sivel/ipython-reload/',
    },
)
