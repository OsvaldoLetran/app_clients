from setuptools import setup


setup(
    name = 'app_main',
    version = '0.1',
    py_modules = ['app_main'],
    install_requires = ['Click', ],
    entry_points = """[console_scripts]
    app_main = app_main:cli
    """,
)
