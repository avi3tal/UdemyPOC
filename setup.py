from setuptools import setup

setup(
    name="udemypoc",
    packages=['udemylib'],
    long_description=open('README.rst').read(),
    author='Avi Tal',
    author_email='avi3tal@gmail.com',
    classifiers=['Private :: Do Not Upload'],  # hack to avoid uploading to pypi
    setup_requires=open('requirements.txt').readlines()
)
