# file_io.py
# 점수를 파일로 저장하고 불러오는 모듈

import os

DATA_FILE = "data/scores.txt"


def save_scores(scores):
    """점수 딕셔너리를 파일에 저장한다."""
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for subject, score in scores.items():
            f.write(f"{subject},{score}\n")
    print(f"점수가 {DATA_FILE}에 저장되었습니다.")


def load_scores():
    """파일에서 점수를 불러와 딕셔너리로 반환한다."""
    if not os.path.exists(DATA_FILE):
        print("저장된 점수 파일이 없습니다.")
        return {}
    scores = {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            subject, score = line.strip().split(",")
            scores[subject] = float(score)
    return scores