from dataclasses import dataclass

@dataclass
class YesNoQuiz:
    title: str
    question: str
    answer: bool
    feedback: dict

    @classmethod
    def from_parsed_yaml(cls, data: dict) -> "YesNoQuiz":
        """Create a YesNoQuiz object from a parsed YAML dictionary."""
        return cls(
            title=data["title"],
            question=data["question"],
            answer=bool(data["answer"]),
            feedback=data.get("feedback", {}),
        )
