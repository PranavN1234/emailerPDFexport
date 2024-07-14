from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from Billoflading import BillOfLadingData
import openai
import os
from dotenv import load_dotenv

load_dotenv()

def read_text_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def extract_bol_data(file_path):
    # Read the text file
    file_content = read_text_file(file_path)

    # Print the content (for debugging, can be removed in production)

    # Initialize the parser with the Pydantic model
    parser = JsonOutputParser(pydantic_object=BillOfLadingData)
    format_response_parser = parser.get_format_instructions()

    # Define the prompt template
    prompt_template = '''Extract the following information from the text:
    {format_instructions}
    Text:
    {text}'''

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["text"],
        partial_variables={"format_instructions": format_response_parser}
    )

    # Generate the formatted prompt with the text file content
    formatted_prompt = prompt.format(text=file_content)

    # Load the OpenAI API key from environment variables
    api_key = os.getenv('OPENAI_API_KEY')

    if not api_key:
        raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

    # Send the request to OpenAI
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": formatted_prompt}
        ],
        temperature=0.0,
    )

    print(response.choices[0].message.content)
    output = response.choices[0].message.content
    
   
    parsed_output = parser.parse(output)
    
   
    return parsed_output

# Path to your text file
text_file_path = "data.txt"

# Extract and print the parsed Bill of Lading data
parsed_data = extract_bol_data(text_file_path)
print(parsed_data)
