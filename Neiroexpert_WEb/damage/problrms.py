import pathlib
import os

            
projekt_path = r'C:\Users\suslo\Google Диск\2,5 млрд\Neiroexpert\Neiroexpert_WEb\projekts'
projekt_number = 2
# files_path = projekt_path + str('/') + str(projekt_number)+ str('neiro_damage')
files_path = os.path.join(projekt_path,str(projekt_number),'neiro_damage' )

pic_path = files_path + str('\\') + "graf" +  str('\\')
print(files_path, pic_path, 'до проверки папок в нейродамадж')
os.mkdir(files_path)        
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
print(files_path, pic_path,  'после проверки папок в нейродамадж')