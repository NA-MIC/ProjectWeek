import xml.etree.ElementTree as ET

ns = {'inkscape': 'http://www.inkscape.org/namespaces/inkscape',
      'sodipodi': 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd',
      'ns': 'http://www.w3.org/2000/svg'}

polarMapFP = "https://github.com/NA-MIC/ProjectWeek/blob/master/PW37_2022_Virtual/Projects/SlicerHeartPolarMaps/PolarMap.svg"

tree = ET.parse(polarMapFP)
root = tree.getroot()

for group in root.findall('ns:g', ns):
    for path in group[0].findall('ns:path', ns):
        # try setting each element from 0-10 degrees to white
        if(path.attrib["{http://www.inkscape.org/namespaces/inkscape}label"] == "0-10"):
            style = path.attrib["style"]
            style = style[0:20] + "ffffff" + style[27:]
            print(style)
            #style[21:27] = "FFFFFF"
            path.set('style', style)

# Saving the changed SVG, though ideally this is unnecessary
outputFN = "C:\\Users\\haber\\Documents\\School\\VT Ablation Project\\3D Slicer\\Project Week 37\\testOutput.svg"
tree.write(outputFN)

# Show the updated polar map in Slicer
imageWidget = qt.QLabel()
#!!! DO SOMETHING HERE TO SHOW THE SVG IN SLICER !!!
imageWidget.show()
