from setuptools import setup

setup(
    name='pro',
    version='0.1.2',
    author='Gabriel Grant',
    author_email='g@briel.ca',
    py_modules=['pro'],
    scripts = [
        'bin/pro'
    ],
    license='LGPL',
    long_description=open('README.markdown').read(),
)
