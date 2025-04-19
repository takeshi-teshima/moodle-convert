#Quiz: {
	rubric:   string & != ""
	type:     "multichoice" | "truefalse"
	title:    string & != ""
	question: string & != ""

	if type == "multichoice" {
		choices: {
			A: string & != ""
			B: string & != ""
			...string & != ""
		}
		answer: string & or([ for k, _ in choices { k } ])
		feedback: {
			(k): string & != "" for k, _ in choices
		}
	}

	if type == "truefalse" {
		answer: bool
		feedback: {
			true:  string & != ""
			false: string & != ""
		}
	}
}

Quizzes: [...#Quiz]
