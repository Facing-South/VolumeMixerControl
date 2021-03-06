import pythoncom
from pycaw.pycaw import AudioUtilities

def setAppVolumeName(appName, level):
  try:
    pythoncom.CoInitialize()
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
      if session.Process and session.Process.name() == appName:
        volume = session.SimpleAudioVolume
        volume.SetMasterVolume(level, None)
  except Exception as e:
    print(e)
    input()
    pass