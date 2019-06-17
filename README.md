# tableau-workbook-xml

## Python manipulation of Tableau workbooks via the XML
tableauxml is designed to enable a more efficient method of modifying the various components of the Tableau workbook via XML.

As there are existing ways to read Tableau workbooks via the API, this package is aimed at increasing the ability to efficiently parse through the XML format of workbooks. For example, this package aims to allow you to modify data sources and not run into internal errors when doing so. This functionality does not exist to my knowledge elsewhere.

A large thank you to Tableau themselves for publishing their [document api](http://tableau.github.io/document-api-python/docs/), which gave some inspiration on how to structure this package.

_Note: While this package is public, it is in its initial development. Please do not expect full functionality, as it is a continual work in progress. Updates will be committed as soon as they are in relatively functional states. Again, this package is in INITIAL STAGES.

## Installation
Currently, the easiest way to install is from its ([source](https://github.com/ErikKBethke/tableau-workbook-xml)) on Github:

`pip install git+https://github.com/ErikKBethke/tableau-workbook-xml`

### Requirements
This package has dependencies on the following (included in setup.py):
* lmxl

### Limitations
Currently, this package is only designed to work with Tableau unpackaged workbooks that have excel-direct connections. You may attempt to access workbooks in other formats, but success may be limited. Development is in progress to build out additional access capabilities.

To get started:
```python
from tableauxml import Workbook

wb = Workbook('Workbook.twb')
```
From there, reference the [Wiki]() for better understanding of what attributes and functions can be used.
_Note: the Wiki has not yet been developed_
