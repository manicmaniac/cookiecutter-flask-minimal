from setuptools import setup


setup(
    name='{{cookiecutter.package}}',
    long_description=open('README.rst').read(),
    version='{{cookiecutter.version}}',
    include_package_data=True,
    zip_safe=False,
    py_modules=['{{cookiecutter.package}}'],
    install_requires=['Flask'],
    test_suite='tests',
)
