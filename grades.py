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

def calculate_average(scores):
    """점수 딕셔너리를 받아 평균을 반환한다."""
    if not scores:
        return 0.0
    return sum(scores.values()) / len(scores)


def print_result(scores, average):
    """점수와 평균을 보기 좋게 출력한다."""
    print("\n" + "=" * 30)
    print("       성적 결과")
    print("=" * 30)
    for subject in SUBJECTS:
        print(f"  {subject:<10} {scores[subject]:>6.1f}점")
    print("-" * 30)
    print(f"  {'평균':<10} {average:>6.1f}점")
    print("=" * 30)
if __name__ == "__main__":
    scores = get_scores()
    print("\n입력된 점수:", scores)
    
    average = calculate_average(scores)
    print(f"평균 점수: {average:.1f}점")
