import unittest
from src.quiz_types.yesno import YesNoQuiz

class TestYesNoQuiz(unittest.TestCase):
    def test_parse_yaml(self):
        yaml_data = [
            {
                "type": "multichoice",
                "title": "機械学習の定義",
                "question": "「機械学習」の説明として適切なのはどれか。",
                "options": [
                    "大量の計算を高速に実行する技術",
                    "データから自動的に規則性や知識を獲得する技術",
                    "人間の直感や常識を直接プログラムとして記述する技術",
                    "大量の知識をルールとして手作業で登録する技術"
                ],
                "answer": "B",
                "feedback": {
                    "A": "これは計算機の性能に関する説明です。",
                    "B": "正解です。これが機械学習の本質です。",
                    "C": "これはルールベースの手法に近い説明です。",
                    "D": "これは第2次AIブームのエキスパートシステムです。"
                }
            },
            {
                "type": "multichoice",
                "title": "ラベルの意味（難問）",
                "question": "以下の学生の中で、「ラベル」の説明が唯一正しいのは誰か？\n\nAさん：「ラベル」は必ずカテゴリー名で、数値予測には不適。  \nBさん：「ラベル」は予測される変数で、質的・量的どちらも含む。  \nCさん：「ラベル」は特徴量の一種で、入力データ。  \nDさん：「ラベル」は真の値で、誤差がない。",
                "options": ["Aさん", "Bさん", "Cさん", "Dさん"],
                "answer": "B",
                "feedback": {
                    "A": "数値予測にもラベルは使われます。",
                    "B": "正解です。ラベルとは予測対象変数のことです。",
                    "C": "特徴量とラベルを混同しています。",
                    "D": "ラベルは観測値であり、誤差も含むことがあります。"
                }
            }
        ]

        # Create an instance of YesNoQuiz and parse the YAML data
        quiz = YesNoQuiz()
        parsed_data = quiz.parse_yaml(yaml_data)

        # Expected output structure (simplified for demonstration)
        expected_output = [
            {
                "type": "multichoice",
                "title": "機械学習の定義",
                "question": "「機械学習」の説明として適切なのはどれか。",
                "options": [
                    "大量の計算を高速に実行する技術",
                    "データから自動的に規則性や知識を獲得する技術",
                    "人間の直感や常識を直接プログラムとして記述する技術",
                    "大量の知識をルールとして手作業で登録する技術"
                ],
                "answer": "B",
                "feedback": {
                    "A": "これは計算機の性能に関する説明です。",
                    "B": "正解です。これが機械学習の本質です。",
                    "C": "これはルールベースの手法に近い説明です。",
                    "D": "これは第2次AIブームのエキスパートシステムです。"
                }
            },
            {
                "type": "multichoice",
                "title": "ラベルの意味（難問）",
                "question": "以下の学生の中で、「ラベル」の説明が唯一正しいのは誰か？\n\nAさん：「ラベル」は必ずカテゴリー名で、数値予測には不適。  \nBさん：「ラベル」は予測される変数で、質的・量的どちらも含む。  \nCさん：「ラベル」は特徴量の一種で、入力データ。  \nDさん：「ラベル」は真の値で、誤差がない。",
                "options": ["Aさん", "Bさん", "Cさん", "Dさん"],
                "answer": "B",
                "feedback": {
                    "A": "数値予測にもラベルは使われます。",
                    "B": "正解です。ラベルとは予測対象変数のことです。",
                    "C": "特徴量とラベルを混同しています。",
                    "D": "ラベルは観測値であり、誤差も含むことがあります。"
                }
            }
        ]

        self.assertEqual(parsed_data, expected_output)

if __name__ == "__main__":
    unittest.main()
