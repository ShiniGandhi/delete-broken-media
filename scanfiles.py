import os
import subprocess

def hasAudio(filePath):
    result = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'a', '-show_entries', 'stream=codec_type', '-of', 'default=noprint_wrappers=1:nokey=1', filePath], capture_output=True, text=True)
    return "audio" in result.stdout

def checkFiles(directory):
    missingAudio = []
    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith((".mp4", ".mkv", ".avi", ".webm")):
                continue
            filePath = os.path.join(root, file)
            if hasAudio(filePath):
                pass
            else:
                missingAudio.append(filePath)
                print(f"{filePath} has no audio track.")
    return missingAudio

if __name__ == "__main__":
    libraryDirectory = input("enter path to media library: ")
    if not os.path.exists(libraryDirectory):
        print("invalid path")
    else:
        missingFiles = checkFiles(libraryDirectory)
        if missingFiles:
            choice = input(f"{len(missingFiles)} files with no audio tracks found. delete? [y/N] ")
            if choice.lower() == 'y':
                for file in missingFiles:
                    print(f'deleting {file}')
                    os.remove(file)
            else:
                print('exiting')