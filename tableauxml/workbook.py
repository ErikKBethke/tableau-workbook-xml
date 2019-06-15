import lxml.etree as etree

from tableauxml import Datasource
# %%
class Workbook:
    """
    A class for the Tableau Workbook, which can be read due to its xml formatting.
    """

    def __init__(self, filepath, encoding='utf-8'):
        self._filepath = filepath
        self.encoding = encoding
        self._xml = self._load_xml(self._filepath)
        self._datasources = self._load_datasources(self._xml)

    @property
    def filepath(self):
        return self._filepath

    @property
    def datasources(self):
        return self._datasources

    def get_docinfo(self):
        """
        Returns all doc info values for the XML workbook object.
        """
        return {
                'URL' : self._xml.docinfo.URL,
                'doctype' : self._xml.docinfo.doctype,
                'encoding' : self._xml.docinfo.encoding,
                'externalDTD' : self._xml.docinfo.externalDTD,
                'internalDTD' : self._xml.docinfo.externalDTD,
                'public_id' : self._xml.docinfo.public_id,
                'root_name' : self._xml.docinfo.root_name,
                'standalone' : self._xml.docinfo.standalone,
                'system_url' : self._xml.docinfo.system_url,
                'xml_version' : self._xml.docinfo.xml_version,
                }

    @staticmethod
    def _load_xml(filepath):
        """
        Generates workbook xml tree on instantiating a workbook
        To-Do: enable archived for tbwx
        """
        return etree.parse(filepath)

    @staticmethod
    def _load_datasources(xml):
        """
        Generates datasources elements and parses through them on instantiating a workbook
        """
        # for workbooks with more than one datasource, iterate
        sources = []
        for source in xml.xpath('/workbook/datasources/datasource'):
            ds = Datasource(source)
            sources.append(ds)
            pass
        return  sources
