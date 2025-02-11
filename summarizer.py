import os
from dotenv import load_dotenv
from openai import OpenAI
import utils

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

input_folder = "input"
output_folder = "output"
prompt_path = "prompt.txt"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

prompt_instructions = utils.load_prompt(prompt_path)

news = utils.load_news(input_folder)

for file_name, content in news:
    print(f"Generating summary for: {file_name} ...")

    summary = utils.generate_summary(client, content, prompt_instructions)
    output_file_name = file_name.replace(".txt", "_summary.docx")
    utils.save_summary_as_word(output_folder, output_file_name, summary)
    
    print(f"Summary saved to: {output_file_name}")