from dataclasses import dataclass


@dataclass
class TrueFalseQuiz:
    title: str
    question: str
    answer: bool
    feedback: dict

    @classmethod
    def from_parsed_yaml(cls, data: dict) -> "TrueFalseQuiz":
        """Create a TrueFalseQuiz object from a parsed YAML dictionary."""
        return cls(
            title=data["title"],
            question=data["question"],
            answer=bool(data["answer"]),
            feedback=data.get("feedback", {}),
        )
