import lxml.etree as etree

# %% datasource class
class Datasource:
    """
    A class for the Tableau Datasources, identified within the xml.

    Attributes with modifier capabilities (set, delete):
        caption (set, delete)

    Sub classes:
        connection
        columns
        groups
    """

    def __init__(self, data_xml):
        """
        Constructor. Passes datasource_xml.
        """
        # assign _datasource_xml when _load_datasources is called
        self._datasource_xml = data_xml
        # initialize attributes available in datasource
        self._caption = self._datasource_xml.get('caption', '')
        self._inline = self._datasource_xml.get('inline', '')
        self._name = self._datasource_xml.get('name', '')
        self._version = self._datasource_xml.get('source', '')
        # initialize child elements within datasource
        # build out - do I want to modify all?
        # enable connection once class and method developed fully
        #self._connection = self._load_connnections(self._datasource_xml)
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
        """
        Caption of datasource. Not to be confused with nammed-connection caption.
        """
        return self._caption

    @caption.setter
    def caption(self, value):
        """
        Setter for caption. Can redefine what the workbook's datasource connection is captioned as.
        """
        self._datasource_xml.set('caption', value)
        self._caption = value

    @caption.deleter
    def caption(self):
        """
        Deleter for caption. Entirely removes.
        """
        del self._datasource_xml.attrib['caption']
        self._caption = None

    @property
    def inline(self):
        """
        Returns information about whether the datasource is inline.
        """
        return self._inline

    @property
    def name(self):
        """
        Returns information about the name of the datasource.
        """
        return self._name

''' Enable once connection class developed
    @staticmethod
    def _load_connection(xml):
        """
        Generates connection elements and parses through them on instantiating a datasource
        """
        wb.datasources[0]._datasource_xml.xpath('./connection/*')
        xml.xpath('./connection/')
        # for workbooks with more than one datasource, iterate
        sources = []
        for source in xml.xpath('/workbook/datasources/datasource'):
            ds = Datasource(source)
            sources.append(ds)
            pass
        return  sources
'''
