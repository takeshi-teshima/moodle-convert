import yaml
from src.quiz_types.multichoice import MultiChoiceQuiz
from src.quiz_types.truefalse import TrueFalseQuiz

QUIZ_TYPE_CLASSES = {
    "truefalse": TrueFalseQuiz,
    "multichoice": MultiChoiceQuiz,
}


def parse_yaml_file(file_path: str):
    """Parse a YAML file and return a list of quizzes."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    quizzes = []
    for quiz_data in data["Quizzes"]:
        quiz_type = quiz_data.get("type")
        if quiz_type not in QUIZ_TYPE_CLASSES:
            raise ValueError(f"Unsupported quiz type: {quiz_type}")

        quiz_class = QUIZ_TYPE_CLASSES[quiz_type]
        quizzes.append(quiz_class.from_parsed_yaml(quiz_data))

    return quizzes
