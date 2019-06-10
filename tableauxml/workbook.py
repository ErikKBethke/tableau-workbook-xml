import lxml.etree as etree

# %%
class Workbook:
    """
    Creates a Tableau Workbook object.
    """

    def __init__(self, filepath, encoding='utf-8'):
        self.filepath = filepath
        self.encoding = encoding
        self.xml = None
        self.datasources = None

    def load_xml(self):
        """
        Takes the workbook filepath and creates an ElementTree object for xml.
        """
        self.xml = etree.parse(self.filepath)

    def load_datasources(self):
        """
        """
        self.datasources = self.xml.xpath('/workbook/datasources/datasource')

    def get_docinfo(self):
        """
        Returns all doc info values for the XML object.
        """
        return {
                'URL' : self.xml.docinfo.URL,
                'doctype' : self.xml.docinfo.doctype,
                'encoding' : self.xml.docinfo.encoding,
                'externalDTD' : self.xml.docinfo.externalDTD,
                'internalDTD' : self.xml.docinfo.externalDTD,
                'public_id' : self.xml.docinfo.public_id,
                'root_name' : self.xml.docinfo.root_name,
                'standalone' : self.xml.docinfo.standalone,
                'system_url' : self.xml.docinfo.system_url,
                'xml_version' : self.xml.docinfo.xml_version,
                }
