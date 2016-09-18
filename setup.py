from setuptools import setup
setup(
    name='freeq',
    version='0.2.0',
    author='Enaunimes; Scott Ming',
    py_modules=['duplicate'],
    include_package_data=True,
    install_requires=[
        'click', 'image', 'wordcloud',
        'pdfminer.six', 'pandas', 'matplotlib'
    ],
    entry_points='''
        [console_scripts]
        freeq=freeq:cli
    ''',
)
