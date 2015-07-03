__author__ = 'Tails'

import sys, re
import xml.etree.ElementTree as ET
import xml.dom.minidom

from six import u

try:
    # Python 2
    unichr
except NameError:  # pragma: nocover
    # Python 3
    unichr = chr

"""
Based on the following understanding of what Jenkins can parse for Nunit XML files.

<test-results>
    <test-suite name="Test Suite 1">
        <results>
            <test-case name="Test Case A" time="5" />
            <test-case name="Test Case B" time="5">
                <failure>
                    <message>Failed...</message>
                    <stack-trace>failed stack trace</stack-trace>
                </failure>
            </test-case>
        </results>
    </test-suite>
</test-results>
"""

class TestSuite(object):
    """Suite of test cases"""

    def __init__(self, name, test_cases=None, hostname=None, id=None,\
                 package=None, timestamp=None, properties=None):
        self.name = name
        if not test_cases:
            test_cases = []
        try:
            iter(test_cases)
        except TypeError:
            raise Exception('test_cases must be a list of test cases')
        self.test_cases = test_cases

    def build_xml_doc(self):
        """Builds the XML document for the JUnit test suite"""
        # build the test suite element
        test_suite_attributes = dict()
        test_suite_attributes['name'] = str(self.name)

        xml_element = ET.Element("test-suite", test_suite_attributes)
        results_element = ET.SubElement(xml_element, 'results')

        # test cases
        for case in self.test_cases:
            test_case_attributes = dict()
            test_case_attributes['name'] = str(case.name)
            if case.time:
                test_case_attributes['time'] = "%f" % case.time

            test_case_element = ET.SubElement(results_element, "test-case", test_case_attributes)

            # failures
            if case.is_failure():
                test_case_failure_element = ET.SubElement(test_case_element, "failure")
                test_case_failure_message_element = ET.SubElement(test_case_failure_element, 'message')
                test_case_failure_message_element.text = case.failure_message
                test_case_failure_stackTrace_element = ET.SubElement(test_case_failure_element, 'stack-trace')
                test_case_failure_stackTrace_element.text = case.failure_stackTrace

        return xml_element

    @staticmethod
    def to_xml_string(test_suites, prettyprint=True, encoding=None):
        """Returns the string representation of the NUnit XML document"""
        try:
            iter(test_suites)
        except TypeError:
            raise Exception('test_suites must be a list of test suites')

        xml_element = ET.Element("test-results")
        for ts in test_suites:
            xml_element.append(ts.build_xml_doc())

        xml_string = ET.tostring(xml_element, encoding=encoding)
        xml_string = TestSuite._clean_illegal_xml_chars(xml_string.decode(encoding or 'utf-8'))

        if prettyprint:
            xml_string = xml.dom.minidom.parseString(xml_string).toprettyxml()

        return xml_string

    @staticmethod
    def to_file(file_descriptor, test_suites, prettyprint=True, encoding=None):
        """Writes the JUnit XML document to file"""
        file_descriptor.write(TestSuite.to_xml_string(test_suites, prettyprint, encoding))

    @staticmethod
    def _clean_illegal_xml_chars(string_to_clean):
        """Removes any illegal unicode characters from the given XML string"""
        # see http://stackoverflow.com/questions/1707890/fast-way-to-filter-illegal-xml-unicode-chars-in-python
        illegal_unichrs = [(0x00, 0x08), (0x0B, 0x1F), (0x7F, 0x84), (0x86, 0x9F),
                           (0xD800, 0xDFFF), (0xFDD0, 0xFDDF), (0xFFFE, 0xFFFF),
                           (0x1FFFE, 0x1FFFF), (0x2FFFE, 0x2FFFF), (0x3FFFE, 0x3FFFF),
                           (0x4FFFE, 0x4FFFF), (0x5FFFE, 0x5FFFF), (0x6FFFE, 0x6FFFF),
                           (0x7FFFE, 0x7FFFF), (0x8FFFE, 0x8FFFF), (0x9FFFE, 0x9FFFF),
                           (0xAFFFE, 0xAFFFF), (0xBFFFE, 0xBFFFF), (0xCFFFE, 0xCFFFF),
                           (0xDFFFE, 0xDFFFF), (0xEFFFE, 0xEFFFF), (0xFFFFE, 0xFFFFF),
                           (0x10FFFE, 0x10FFFF)]

        illegal_ranges = ["%s-%s" % (unichr(low), unichr(high))
                          for (low, high) in illegal_unichrs
                          if low < sys.maxunicode]

        illegal_xml_re = re.compile(u('[%s]') % u('').join(illegal_ranges))
        return illegal_xml_re.sub('', string_to_clean)


class TestCase(object):

    def __init__(self, name, time=None):
        self.name = name
        self.time = time # second
        self.failure_message = None
        self.failure_stackTrace = None

    def add_failure_info(self, message=None, stackTrace=None):
        if message:
            self.failure_message = message
        if stackTrace:
            self.failure_stackTrace = stackTrace

    def is_failure(self):
        """returns true if this test case is a failure"""
        return self.failure_message or self.failure_stackTrace