from llama_index.prompts import PromptTemplate


instruction_str = """\
    1. Analyse and Understand the question.
    2. Search the response by analyzing the description of each tool.
    3. The result should represent a solution to the query.
    4. YOU HAVE TO RETURN MORE THAN 1 TOOLS WHERE POSSIBLE.
    5. IF YOU HAVE NOT GOTTEN SUFFICIENT INFORMATION SAY YOU HAVE NOT FOUND THE RESULT.
    6. Do not quote the expression."""

# new_prompt = PromptTemplate(
#     """\
#     You are working with a pandas dataframe in Python.
#     The name of the dataframe is `df`.
#     This is the result of `print(df.head())`:
#     {df_str}

#     Follow these instructions:
#     {instruction_str}
#     Query: {query_str}

#     Expression: """
# )

new_prompt = PromptTemplate(
    """\
    You are working with a book in pdf containing courses about marketing, splitted into different chapter:
    

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

# context = """Purpose: The primary role of this agent is to assist users by providing accurate 
#             information about world population statistics and details about a country. """

context = """
1. Analyser et comprendre la question.
2. Rechercher la réponse en analysant la description de chaque outil.
3. Le résultat devrait représenter une solution à la requête.
4. VOUS DEVEZ RETOURNER PLUS D'UN OUTIL LORSQUE C'EST POSSIBLE.
5. SI VOUS N'AVEZ PAS SUFFISAMMENT D'INFORMATION, INDIQUEZ QUE VOUS N'AVEZ PAS TROUVÉ LE RÉSULTAT.
6. Ne pas citer l'expression.
7. TU DOIS REPONDRE EN FRANCAIS.
But : Le rôle principal de cet agent est d'aider les utilisateurs en fournissant des informations précises et en répondant à propos 
du livre de marketing. Différents chapitres de livre sont fournis et chacun contient un sujet spécifique. 
La réponse ou la solution peut être trouvée dans plus d'un outil, dans ce cas, retournez toutes les sources. 
Utilisez des puces pour formater la réponse si nécessaire.

 """