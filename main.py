from langchain_community.llms import Ollama 
from youtube import youtube_transcript
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="llama3.1")
yt_transcript = youtube_transcript()

prompt_template = PromptTemplate(
    input_variables=["transcript"],
    template = """Read through the entire transcript carefully.
          Provide a concise summary of the video's main topic and purpose.
            Extract and list the five most interesting or important points from the transcript. For each point: State the key idea in a clear and concise manner.

         - Ensure your summary and key points capture the essence of the video without including unnecessary details.
         - Use clear, engaging language that is accessible to a general audience.
         - If the transcript includes any statistical data, expert opinions, or unique insights, prioritize including these in your summary or key points.
 
         video transcript: {transcript}"""
)

result = llm.invoke(prompt_template.format(transcript=yt_transcript))

# chain = LLMChain(llm=llm, prompt=prompt_template)
# result = chain.invoke({
#     "transcript" : yt_transcript
# })

print(result)
