from dataclasses import dataclass
import yaml


@dataclass
class MultiChoiceQuiz:
    title: str
    question: str
    choices: dict
    answer: str
    feedback: dict
    general_feedback: str = ""
    shuffle: bool = False
    single: bool = True

    @classmethod
    def from_parsed_yaml(cls, data: dict) -> "MultiChoiceQuiz":
        """Create a MultiChoiceQuiz object from a parsed YAML dictionary."""
        return cls(
            title=data["title"],
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            feedback=data.get("feedback", {}),
            general_feedback=data.get("general_feedback"),
            shuffle=data.get("shuffle"),
            single=data.get("single"),
        )
