try:
    import mistletoe
except:
    pip_install('mistletoe')
    import mistletoe

with open('test.md', 'r') as fin:
    docHtml = mistletoe.markdown(fin)

print(docHtml)

displayWidget = qt.QTextEdit()
displayWidget.setText(docHtml)
displayWidget.show()

doc = vtk.vtkXMLUtilities.ReadElementFromString("<root>"+docHtml+"</root>")
question = {}
questions = []
for index0 in range(doc.GetNumberOfNestedElements()):
    element0 = doc.GetNestedElement(index0)
    if element0.GetName() == 'h1':
        # Found a new question
        # Save old question first
        if question:
            questions.append(question)
        question = {}
        question['title'] = element0.GetCharacterData()
        question['answers'] = []
    if element0.GetName() == 'ul':
        # Found a new answer list
        for index1 in range(element0.GetNumberOfNestedElements()):
            element1 = element0.GetNestedElement(index1)
            question['answers'].append(element1.GetCharacterData())

print(questions)
