from dataclasses import dataclass
import yaml


@dataclass
class MultiChoiceQuiz:
    title: str
    question: str
    choices: dict
    answer: str
    feedback: dict

    @classmethod
    def from_parsed_yaml(cls, data: dict) -> "MultiChoiceQuiz":
        """Create a MultiChoiceQuiz object from a parsed YAML dictionary."""
        return cls(
            title=data["title"],
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            feedback=data.get("feedback", {}),
        )
