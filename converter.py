# converter.py
# 점수를 학점으로 변환하는 모듈

GRADE_SCALE = [
    (95, "A+"), (90, "A"),  (85, "B+"),
    (80, "B"),  (75, "C+"), (70, "C"),
    (65, "D+"), (60, "D"),  (0,  "F")
]


def convert_to_grade(score):
    """점수를 학점 문자열로 변환한다."""
    for threshold, grade in GRADE_SCALE:
        if score >= threshold:
            return grade
    return "F"


def print_grades(scores):
    """각 과목의 학점을 출력한다."""
    print("\n" + "=" * 30)
    print("       학점 결과")
    print("=" * 30)
    for subject, score in scores.items():
        grade = convert_to_grade(score)
        print(f"  {subject:<10} {score:>5.1f}점  {grade}")
    print("=" * 30)