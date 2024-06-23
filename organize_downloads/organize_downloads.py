import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DownloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            if os.path.isfile(src):
                self.organize_files(src)

    def organize_files(self, src):
        extension_to_folder = {
            '.pdf': 'Documents',
            '.docx': 'Documents',
            '.txt': 'Documents',
            '.jpg': 'Images',
            '.png': 'Images',
            '.gif': 'Images',
            '.exe': 'Software',
            '.zip': 'Software'
        }

        _, extension = os.path.splitext(src)
        if extension in extension_to_folder:
            folder_name = extension_to_folder[extension]
            new_destination = folder_to_track + "/" + folder_name + "/" + os.path.basename(src)
            if not os.path.exists(folder_to_track + "/" + folder_name):
                os.makedirs(folder_to_track + "/" + folder_name)
            shutil.move(src, new_destination)

folder_to_track = "/path/to/your/Downloads"
event_handler = DownloadHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
