VERSION = "0.4.0"
# ========configuration============ 
ADB_PATH = r".\tools\adb\adb.exe"
TARGET_PORT = 3861

TIMETABLE_TASK = [[6, 7],[6, 7],[6, 7],[6],[],[],[],[],[]]

WANTED_HIGHEST_LEVEL = [[0, 8, -1], [1, 8, -1], [2, 8, -1]]
EXCHANGE_HIGHEST_LEVEL = [[0, 1, 3], [1, 1, 3], [2, 1, 3]]

QUEST = {
            "HARD":     [
                            [[13,1,3], [16,1,3]],
                            [[13,2,3]],
                        ],
            "NORMAL":   [
                            [[16,1,2], [17,1,2]],
                            [[15,4,2], [18,2,3]],
                        ],
        }

TIME_AFTER_CLICK = 0.7

# =================================

PIC_PATH = "./assets"
SCREENSHOT_NAME = "screenshot.png"