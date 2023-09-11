import scan
import os

to_scan = []

while True:
    print("Current directories to scan - ", to_scan)
    directory = input("Enter a path to add to the scan, or press enter to start: ")
    if directory == "":
        break

    if os.path.isdir(directory):
        to_scan.append(directory)
    else:
        print("Could not find the provided directory")

for i, path in enumerate(to_scan):
    print(f"Scanning {path} ({i+1}/{len(to_scan)})")

    threats = scan.check_dir(path)
    print("Scan complete")
    total = len(threats)
    if total > 0:
        print(f"{total} Threat(s) found.")
        for t in threats:
            print("-" * 40)
            print("THREAT DETAILS: ")
            print("File name:\t", os.path.basename(t.filepath))
            print("Path:\t", t.filepath)
            print("MD5 hash:\t", t.file_hash)
            print("Date of detection:\t", t.detection_time)

            should_quarantine = input("Do you wish to quarantine the file? y/n ")
            if should_quarantine.lower() in ["y", "yes"]:
                t.quarantine()
                print("File was quarantined")
