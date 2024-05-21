from dotenv import load_dotenv
import os
import ast
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
from helpers.prompts import new_prompt, instruction_str, context
from helpers.note_engine import note_engine_
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI
from helpers.pdf import (chap1_engine, chap2_engine, chap3_engine, chap4_engine, chap5_engine,
                 chap6_engine, chap7_engine, chap8_engine, chap9_engine, chap10_engine,
                 chap11_engine, chap12_engine, chap13_engine, chap14_engine, chap15_engine,
                 chap16_engine, chap17_engine, chap18_engine, chap19_engine, chap20_engine, chap21_engine, chap22_engine,
                 chap23_engine, chap24_engine, chap25_engine, chap26_engine, chap27_engine,
                 chap28_engine, chap29_engine, chap30_engine, chap31_engine, chap32_engine, chap33_engine)

from descriptions import (chap1_desc, chap2_desc, chap3_desc, chap4_desc, chap5_desc, chap6_desc, chap7_desc,
                          chap8_desc, chap9_desc, chap10_desc, chap11_desc, chap12_desc, chap13_desc,chap14_desc,chap15_desc,
                          chap16_desc, chap17_desc, chap18_desc, chap19_desc, chap20_desc, chap21_desc, chap22_desc,
                          chap23_desc, chap24_desc, chap25_desc, chap26_desc, chap27_desc, chap28_desc, chap29_desc,
                          chap30_desc, chap31_desc, chap32_desc, chap33_desc)

load_dotenv()

population_path = os.path.join("./data", "population.csv")
population_df = pd.read_csv(population_path)

population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str
)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})

