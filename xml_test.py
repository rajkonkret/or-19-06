from xml.dom import minidom

DOMTree = minidom.parse('dane_xml.xml')
print((DOMTree.toxml))
# <bound method Node.toxml of <xml.dom.minidom.Document object at 0x00000247B1D76090>>

cNodes = DOMTree.childNodes
print(cNodes)
# [<DOM Element: znajomi at 0x2c4bd9204b0>]
print(cNodes[0])
# <DOM Element: znajomi at 0x198716504b0>
print(cNodes[0].getElementsByTagName('osoba'))
# [<DOM Element: osoba at 0x1d1b92f1810>, <DOM Element: osoba at 0x1d1b9308b90>]
print(cNodes[0].getElementsByTagName('osoba')[0])
# <DOM Element: osoba at 0x1746fe21810>
print(cNodes[0].getElementsByTagName('osoba')[0].toxml())
# <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>
print(cNodes[0].getElementsByTagName('osoba')[1].toxml())
print(cNodes[0].getElementsByTagName('osoba')[1].getElementsByTagName('imie'))
# [<DOM Element: imie at 0x1f50401cc30>]
print(cNodes[0].getElementsByTagName('osoba')[1].getElementsByTagName('imie')[0].toxml())
# <imie foo="aaaa">Janina</imie>
