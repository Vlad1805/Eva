from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline



class Oracle():

    def __init__(self, question, paragraph):
        self.question = question
        self.paragraph = paragraph
        model_name = "deepset/tinyroberta-squad2"
        self.nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    
    def answer(self):
        try:
            QA_input = {
                'question': self.question,
                'context': self.paragraph,
            }
            res = self.nlp(QA_input)
            return res["answer"].strip("\"")
        except:
            return "Noapte buna gigi"


