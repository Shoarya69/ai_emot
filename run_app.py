from ai_face_persona import main,confi
from ai_face_persona.self_api import monitor_and_delete
import subprocess
import sys
import threading


file_name = "/home/shoarya/Desktop/ai_emotion/AI-Face-Emotion-Persona/fast.py"


print('Starting main()')
app_process = subprocess.Popen([sys.executable, "fast.py"])
thread = threading.Thread(target=monitor_and_delete, args=(app_process,file_name), daemon=True)
thread.start()
try:
    main.main()
except Exception as e:
    print("Somthing went wrong")
finally:
    app_process.terminate()  # polite termination
    app_process.wait()
    
