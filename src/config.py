from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PATH_DATA = BASE_DIR / "data"
PATH_AMESHOUSING = PATH_DATA / "raw" / "AmesHousing.csv"