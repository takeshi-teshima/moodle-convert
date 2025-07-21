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
    shuffleanswers: bool = False
    single: bool = True
    answernumbering: str = "abc"  # one of "abc", "ABCD", "123", or "none"

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
            shuffleanswers=data.get("shuffleanswers"),
            single=data.get("single"),
            answernumbering=data.get("answernumbering"),
        )
