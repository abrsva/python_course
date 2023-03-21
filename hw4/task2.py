import xml.etree.ElementTree as ET

tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
with open("nouns.txt", 'w', encoding="UTF-8") as f:
    for token in root.findall('text/paragraphs/paragraph/sentence/tokens/token'):
        attribs = set(map(lambda x: x.attrib['v'], token.findall('tfr/v/l/g')))
        if 'NOUN' in attribs and "plur" in attribs:
            f.write(token.attrib['text'] + '\n')
