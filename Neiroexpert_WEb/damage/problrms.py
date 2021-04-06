import pathlib
import os

            
projekt_path = r'C:\Users\suslo\Google Диск\2,5 млрд\Neiroexpert\neiroexpert_web\projekts\\'
projekt_number = 66
# files_path = projekt_path + str('/') + str(projekt_number)+ str('neiro_damage')
files_path = os.path.join(projekt_path, (str(projekt_number)+'\nero_damage'))
# files_path = os.path.join(files_path, str(15))
path = os.getcwd()  
print(files_path)
pic_path = files_path + str('\\') + "graf" +  str('\\')
# print(files_path, pic_path, 'до проверки папок в нейродамадж')
      
if not os.path.exists(files_path):
    os.mkdir(files_path)
else:
    path = pathlib.Path(files_path)
    for p in path.glob('*.*'):
        os.remove(p)

            
if not os.path.exists(pic_path):
    os.mkdir(pic_path)
else:
    path = pathlib.Path(pic_path)
    for p in path.glob('*.*'):
        os.remove(p)
# print(files_path, pic_path,  'после проверки папок в нейродамадж')