#CommonTraits: {
	title!: string,
	rubric?: string,
	...
}

#MultiChoiceQuiz: #CommonTraits & {
	type:     "multichoice",
	question!: string,
	choices!: { [=~"^[A-Z]$"]: string},
	answer!: string & or([ for k, v in choices { k } ]),
	feedback?: {	for k, v in choices { (k)?: string } },
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
	format: "html" | "moodle_auto_format" | "plain_text" | "markdown",
	html_escape?: bool
}