import lxml.etree as etree

# %% datasource class
class Datasource:
    """
    A class for the Tableau Datasources, identified within the xml.
    Property modification capabilities based on tableu document api.

    Attributes with modifier capabilities (set, delete):
        caption (set, delete)

    Sub classes:
        connection
        columns
        groups
    """

    def __init__(self, data_xml):
        # datasource ElementTree pulled from full workbook xml, temporarily choosing 1st
        # eventually, workbook will iterate through [0:XXX] of datasources
        self._datasource_xml = data_xml.xpath('/workbook/datasources/datasource')[0]
        # initialize attributes available in datasource
        self._caption = self._datasource_xml.get('caption', '')
        self._inline = self._datasource_xml.get('inline', '')
        self._name = self._datasource_xml.get('name', '')
        self._version = self._datasource_xml.get('source', '')
        # initialize child elements within datasource
        # build out - do I want to modify all?
        self._connection = None
        self._aliases_enabled = self._datasource_xml.find('aliases').attrib
        # note: check how column vs. column-instance compare
        self._columns = None
        self._groups = None
        # what is this?
        self._extract = None
        self._layout = None
        self._style = None
        self._semantic_values = None
        self._default_sorts = None

    @property
    def caption(self):
        return self._caption

    # allows manipulation of caption in datasource xml
    @caption.setter
    def caption(self, value):
        self._datasource_xml.set('caption', value)
        self._caption = value

    @caption.deleter
    def caption(self):
        del self._datasource_xml.attrib['caption']
        self._caption = None

    @property
    def inline(self):
        return self._inline

    @property
    def name(self):
        return self._name
