
Js_File = 'C:\\Users\\Zidane Khan\\Downloads\\SAMPLE1.json' 

with open(Js_File,'r') as js_file:

    Csv_Contents=js_file.read()
    print(Csv_Contents)