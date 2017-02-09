import os
import pprint
import sys
import xml.etree.ElementTree as ET

from lxml import etree


def prettyPrintXml(xmlFilePathToPrettyPrint):
    assert xmlFilePathToPrettyPrint is not None
    parser = etree.XMLParser(resolve_entities=False, strip_cdata=False)
    document = etree.parse(xmlFilePathToPrettyPrint, parser)
    document.write(xmlFilePathToPrettyPrint, pretty_print=True, encoding='utf-8')


root = ET.Element("models")

for filename in sorted(os.listdir(".")):
    if os.path.isdir(filename):
        if filename != ".idea":
            menu = ET.SubElement(root, filename)
            for subfilename in sorted(os.listdir("./" + filename)):
                sparqlFile = ET.SubElement(menu, subfilename)
                if os.path.isfile("./" + filename + "/" + subfilename):
                    with open("./" + filename + "/" + subfilename) as file_:
                        fields = dict()
                        linenumber = 0
                        for line in file_:
                            linenumber += 1
                            if linenumber == 1:
                                if not line.startswith("##"):
                                    sys.exit(subfilename + ": does not contain a correct header")
                                else:
                                    header = True
                                    fieldname = line.replace("##", "")
                                    content = ""
                            else:
                                if line.startswith("#") and not line.startswith("##"):
                                    content += line.replace("#", "")
                                if line.startswith("##"):
                                    fields[fieldname] = content
                                    fieldname = line.replace("##", "")
                                    content = ""
                                if not line.startswith("#"):
                                    if header == True:
                                        fields[fieldname] = content
                                        fields["query"] = line
                                    else:
                                        fields["query"] += line
                                    header = False
                        pprint.pprint(fields)
                        for field in fields.keys():
                            nodeElement = ET.SubElement(sparqlFile, field)
                            nodeElement.text = fields[field]

tree = ET.ElementTree(root)

tree.write("models.xml", encoding="utf-8", xml_declaration=True)

prettyPrintXml('models.xml')
