import pytest

from lxml import etree
from lxml import objectify

from lxml_to_dict import lxml_to_dict


def test_one_element():
    root = objectify.Element("root")            # <root></root>
    assert lxml_to_dict(root) == {'root': None}


def test_one_subelement():
    root = objectify.Element("root")            # <root></root>
    objectify.SubElement(root, "b")             # <root><b></b></root>
    assert lxml_to_dict(root) == {'root': {'b': None}}


def test_two_subelements():
    root = objectify.Element("root")            # <root></root>
    objectify.SubElement(root, "b")             # <root><b></b></root>
    objectify.SubElement(root, "a")             # <root><b></b><a></a></root>
    assert lxml_to_dict(root) == {'root': {'b': None, 'a': None}}


def test_two_subelements_same_tag():
    root = objectify.Element("root")            # <root></root>
    objectify.SubElement(root, "b")             # <root><b></b></root>
    objectify.SubElement(root, "b")             # <root><b></b><b></b></root>
    assert lxml_to_dict(root) == {'root': {'b': None, 'b1': None}}


def test_many_subelements_same_tag():
    root = objectify.Element("root")            # <root></root>
    objectify.SubElement(root, "b")             # <root><b></b></root>
    objectify.SubElement(root, "b")             # <root><b></b><b></b></root>
    objectify.SubElement(root, "b")
    objectify.SubElement(root, "b")
    objectify.SubElement(root, "b")
    objectify.SubElement(root, "b")
    objectify.SubElement(root, "b")
    assert lxml_to_dict(root) == {'root': {'b': None,
                                           'b1': None,
                                           'b2': None,
                                           'b3': None,
                                           'b4': None,
                                           'b5': None,
                                           'b6': None}}


def test_nested_subelements():
    root = objectify.Element("root")            # <root></root>
    b = objectify.SubElement(root, "b")         # <root><b></b></root>
    a = objectify.SubElement(b, "a")            # <root><b><a></a></b></root>
    objectify.SubElement(a, "c")                # <root><b><a><c></c></a></b></root>
    assert lxml_to_dict(root) == {'root':
                                  {'b':
                                   {'a':
                                    {'c': None}
                                    }
                                   }
                                  }


def test_nested_subelements_same_tags():
    root = objectify.Element("root")            # <root></root>
    b = objectify.SubElement(root, "b")         # <root><b></b></root>
    a = objectify.SubElement(b, "a")            # <root><b><a></a></b></root>
    a = objectify.SubElement(b, "a")            # <root><b><a></a><a></a></b></root>
    objectify.SubElement(a, "c")                # <root><b><a></a><a><c></c></a></b></root>
    objectify.SubElement(a, "c")                # <root><b><a></a><a><c></c><c></c></a></b></root>
    assert lxml_to_dict(root) == {'root':
                                  {'b':
                                   {'a': None,
                                    'a1':
                                    {'c': None,
                                     'c1': None}
                                    }
                                   }
                                  }
