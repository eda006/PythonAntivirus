import shutil
import os

quarantine_dir = "Quarantine"


def quarantine_file(path):
    filename = os.path.basename(path)
    shutil.copyfile(path, os.path.join(quarantine_dir, filename + ".QUARANTINE"))
    os.remove(path)

