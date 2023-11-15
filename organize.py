import os
import shutil
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#Caminhos dos diretórios
from_dir = "C:/Users/Prof Andréa/Downloads"
to_dir = "./"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

#Classe gerenciadora de Arquivos
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        name,ext = os.path.splitext(event.src_path)
        for key,value in dir_tree.items():
            if ext in value :
                file_name = os.path.basename(event.src_path)
                path1 = from_dir + "/" + file_name
                path2 = to_dir + "/" + key
                path3 = to_dir + "/" + key + "/" + file_name


#instanciando/inicializando a classe Gerenciadora de Arquivos
event_handler = FileMovementHandler()

#instanciando o observador
observer = Observer()

#Agedando o Oberservador
observer.schedule(event_handler,from_dir,recursive=True)

#Startando o observador
observer.start()


while True:
    time.sleep(2)
    print("Executando...")



