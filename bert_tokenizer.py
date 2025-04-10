from transformers import BertTokenizer

bert_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
input_sentence = "Lets see how this works Rono Savio"

bert_tokens = bert_tokenizer.tokenize(input_sentence)
print(bert_tokens)

print("Now we are working on test branch ")