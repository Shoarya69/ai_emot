import os 
import time
from ai_face_persona.confi import value
def delete_lines_after_delay(file_path):
      # wait 200 sec
    
   
    with open(file_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if "delete_i" not in line:
            new_lines.append(line)

    with open(file_path, "w") as f:
        f.writelines(new_lines)

def delete_file_later(path, delay):
    time.sleep(delay)
    if os.path.exists(path):
        os.remove(path)
        print("Deleted:", path)


def monitor_and_delete(process,FAST_FILE):
    """Background thread: kills and deletes fast.py when confi.value == 1"""
    while True:
        if value == 1:
            print("\nconfi.value is 1 → Terminating fast.py and deleting file...\n")

            # Kill the subprocess
            process.terminate()
            process.wait()

            # Delete the file
            if os.path.exists(FAST_FILE):
                os.remove(FAST_FILE)
                print("fast.py deleted successfully.")

            break  # stop this thread
        time.sleep(0.2)  
