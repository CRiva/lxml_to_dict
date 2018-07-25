import re


def lxml_to_dict(element):
    ret = {}
    if element.getchildren() == []:
        tag = re.sub('{.*}', '', element.tag)
        ret[tag] = element.text
    else:
        count = {}
        for elem in element.getchildren():
            subdict = lxml_to_dict(elem)
            tag = re.sub('{.*}', '', element.tag)
            subtag = re.sub('{.*}', '', elem.tag)
            if ret.get(tag, False) and subtag in ret[tag].keys():
                count[subtag] = count[subtag]+1 if count.get(subtag, False) else 1
                elemtag = subtag+str(count[subtag])
                subdict = {elemtag: subdict[subtag]}
            if ret.get(tag, False):
                ret[tag].update(subdict)
            else:
                ret[tag] = subdict
    return ret
