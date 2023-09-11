import os
import hashlib
import datetime
import quarantine

# list of malware MD5 hashes was found here: https://github.com/Len-Stevens/MD5-Malware-Hashes/blob/main/MD5%20Hahses.zip
# memory usage may be massive here -- TO DO: use a database instead
malware_hashes = open("MD5 Hashes.txt", "r").read().split("\n")


class Threat:
    def __init__(self, filepath, file_hash, detection_time=None):
        self.filepath = filepath
        self.file_hash = file_hash

        if detection_time is None:
            self.detection_time = datetime.datetime.now()

    def quarantine(self):
        quarantine.quarantine_file(self.filepath)



def check_dir(directory):
    threats_found = []

    # iterate through all files in directory
    for filename in os.scandir(directory):
        # check that file is a file and not a folder
        if filename.is_file():
            filepath = os.path.join(directory, filename)
            # read bytes from the file, do an md5 hash, check if in list of bad hashes
            file = open(filepath, "rb")
            file_content = file.read()
            file_hash = hashlib.md5(file_content).hexdigest()

            if file_hash in malware_hashes:
                threat = Threat(filepath, file_hash)
                threats_found.append(threat)
    return threats_found


