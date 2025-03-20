
SRC_File = 'C:\\Users\\Zidane Khan\\Downloads\\SAMPLE.csv' 

with open(SRC_File,'r') as src_file:

    Csv_Contents=src_file.read()
    print(Csv_Contents)