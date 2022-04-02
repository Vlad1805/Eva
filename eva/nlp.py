import spacy

# Load English tokenizer, tagger, parser and NER
class NLP():
    def __init__(self, question):
        self.nlp = spacy.load("en_core_web_md")
        self.question = question
    # Process whole documents
    def process(self):
        doc = self.nlp(self.question)

        # Analyze syntax
        print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
        print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

        # Find named entities, phrases and concepts
        for entity in doc.ents:
            print(entity.text, entity.label_)

nlp = NLP("What is the biggest country in Europe?")
nlp.process();