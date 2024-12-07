from langchain_community.document_loaders import YoutubeLoader
url = str(input("Enter youtube url: "))


loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
content = loader.load()

def youtube_transcript():
    transcript = ''
    for each in content:
        transcript += each.page_content
    return transcript

