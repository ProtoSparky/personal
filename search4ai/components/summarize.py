from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize(text, language="english", sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join([str(sentence) for sentence in summary])

import components.tokenfuckoff as tk
def summarize_ai(text, context, sentences_count, ai_model, ai_api):
    #summarization using AI
    import datetime
    from ollama import Client
    current_datetime = datetime.datetime.now()
    system_promt = """You are an AI summarization tool. 
    Your job is to summarize text from the conversation the same way a human would do it, using context to look for relevant information that answers the user's question. 
    You will stick to the maximum summary length of """  + str(sentences_count) + """ sentence(s), 
    and yet you will bring forward relevant information without compromising on your summary quality. 
    You will NEVER add information that was not presented in the first place.
    You will ONLY reply with the summary of the text
    The current system time is
    """ + current_datetime.strftime("%Y-%m-%d %H:%M") + " as YYYY-MM-DD HH:MM:SS."
    msg = []
    sys_msg = {"role": "system", "content": system_promt}
    msg.append(sys_msg)


    usr_msg = {"role": "user", "content": '"'}
    msg.append(usr_msg)

    usr_txt = tk.chunkenizer(text)
    for current_txt in usr_txt:
        usr_msg = {"role": "user", "content": current_txt}
        msg.append(usr_msg)

    usr_msg = {"role": "user", "content": '"' + context}
    msg.append(usr_msg)


    response = Client(ai_api).chat(model=ai_model, messages=msg)
    clean_response = response["message"]["content"]
    return clean_response


