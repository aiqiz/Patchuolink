import openai
openai.api_key = "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"
system = [{"role": "system",
           "content": "You are chatbot who enjoys python programming."}]
user = [{"role": "user", "content": "brief introduction?"}]
chat = []
while not user[0]['content'] == "exit":
    response = openai.ChatCompletion.create(
        messages = system + chat[-20:] + user,
        model="gpt-3.5-turbo", top_p=0.5, stream=True)
    reply = ""
    for delta in response:
        if not delta['choices'][0]['finish_reason']:
            word = delta['choices'][0]['delta']['content']
            reply += word
            print(word, end ="")
    chat += user + [{"role": "assistant", "content": reply}]
    user = [{"role": "user", "content": input("\nPrompt: ")}]