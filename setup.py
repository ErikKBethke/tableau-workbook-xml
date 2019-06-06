from setuptools import setup

setup(name='tableau-workbook-xml',
      version='0.1',
      description='Python manipulation of Tableau workbooks via the XML',
      url='https://github.com/ErikKBethke/tableau-workbook-xml',
      author='ErikKBethke',
      author_email='erik.k.bethke@gmail.com',
      license='MIT',
      packages=['tableau-workbook-xml'],
      install_requires=[
      'lxml'
    ]
)
