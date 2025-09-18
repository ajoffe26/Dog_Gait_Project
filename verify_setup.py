import importlib, sys

print('Python executable:', sys.executable)
packages = ['numpy', 'pandas', 'sklearn', 'torch', 'cv2', 'mediapipe']
for p in packages:
    try:
        m = importlib.import_module('cv2' if p == 'opencv-python' or p == 'cv2' else p)
        v = getattr(m, '__version__', None)
        print(f"{p} OK", 'version=' + (v or 'unknown'))
    except Exception as e:
        print(p + ' ERROR', e)

print('Python', sys.version)
