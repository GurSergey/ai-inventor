
from config import get_config
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer


class T5BaseClass:
    def __init__(self):
        path_to_model = get_config()['models-path'] + '/' + 't5base'
        self.tokenizer = T5Tokenizer.from_pretrained(path_to_model)
        self.model = T5ForConditionalGeneration.from_pretrained(path_to_model)
        self.model.to(torch.device('cpu'))
        self.model.eval()

    def answer(self, question, **kwargs):
        inputs = self.tokenizer(question, return_tensors='pt').to(self.model.device)
        with torch.no_grad():
            hypotheses = self.model.generate(**inputs, num_beams=7, min_length=100, max_length=512,
                                             repetition_penalty=2.0, length_penalty=1.0, early_stopping=True,
                                             no_repeat_ngram_size=3, num_return_sequences=5,
                                             **kwargs)
        return [self.tokenizer.decode(hypothesis, skip_special_tokens=True) for hypothesis in hypotheses]
