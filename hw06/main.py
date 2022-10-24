
from operator import truediv
from pathlib import Path
import sys
import re
import shutil



img_files=[]
videos_files=[]
documents_files=[]
music_files=[]
archives_files=[]
other_files=[]

images=['.png','.jpg','.jpeg','.svg'],
videos=['.avi', '.mp4', '.mov', '.mkv'],
documents=['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
music=['.mp3', '.ogg', '.wav', '.amr'],
archives=['.zip', '.gz', '.tar','.rar']



FOLDERS =[]



#! cловник для розширень і сортування файлів
FILE_TYPES={
    tuple(['png','jpg','jpeg','svg']):img_files,
    tuple(['avi', 'mp4', 'mov', 'mkv']):videos_files,
    tuple(['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']):documents_files,
    tuple(['mp3', 'ogg', 'wav', 'amr']):music_files,
    tuple(['zip', 'gz', 'tar','rar']):archives_files,
}

FILE_TAGS={
    'images':img_files,
    'videos':videos_files,
    'documents':documents_files,
    'music':music_files,
    'archives':archives_files,
}



#! словник для перекладу 
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}





for k,v in zip(CYRILLIC_SYMBOLS,TRANSLATION):
    TRANS[ord(k)]=v
    TRANS[ord(k.upper())]=v.upper()



#! парсинг файлів
def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()



def scanning(folder: Path)->None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ['images','videos','documents','archives','music']:
                FOLDERS.append(item)
            continue
        ext = get_extension(item.name).lower()
        fullname= folder / item.name
        for k,v in FILE_TYPES.items():
            if ext in k:
                v.append(fullname)
            else:
                normalize(fullname.name)




#! нормалізація файлів
def normalize(name: str) -> str:
    try:
        ext,t_name = name.split('.')[::-1]
    except:
        pass
    t_name = t_name.translate(TRANS)
    t_name = re.sub(r'\W', '_', t_name)
    t_name=t_name+'.'+ext
    return t_name

#! cтворення та переміщення файлів у папки


def handle_standart(filename:Path, path:Path):
    path.mkdir(exist_ok=True,parents=True)
    filename.replace(path / normalize(filename.name))

def handle_archives(filename:Path,path:Path):
    path.mkdir(exist_ok=True,parents=True)
    archive_folder= path / normalize(filename.name.replace(filename.suffix,''))
    
    archive_folder.mkdir(exist_ok=True,parents=True)
    try: 
        shutil.unpack_archive(str(filename.resolve()),str(archive_folder.resolve()))
    except shutil.ReadError:
        print(f"It isn't archive: {filename.name}")
        archive_folder.rmdir()
    filename.unlink()

#! основний скрипт
def main(path:Path):
    scanning(path)
    for file in FILE_TAGS.get('images'):
        handle_standart(file , path / 'images')
    for file in FILE_TAGS.get('videos'):
        handle_standart(file , path / 'videos')
    for file in FILE_TAGS.get('documents'):
        handle_standart(file , path / 'documents')
    for file in FILE_TAGS.get('music'):
        handle_standart(file , path / 'music')
    for file in FILE_TAGS.get('archives'):
        handle_archives(file , path / 'archives')
        
    

        
        




if __name__=='__main__':
    dir_scan=Path(sys.argv[1])
    main(dir_scan.resolve())
    

