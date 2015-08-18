# coding: utf-8
import os 
FindPath="docs"
filenames=os.listdir(FindPath) 
for name in filenames:
	if name.endswith(".md"):
		dotIndex = name.index(".")
		fileName = name[:dotIndex]
		fromFile=os.path.join(FindPath,name)
		toFile = "docbook/" + fileName + ".xml"
		cmd = "pandoc "+fromFile+" -f markdown -t docbook -o "+toFile
		os.system(cmd)
