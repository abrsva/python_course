import xml.etree.ElementTree as ET

tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
conj = 0
verb = 0
with open("nouns.txt", 'w', encoding="UTF-8") as f:
    for token in root.findall('text/paragraphs/paragraph/sentence/tokens/token'):
        word = token.attrib['text']
        attribs = set(map(lambda x: x.attrib['v'], token.findall('tfr/v/l/g')))
        if word.strip().lower() == "может":
            if "CONJ" in attribs:
                conj += 1
            if "VERB" in attribs:
                verb += 1

print("Conj:", conj)
print("Verb:", verb)
