from epanetgpt import EPANETBot

d = EPANETBot(openai_key='************************************')

print('Example')
inp_file_path = "Net1.inp"
pdf_file_path = "Net1.pdf"
resp = d.generatePDF(inp_file_path, pdf_file_path)
if resp:
    extracted_text, num_pages = d.generateText(file_path=pdf_file_path)
    df = d.generateEmbeddings(extracted_text)
    print('USER: Give me a summary of the water network? junctions, pipes, pumps etc.')
    prompt = d.generatePrompt(df, num_pages, 'Give me a summary of the water network? junctions, pipes, pumps etc.')
    response = d.sendPrompt(prompt, model="gpt-3.5-turbo")
    print('AI')
    print(response, '\n')
