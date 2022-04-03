from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from collections import defaultdict

class Oracle():

    def __init__(self, question, paragraph):
        self.question_text = question["question_text"]
        self.question_answer_choices = question["answer_choices"]
        self.question_type = question["question_type"]
        self.paragraph = paragraph
        model_name = "deepset/tinyroberta-squad2"
        #model_name = "deepset/roberta-base-squad2"
        self.nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    
    def multiple_choice(self, paragraphs, whole_text):
        best_score = 0
        best_ans = ""

        for parag in paragraphs:
            if len(parag) < 4:
                continue

            QA_input = {
                'question': self.question_text,
                'context': parag,
            }
            res = self.nlp(QA_input)
            
            if res["score"] > 0.95 and res["answer"] in self.question_answer_choices:
                return res["answer"].strip("\"")
            if res["score"] > best_score and res["answer"] in self.question_answer_choices:
                best_score = res["score"]
                best_ans = res["answer"]
        if best_ans == "":
            max_freq = 0
            for ans in self.question_answer_choices:
                freq = whole_text.count(ans)
                if freq > max_freq:
                    max_freq = freq
                    best_ans = ans
        return best_ans

    def direct_answer(self, paragraphs):
        best_score = 0
        best_ans = ""

        for parag in paragraphs:
            if len(parag) < 4:
                continue

            QA_input = {
                'question': self.question_text,
                'context': parag,
            }
            res = self.nlp(QA_input)

            if res["score"] > 0.95:
                return res["answer"].strip("\"")
            if res["score"] > best_score:
                best_score = res["score"]
                best_ans = res["answer"]
   
        return best_ans

    def answer(self):
        whole_text = self.paragraph
        if len(whole_text) == 0:
            return "Noapte buna gigi"

        paragraphs = whole_text.split("\n")
        
        if self.question_type == "multiple_choice":
            best_ans = self.multiple_choice(paragraphs, whole_text)
        else: 
            best_ans = self.direct_answer(paragraphs)

        return best_ans
            
# with open('paragraph.txt', 'r', encoding="utf-8") as f:
#         paragraph = f.read()  

# oracle = Oracle("Where is the northernmost point of land in the world?", paragraph)
# print(oracle.answer())
        


