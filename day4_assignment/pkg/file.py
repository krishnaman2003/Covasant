import os
import datetime

class File:
    def __init__(self, directory):
        self.directory = directory

    def getMaxSizeFile(self, n):
        files = [f for f in os.listdir(self.directory)
                 if os.path.isfile(os.path.join(self.directory, f))]
        files_sorted = sorted(
            files,
            key=lambda f: os.path.getsize(os.path.join(self.directory, f)),
            reverse=True
        )
        return files_sorted[:n]

    def getLatestFiles(self, date_obj):
        latest_files = []
        for f in os.listdir(self.directory):
            full_path = os.path.join(self.directory, f)
            if os.path.isfile(full_path):
                mod_time = os.path.getmtime(full_path)
                mod_date = datetime.date.fromtimestamp(mod_time)
                if mod_date > date_obj:
                    latest_files.append(f)
        return latest_files
