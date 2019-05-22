from collections import UserDict

from lxml import etree

from .host_properties import HostProperties
from .report_item import ReportItem


class ReportHost(UserDict):
    def __init__(self, elements, host_properties):
        super(ReportHost, self).__init__(host_properties)
        assert isinstance(elements, list)
        self['report_items'] = elements

    @staticmethod
    def from_etree(elem):
        if elem is None:
            return elem
        assert isinstance(elem, etree._Element)
        assert elem.tag == 'ReportHost'

        host_properties = {'name': elem.attrib.get('name')}
        if elem.find('HostProperties') is not None:
            host_properties['tags'] = HostProperties.from_etree(elem.find('HostProperties'))
        report_items = [ReportItem.from_etree(el) for el in elem.findall('ReportItem')]

        return ReportHost(report_items, host_properties)
