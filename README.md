# lxml to dict #

[Package on Pypi](https://pypi.org/project/lxml-to-dict/)

A simple conversion of an lxml.objectify element to a python dictionary.

## Usage ##

~~~python
>>> from lxml_to_dict import lxml_to_dict
>>> 
>>> lxml_to_dict(<the lxml.objectfy.Element>)
>>>
>>> root = objectify.Element("root")            # <root></root>
>>> b = objectify.SubElement(root, "b")         # <root><b></b></root>
>>> b = objectify.SubElement(root, "b")         # <root><b></b><b></b></root>
>>> a = objectify.SubElement(root, "a")         # <root><b></b><b></b><a></a></root>
>>> lxml_to_dict(root)                          # {'root': {'b': None, 'b1': None, 'a': None}}
~~~

## Test ##

You can run the tests using [tox](https://tox.readthedocs.io/en/latest/)

~~~shell
tox
~~~

## Publish ##

To publish a new version of this package your Pypi user needt to be added to the project. (Ask Connor to give you access)

~~~shell
# Update version number in setup.py

python setup.py sdist
twine upload dist/*
~~~