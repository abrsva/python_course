import xml.etree.ElementTree as ET

tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
with open("sentences.txt", "w", encoding='utf-8') as file:
    for x in root.findall('text/paragraphs/paragraph/sentence'):
        sentence = x.find('source').text
        file.write(sentence + '\n')