tools = [
    note_engine_,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="This gives information at the world population and demographics",
        ),
    ),
    # Chapter 1
    QueryEngineTool(
        query_engine=chap1_engine,
        metadata=ToolMetadata(
            name="M1_chap1_pdf",
            description= chap1_desc,
            
        ),
        
    ),
    # Chapter 2 
    QueryEngineTool(
        query_engine=chap2_engine,
        metadata=ToolMetadata(
            name="M1_chap3_pdf",
            description= chap2_desc,
        ),
    ),
     # Chapter 3 
    QueryEngineTool(
        query_engine=chap3_engine,
        metadata=ToolMetadata(
            name="M1_Script_Video_1_1",
            description= chap3_desc,
        ),
    ),
     # Chapter 4 
    QueryEngineTool(
        query_engine=chap4_engine,
        metadata=ToolMetadata(
            name="M1_Script_Video_1_2",
            description= chap4_desc,
        ),
    ),
     # Chapter 5 
    QueryEngineTool(
        query_engine=chap5_engine,
        metadata=ToolMetadata(
            name="M1_Script_Video_1_3",
            description=chap5_desc,
        ),
    ),
    # Chapter 6 
    QueryEngineTool(
        query_engine=chap6_engine,
        metadata=ToolMetadata(
            name="M1_Script_Video_1_4",
            description=chap6_desc,
        ),
    ),
    # Chapter 7 
    QueryEngineTool(
        query_engine=chap7_engine,
        metadata=ToolMetadata(
            name="M1_Script_Video_1_5",
            description=chap7_desc,
        ),
    ),
    # Chapter 8 
    QueryEngineTool(
        query_engine=chap8_engine,
        metadata=ToolMetadata(
            name="M2_Chap6_pdf",
            description=chap8_desc,
        ),
    ),
    # Chapter 9 
    QueryEngineTool(
        query_engine=chap9_engine,
        metadata=ToolMetadata(
            name="M2_Chap7_pdf",
            description=chap9_desc,
        ),
    ),
    # Chapter 10 
    QueryEngineTool(
        query_engine=chap10_engine,
        metadata=ToolMetadata(
            name="M2_Chap8_pdf",
            description=chap10_desc,
                            
        ),
    ),
     # Chapter 11 
    QueryEngineTool(
        query_engine=chap11_engine,
        metadata=ToolMetadata(
            name="M2_Chap9_pdf",
            description=chap11_desc,
                            
        ),
    ),
     # Chapter 12 
    QueryEngineTool(
        query_engine=chap12_engine,
        metadata=ToolMetadata(
            name="M2_Script_Video_2_1",
            description=chap12_desc,
                            
        ),
    ),
     # Chapter 13 
    QueryEngineTool(
        query_engine=chap13_engine,
        metadata=ToolMetadata(
            name="M2_Script_Video_2_2",
            description=chap13_desc,
                            
        ),
    ),
     # Chapter 14 
    QueryEngineTool(
        query_engine=chap14_engine,
        metadata=ToolMetadata(
            name="M2_Script_Video_2_3",
            description=chap14_desc,
                            
        ),
    ),
     # Chapter 15 
    QueryEngineTool(
        query_engine=chap15_engine,
        metadata=ToolMetadata(
            name="M1_M3_Chap3_pdf",
            description=chap15_desc,
                            
        ),
    ),
     # Chapter 16 
    QueryEngineTool(
        query_engine=chap16_engine,
        metadata=ToolMetadata(
            name="M2_M3_Chap7_pdf",
            description=chap16_desc,
                            
        ),
    ), 
    # Chapter 17 
    QueryEngineTool(
        query_engine=chap17_engine,
        metadata=ToolMetadata(
            name="M3_Chap11_pdf",
            description=chap17_desc,
                            
        ),
    ), 
    # Chapter 18 
    QueryEngineTool(
        query_engine=chap18_engine,
        metadata=ToolMetadata(
            name="M3_Chap12_pdf",
            description=chap18_desc,
                            
        ),
    ), 
    # Chapter 19 
    QueryEngineTool(
        query_engine=chap19_engine,
        metadata=ToolMetadata(
            name="M3_Script_Video_3_1",
            description=chap19_desc,
                            
        ),
    ), 
    # Chapter 20 
    QueryEngineTool(
        query_engine=chap20_engine,
        metadata=ToolMetadata(
            name="M3_Script_Video_3_2",
            description=chap20_desc,
                            
        ),
    ), 
    # Chapter 21 
    QueryEngineTool(
        query_engine=chap21_engine,
        metadata=ToolMetadata(
            name="M3_Script_Video_3_3",
            description=chap21_desc,
                            
        ),
    ),
     # Chapter 22 
    QueryEngineTool(
        query_engine=chap22_engine,
        metadata=ToolMetadata(
            name="M3_Script_Video_3_4",
            description=chap22_desc,
                            
        ),
    ),
     # Chapter 23 
    QueryEngineTool(
        query_engine=chap23_engine,
        metadata=ToolMetadata(
            name="M4_Chap13_pdf",
            description=chap23_desc,
                            
        ),
    ),
       # Chapter 24 
    QueryEngineTool(
        query_engine=chap24_engine,
        metadata=ToolMetadata(
            name="M4_Script_Video_4_1",
            description=chap24_desc,
                            
        ),
    ),
        # Chapter 25 
    QueryEngineTool(
        query_engine=chap25_engine,
        metadata=ToolMetadata(
            name="M4_Script_Video_4_2",
            description=chap25_desc,
                            
        ),
    ),
        # Chapter 26
    QueryEngineTool(
        query_engine=chap26_engine,
        metadata=ToolMetadata(
            name="M5_Chap14_pdf",
            description=chap26_desc,
                            
        ),
    ),
        # Chapter 27
    QueryEngineTool(
        query_engine=chap27_engine,
        metadata=ToolMetadata(
            name="M5_Script_Video_5_1",
            description=chap27_desc,
                            
        ),
    ),
        # Chapter 28
    QueryEngineTool(
        query_engine=chap28_engine,
        metadata=ToolMetadata(
            name="M5_Script_Video_5_2",
            description=chap28_desc,
                            
        ),
    ),
        # Chapter 29
    QueryEngineTool(
        query_engine=chap29_engine,
        metadata=ToolMetadata(
            name="M5_Script_Video_5_3",
            description=chap29_desc,
                            
        ),
    ),
        # Chapter 30
    QueryEngineTool(
        query_engine=chap30_engine,
        metadata=ToolMetadata(
            name="M5_Chap15_pdf",
            description=chap30_desc,
                            
        ),
    ),
        # Chapter 31
    QueryEngineTool(
        query_engine=chap31_engine,
        metadata=ToolMetadata(
            name="M6_Script_Video_6_1",
            description=chap31_desc,
                            
        ),
    ),
        # Chapter 32
    QueryEngineTool(
        query_engine=chap32_engine,
        metadata=ToolMetadata(
            name="M6_Script_Video_6_2",
            description=chap32_desc,
                            
        ),
    ),
        # Chapter 33
    QueryEngineTool(
        query_engine=chap33_engine,
        metadata=ToolMetadata(
            name="M6_Script_Video_6_3",
            description=chap33_desc,
                            
        ),
    ),
    
]

