import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer

class Oracle():

    def __init__(self, question, paragraph):
        self.question = question
        self.paragraph = paragraph
        #Model
        self.model = (BertForQuestionAnswering
        .from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad',return_dict=False))
        #Tokenizer
        self.tokenizer = (BertTokenizer
        .from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad'))
    
    def answer(self):
        encoding = self.tokenizer.encode_plus(text=self.question,text_pair=self.paragraph, add_special=True)
 
        inputs = encoding['input_ids']  #Token embeddings
        sentence_embedding = encoding['token_type_ids']  #Segment embeddings
        tokens = self.tokenizer.convert_ids_to_tokens(inputs) #input tokens
        
        start_scores, end_scores = self.model(input_ids=torch.tensor([inputs]), token_type_ids=torch.tensor([sentence_embedding]))
        
        start_index = torch.argmax(start_scores)
        
        end_index = torch.argmax(end_scores)
        
        answer = ' '.join(tokens[start_index:end_index+1])

        return answer.strip("\"")


