#CommonTraits: {
	title!: string,
	rubric?: string,
	general_feedback?: string,
	...
}

#MultiChoiceQuiz: #CommonTraits & {
	type:     "multichoice",
	question!: string,
	choices!: { [=~"^[A-Z]$"]: string},
	answer!: string & or([ for k, v in choices { k } ]),
	feedback?: { for k, v in choices { (k)?: string } },
	shuffleanswers?: *false | bool,
	answernumbering?: *"abc" | "ABCD" | "123" | "none",
	single?: *true | bool  // true for single choice, false for multiple choices
}

#TrueFalseQuiz: #CommonTraits & {
	type: "truefalse",
	question!: string,
	answer!: bool,
	feedback?: {
		true?:  string,
		false?: string,
	}
}

Quizzes: [...(#MultiChoiceQuiz | #TrueFalseQuiz)]

#config: {
	format: "markdown" | "html" | "moodle_auto_format" | "plain_text",
	html_escape?: *true | bool,
	multichoice?: {
		shuffleanswers?: *false | bool,
		answernumbering?: *"abc" | "ABCD" | "123" | "none",
	}
}