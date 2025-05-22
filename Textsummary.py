
import torch
import gradio
from transformers import pipeline

# Use the model ID from the Hugging Face Hub
text_summary = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6",
                        torch_dtype=torch.bfloat16)






# Example text
# text = '''Costello's (also known as Tim's) was a bar and restaurant in Midtown Manhattan,
#     New York City, from 1929 to 1992. The bar operated at several locations near the intersection
#  of East 44th Street and Third Avenue. Costello's was known as a drinking spot for journalists with the
#   New York Daily News, writers with The New Yorker, novelists, and cartoonists, including the author Ernest Hemingway,
#   the cartoonist James Thurber, the journalist John McNulty, the poet Brendan Behan, the short-story writer John O'Hara,
#   and the writers Maeve Brennan and A. J. Liebling. The bar is also known for having been home to a wall where Thurber drew a
#   cartoon depiction of the "Battle of the Sexes" at some point between 1934 and 1935; the cartoon was destroyed, illustrated again,
#   and then lost in the 1990s. A wall illustrated in 1976 by several cartoonists, including Bill Gallo, Stan Lee, Mort Walker,
#    Al Jaffee, Sergio Aragonés, and Dik Browne, is still on display at the bar's final location.'''
#
# # Print the summary
# print(text_summary(text))


#we are writing this function gardio accepts function, this function will return the output
def summary(input):
    output = text_summary(input)
    return output[0]['summary_text']


gradio.close_all()

# demo = gradio.Interface(fn=summuray,inputs="text",outputs="text")

demo = gradio.Interface(fn=summary,
                        inputs=[gradio.Textbox(label="Input text to summarize",lines=6)],
                        outputs=[gradio.Textbox(label="Summarized text", lines=4)],
                        title="@GenAi Project 1: Text Summarizer",
                        description="THis application can used for summarizing the text")

demo.launch()