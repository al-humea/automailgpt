# si pas déjà dans les brouillons cherche et feed le texte dans les mails et dans les pdf

import openai

openai.api_key = open("./id.txt", "r").readlines()[2].strip().split(":")[1]
model_engine = "text-davinci-002"
context = open("./context.txt", "r").readlines()
for i, ctxt in enumerate(context):
	if (i > 3):
		break
	context[i] = ctxt.strip().split(":")[1]
print(context)
"""
prompt = (f" From now on you are an assistant for \"{context[0]}\", \"{context[1]}\" who is working in \"{context[2]}\".\nHere are the kind of exchanges that are expected from you : 
# Send the request to the API
response = openai.Completion.create(engine=model_engine, prompt=prompt)

# Print the generated text
print(response["choices"][0]["text"])
"""