from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
WEBCAM = 'Webcam'
RTSP = 'RTSP'
YOUTUBE = 'YouTube'

SOURCES_LIST = [IMAGE, VIDEO, WEBCAM, RTSP, YOUTUBE]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'office_4.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'office_4_detected.jpg'
IMAGE_1_PATH = IMAGES_DIR / 'AbandonedCandidAfricanporcupine.mp4'
IMAGE_2_PATH = IMAGES_DIR / 'BarrenSecondhandAcornwoodpecker-mobile.mp4'
IMAGE_3_PATH = IMAGES_DIR / 'SlimyDependentIbadanmalimbe-mobile.mp4'
#IMAGE_4_PATH = IMAGES_DIR / 'video_4.mp4'
#IMAGE_5_PATH = IMAGES_DIR / 'video_5.mp4'
IMAGE_DICT = {
    'image_1': IMAGE_1_PATH,
    'image_2': IMAGE_2_PATH,
    'image_3': IMAGE_3_PATH,
    #'video_4': VIDEO_4_PATH,
    #'video_5': VIDEO_5_PATH,
}



# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEO_1_PATH = VIDEO_DIR / 'AbandonedCandidAfricanporcupine.mp4'
VIDEO_2_PATH = VIDEO_DIR / 'BarrenSecondhandAcornwoodpecker-mobile.mp4'
VIDEO_3_PATH = VIDEO_DIR / 'SlimyDependentIbadanmalimbe-mobile.mp4'
#VIDEO_4_PATH = VIDEO_DIR / 'video_4.mp4'
#VIDEO_5_PATH = VIDEO_DIR / 'video_5.mp4'
VIDEOS_DICT = {
    'video_1': VIDEO_1_PATH,
    'video_2': VIDEO_2_PATH,
    'video_3': VIDEO_3_PATH,
    #'video_4': VIDEO_4_PATH,
    #'video_5': VIDEO_5_PATH,
}

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'best.pt'

# Webcam
WEBCAM_PATH = 0
