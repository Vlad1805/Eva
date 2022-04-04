from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from collections import defaultdict
import time

class Oracle():

    def __init__(self, question, paragraph):
        self.question_text = question["question_text"]
        self.question_answer_choices = question["answer_choices"]
        self.question_type = question["question_type"]
        self.paragraph = paragraph
        model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
        self.nlp = pipeline('question-answering', model=model_name, tokenizer=model_name, batch_size=256)
    
    def multiple_choice(self, paragraphs):
        start_counter1 = time.time()
        best_score = 0
        best_ans = ""
        for i in range(0, len(paragraphs), 2):
            end_counter1 = time.time()

            if end_counter1 - start_counter1 > 55:
                return best_ans

            if i == (len(paragraphs) - 1):
                i -= 3
            parag = paragraphs[i] + paragraphs[i+1]
            if len(parag) < 4:
                continue

            QA_input = {
                'question': self.question_text,
                'context': parag,
            }
            res = self.nlp(QA_input)
            
            if res["score"] > 0.82 and res["answer"] in self.question_answer_choices:
                return res["answer"].strip("\"")
            if res["score"] > best_score and res["answer"] in self.question_answer_choices:
                best_score = res["score"]
                best_ans = res["answer"]
            
        if best_ans == "":
            best_ans = self.question_answer_choices[0]
        return best_ans

    def direct_answer(self, paragraphs):
        start_counter2 = time.time()
        best_score = 0
        best_ans = ""

        for i in range(0, len(paragraphs), 2):
            end_counter2 = time.time()
            if end_counter2 - start_counter2 > 55:
                return best_ans
            if i == (len(paragraphs) - 1):
                i -= 3
            parag = paragraphs[i] + paragraphs[i+1]
            if len(parag) < 4:
                continue

            QA_input = {
                'question': self.question_text,
                'context': parag,
            }
            res = self.nlp(QA_input)

            if res["score"] > 0.82:
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
            best_ans = self.multiple_choice(paragraphs)
        else: 
            best_ans = self.direct_answer(paragraphs)

        return best_ans
            
# with open('paragraph.txt', 'r', encoding="utf-8") as f:
#         paragraph = f.read()  

# oracle = Oracle("Where is the northernmost point of land in the world?", paragraph)
# print(oracle.answer())
        





# with open('paragraph.txt', 'r', encoding="utf-8") as f:
#         paragraph = f.read()

# oracle = Oracle("What is the capital of Romania?", paragraph)


