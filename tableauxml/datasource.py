import lxml.etree as etree

class Datasource:
    """
    A class for the Tableau Datasources, identified within the xml.
    """

    def __init__(self):
        self._caption = ''
        self._inline = ''


    def _load_datasources(self):
        """
        Creates datasource element list
        """
        self._datasources = self._xml.xpath('/workbook/datasources/datasource')
