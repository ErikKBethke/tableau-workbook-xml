from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='tableauxml',
      version='0.1',
      description='Python manipulation of Tableau workbooks via the XML',
      long_description=readme(),
      url='https://github.com/ErikKBethke/tableau-workbook-xml',
      author='ErikKBethke',
      author_email='erik.k.bethke@gmail.com',
      license='MIT',
      test_suite='nose.collector',
      tests_require=['nose'],
      keywords='tableau xml workbook',
      include_package_data=True,
      packages=['tableauxml'],
      install_requires=[
      'lxml',
      'io',
    ],
    zip_safe=False
)
