from dataclasses import dataclass


@dataclass
class TrueFalseQuiz:
    title: str
    question: str
    answer: bool
    feedback: dict
    default_grade: float | int
    general_feedback: str = ""

    @classmethod
    def from_parsed_yaml(cls, data: dict) -> "TrueFalseQuiz":
        """Create a TrueFalseQuiz object from a parsed YAML dictionary."""
        return cls(
            title=data["title"],
            question=data["question"],
            answer=bool(data["answer"]),
            feedback=data.get("feedback", {}),
            default_grade=data.get("default_grade"),
            general_feedback=data.get("general_feedback", ""),
        )
