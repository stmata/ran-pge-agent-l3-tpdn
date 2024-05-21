from fastapi import FastAPI, HTTPException, Request, Query
from typing import Optional
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
import uvicorn
from dotenv import load_dotenv
import os
import ast
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI
from helpers.top_dowm import tools
from helpers.prompts import new_prompt, instruction_str, context
from collections import defaultdict
load_dotenv()


llm = OpenAI(model="gpt-3.5-turbo")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context, max_iterations=None)

# Define chapter dictionnary

chapters = {'': ''
            }

# Create FastAPI app
app = FastAPI()

class serverResponse(BaseModel):
    question: str
    response: str
    content: str
    source: list
# Model of Client input values
class userQuery(BaseModel):
    question: str

# Function to retrieve the extracted chunks to answer the question
def extract_chunk_content(agent_result):
     # Get text element from result source_nodes
    extracted_text = [entry.text for entry in agent_result.source_nodes]
    # Provided text
    text = extracted_text
    # Convert the text from list to string
    text = ''.join(text)
    # Removing "[" and "]" characters from the beginning and end of the text
    text = text[2:-1]
    # Replacing "\n" with new line
    text = text.replace('\n', '\n')
    # Splitting text into chapters
    chapters = text.split("CHAPTER")
    return text

@app.post("/process-data")
def process_data(query: userQuery):
    # Process the receive data
    print('Receiving user query ...')
    print(f'User input: {query.question}')
    result = agent.query(query.question)
    print(result)
    # Get Metadata
    metadata = [entry.metadata for entry in result.source_nodes]
    list_of_dicts = ast.literal_eval(str(metadata))
    scores = [entry.score for entry in result.source_nodes]
    print(list_of_dicts)
    # Extract peace of texts (chunks) used to respond
    chunks = extract_chunk_content(result) 
    # # Given dictionary
    # data = [{'page_label': '2', 'file_name': './data/Chap1.pdf'}, {'page_label': '11', 'file_name': './data/Chap1.pdf'}]

    # Extract and format the desired information
    formatted_sources = [f"{entry['file_name'].split('/')[-1].split('.')[0]} : Page label {entry['page_label']}" for entry in list_of_dicts]
    # Replacing Chapx with its corresponding value from the chapters dictionary
    formatted_sources_with_chapter_names = [chapters.get(source.split(" : ")[0], source.split(" : ")[0]) + " : Page label " + source.split(" : ")[1] for source in formatted_sources]
    # Cleaning up the source list to remove the duplicate "Page label" phrase and organizing by chapter
    chapter_pages = defaultdict(list)
    for item in formatted_sources_with_chapter_names:
        chapter_info, page_number = item.rsplit(' ', 3)[0], item.split()[-1]
        chapter_info = chapter_info.replace(" : Page label Page label", "")  # Clean up redundant "Page label"
        chapter_pages[chapter_info].append(page_number)
    # Adjusting the formatting to remove the repeated "Page label: Page label" issue
    bullet_list = [f"- {chapter} {', '.join(sorted(set(pages)))}" for chapter, pages in chapter_pages.items()]
    print(f'Formatted sources: {formatted_sources}')
    print(f'Formatted sources with chapters: {bullet_list}')
    print(scores)
    
    # return {'Response': {response}}
    return {'response' : result.response, 'sources':bullet_list, 'scores':scores, 'chunks': chunks}

# Launch the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8104))
    uvicorn.run(app, host="0.0.0.0", port=port)
