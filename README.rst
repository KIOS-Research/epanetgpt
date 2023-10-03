=========
epanetgpt
=========


.. image:: https://img.shields.io/pypi/v/epanetgpt.svg
        :target: https://pypi.python.org/pypi/epanetgpt

.. image:: https://img.shields.io/travis/mariosmsk/epanetgpt.svg
        :target: https://travis-ci.com/mariosmsk/epanetgpt

.. image:: https://readthedocs.org/projects/epanetgpt/badge/?version=latest
        :target: https://epanetgpt.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

epanetgpt is a Python package designed to enable users to interact with their EPANET input files through natural language conversations. Inspired by pdfgpt, its objective is to suggest/run code snippets.

How to install
---------------

**Environments -> base (root) -> open terminal -> pip install epanetgpt**

* pip install epanetgpt

Example
-------

.. code-block:: python

    from epanetgpt import EPANETBot

    d = EPANETBot(openai_key='************************************')

    print('Example:')
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

.. code-block:: none

    Example:

    USER: Give me a summary of the water network? junctions, pipes, pumps etc.

    AI

    Summary of the water network based on the provided data:

    Junctions:
    - Junction 10 is at elevation 710 with no demand.
    - Junction 11 is at elevation 710 with a demand of 150.
    - Junction 12 is at elevation 700 with a demand of 150.
    - Junction 13 is at elevation 695 with a demand of 100.
    - Junction 21 is at elevation 700 with a demand of 150.
    - Junction 22 is at elevation 695 with a demand of 200.
    - Junction 23 is at elevation 690 with a demand of 150.
    - Junction 31 is at elevation 700 with a demand of 100.
    - Junction 32 is at elevation 710 with a demand of 100.

    Reservoirs:
    - Reservoir 9 has a head of 800.

    Tanks:
    - Tank 2 has an elevation of 850, an initial level of 120, a minimum level of 100, a maximum level of 150, a diameter of 50.5, and no volume curve specified.

    Pipes:
    - Pipe 10 connects junction 10 to junction 11 with a length of 10530, a diameter of 18, a roughness of 100, and no minor loss. The pipe is open.
    - Pipe 11 connects junction 11 to junction 12 with a length of 5280, a diameter of 14, a roughness of 100, and no minor loss. The pipe is open.
    - Pipe 12 connects junction 12 to junction 13 with a length of 5280, a diameter of 10, a roughness of 100, and no minor loss. The pipe is open.
    - Pipe 21 connects junction 21 to junction 22 with a length of 5280, a diameter of 10, a roughness of 100, and no minor loss. The pipe is open.
    - Pipe 22 connects junction 22 to junction 23 with a length of 5280, a diameter of 12, a roughness of 100, and no minor loss. The pipe is open.
    - Pipe 31 connects junction 31 to junction 32 with a length of 5280, a diameter of 6, a roughness of 100, and no minor loss. The pipe is open.
    - Pipe 110 connects tank 2 to junction 12 with a length of 200, a diameter of 18, a roughness of 100, and no minor loss. The pipe is open.
    - Pipe 111 connects junction 11 to junction 21 with a length of 5280, a diameter of 10, a roughness of 100, and no minor loss. The pipe is open.
    - Pipe 112 connects junction 12 to junction 22 with a length of 5280, a diameter of 12, a roughness of 100, and no minor loss. The pipe is open.
    - Pipe 113 connects junction 13 to junction 23 with a length of 5280, a diameter of 8, a roughness of 100, and no minor loss. The pipe is open.
    - Pipe 121 connects junction 21 to junction 31 with a length of 5280, a diameter of 8, a roughness of 100, and no minor loss. The pipe is open.
    - Pipe 122 connects junction 22 to junction 32 with a length of 5280, a diameter of 6, a roughness of 100, and no minor loss. The pipe is open.

    Pumps:
    - Pump 9 is connected from node 9 to node 10 with the parameter "HEAD 1".

    Valves:
    - No valve information specified.

    Demand Patterns:
    - Two demand patterns are specified. The first pattern has multipliers 1.0, 1.2, 1.4, 1.6, 1.4, and 1.2. The second pattern has multipliers 1.0, 0.8, 0.6, 0.4, 0.6, and 0.8.

    Curves:
    - Curve 1 has X-Value 1500 and Y-Value 250. It represents the pump curve for Pump 9.

    Controls:
    - There is a control specified that opens link 9 if node 2 is below 110 and closes it if node 2 is above 140.

    Energy:
    - Global efficiency is specified as 75.
    - Global price is specified as 0.0.
    - Demand charge is specified as 0.0.

    Emitters:
    - No emitter information specified.

    Quality:
    - Initial quality is specified for all junctions (10, 11, 12, 13, 21, 22, 23, 31, 32) and tanks (9, 2).

    Sources:
    - No source information specified.

    Reactions:
    - Reaction coefficients are specified for bulk, tank, and wall reactions.


* Free software: MIT license
* Documentation: https://epanetgpt.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
