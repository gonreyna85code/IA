from transformers import AutoModelWithLMHead, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("ncoop57/DiGPTame-medium")
model = AutoModelWithLMHead.from_pretrained("ncoop57/DiGPTame-medium")

# Let's chat for 100 lines
for step in range(100):
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(input(">> User:") + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

    #solve index out of range error
    if len(bot_input_ids) > 512:
        bot_input_ids = bot_input_ids[-512:]

    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(bot_input_ids, max_length=100, pad_token_id=tokenizer.eos_token_id)
    
    # pretty print last ouput tokens from bot
    print(">> Bot: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
