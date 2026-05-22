python
# grades.py

SUBJECTS = ["국어", "영어", "수학", "과탐"]


def get_scores():
    """4개 과목의 점수를 입력받아 딕셔너리로 반환한다."""
    scores = {}
    print("과목별 점수를 입력하세요 (0~100).\n")

    for subject in SUBJECTS:
        while True:
            try:
                score = float(input(f"{subject} 점수: "))
                if 0 <= score <= 100:
                    scores[subject] = score
                    break
                else:
                    print("  → 0에서 100 사이의 점수를 입력하세요.")
            except ValueError:
                print("  → 숫자를 입력하세요.")

    return scores


if __name__ == "__main__":
    scores = get_scores()
    print("\n입력된 점수:", scores)
