import os
from openai import OpenAI
import docx

def load_prompt(prompt_path: str) -> str:
    """Reads the prompt file and returns its content as a string."""
    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_news(input_folder: str) -> list:
    """
    Returns a list of tuples (file_name, text_content).
    Each .txt file inside the input_folder is loaded.
    """
    files = []
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.txt'):
            file_path = os.path.join(input_folder, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            files.append((file_name, content))
    return files

def generate_summary(client: OpenAI, text: str, prompt: str, model: str = "gpt-4") -> dict:
    """
    Sends the text to OpenAI's API to generate a summary in Portuguese
    according to the instructions in the prompt.

    Returns:
        dict: A dictionary with keys 'title' and 'content'.
    """
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": text}
    ]
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=1000
    )

    full_summary = response.choices[0].message.content.strip()
    
    # The prompt must ensure that the first line contains the title
    lines = full_summary.split("\n", 1)
    title = lines[0].strip() if lines else "No Title"
    content = lines[1].strip() if len(lines) > 1 else "No Content"
    
    return {"title": title, "content": content}

def save_summary_as_word(output_folder: str, file_name: str, summary: dict):
    """
    Saves the summary into a .docx file inside the 'output_folder'
    using python-docx, applying the specified format:
    
    - Title: Bold text (from `summary['title']`).
    - Content: Normal text (from `summary['content']`).
    """
    # Create a Document object
    doc = docx.Document()
    
    # Add the title (bold)
    title_paragraph = doc.add_paragraph()
    title_run = title_paragraph.add_run(summary["title"])
    title_run.bold = True
    
    # Add the content (normal text)
    content_paragraph = doc.add_paragraph(summary["content"])
    
    # OPTIONAL: Add a separator line
    doc.add_paragraph("________________________________________")

    # Save file with .docx extension
    output_path = os.path.join(output_folder, file_name)
    doc.save(output_path)