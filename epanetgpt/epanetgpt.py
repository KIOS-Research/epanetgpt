"""Main module."""
from pdfgpt import *
from fpdf import FPDF


class EPANETBot:

    def __init__(self, openai_key):
        openai.api_key = openai_key
        self.cnt = 4000
        self.pdfgpt_d = PDFBot(openai_key=openai_key)

    def generatePDF(self, inp_file_path=None, pdf_file_path=None):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=5)
        try:
            with open(inp_file_path, "r") as file:
                for line in file:
                    cleaned_line = line.strip().replace('\n', '').replace('\r', '')
                    pdf.cell(200, 2, txt=cleaned_line, ln=True)
        except FileNotFoundError:
            print(f"File not found: {inp_file_path}")
            return False
        pdf.output(pdf_file_path)
        return True

    def generateText(self, file_path=None, df=None):
        extracted_text, num_pages = self.pdfgpt_d.generateText(file_path=file_path, df=df)
        return extracted_text, num_pages

    def generateEmbeddings(self, extracted_text='', model_embeddings="text-embedding-ada-002"):
        df = self.pdfgpt_d.generateEmbeddings(extracted_text, model_embeddings=model_embeddings)
        return df

    def generatePrompt(self, df, num_pages, message, model_embeddings="text-embedding-ada-002"):
        prompt = self.pdfgpt_d.generatePrompt(df, num_pages, message, model_embeddings=model_embeddings)
        return prompt

    def sendPrompt(self, prompt, model="gpt-3.5-turbo", temperature=0.9, max_tokens=1500):
        response = self.pdfgpt_d.sendPrompt(prompt, model=model, temperature=temperature, max_tokens=max_tokens)
        return response
