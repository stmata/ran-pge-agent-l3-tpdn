import os
from llama_index import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers import PDFReader
from dotenv import load_dotenv

load_dotenv()
def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index

path = './data'

'''    Module1  '''


'''
Chap 1
'''
pdf_path = os.path.join(path, "Chapter 1.pdf")
chap1_pdf = PDFReader().load_data(file=pdf_path)
chap1_index = get_index(chap1_pdf, "M1_chap1_pdf")
chap1_engine = chap1_index.as_query_engine()

'''
Chap 2
'''
pdf_path = os.path.join("data", "Chapter 3.pdf")
chap2_pdf = PDFReader().load_data(file=pdf_path)
chap2_index = get_index(chap2_pdf, "M1_chap3_pdf")
chap2_engine = chap2_index.as_query_engine()

'''
Chap 3
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 1_1 - QU'EST-CE QUE LE MARKETING.pdf")
chap3_pdf = PDFReader().load_data(file=pdf_path)
chap3_index = get_index(chap3_pdf, "M1_Script_Video_1_1")
chap3_engine = chap3_index.as_query_engine()

'''
Chap 4
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 1_2 - MARKETING STRATEGIQUE ET OPERATIONNEL.pdf")
chap4_pdf = PDFReader().load_data(file=pdf_path)
chap4_index = get_index(chap4_pdf, "M1_Script_Video_1_2")
chap4_engine = chap4_index.as_query_engine()

'''
Chap 5
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 1_3 - MARKETING MARCHAND NON MARCHAND SOCIAL.pdf")
chap5_pdf = PDFReader().load_data(file=pdf_path)
chap5_index = get_index(chap5_pdf, "M1_Script_Video_1_3")
chap5_engine = chap5_index.as_query_engine()

'''
Chap 6
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 1_4 - LA NOTION DE BESOIN.pdf")
chap6_pdf = PDFReader().load_data(file=pdf_path)
chap6_index = get_index(chap6_pdf, "M1_Script_Video_1_4")
chap6_engine = chap6_index.as_query_engine()

'''
Chap 7
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 1_5 - LA NOTION DE CLIENT.pdf")
chap7_pdf = PDFReader().load_data(file=pdf_path)
chap7_index = get_index(chap7_pdf, "M1_Script_Video_1_5")
chap7_engine = chap7_index.as_query_engine()


''' Module 2'''

'''
Chap 8
'''
pdf_path = os.path.join("data", "Chapter 6.pdf")
chap8_pdf = PDFReader().load_data(file=pdf_path)
chap8_index = get_index(chap8_pdf, "M2_Chap6_pdf")
chap8_engine = chap8_index.as_query_engine()

'''
Chap 9
'''
pdf_path = os.path.join("data", "Chapter 7.pdf")
chap9_pdf = PDFReader().load_data(file=pdf_path)
chap9_index = get_index(chap9_pdf, "M2_Chap7_pdf")
chap9_engine = chap9_index.as_query_engine()

'''
Chap 10
'''
pdf_path = os.path.join("data", "Chapter 8.pdf")
chap10_pdf = PDFReader().load_data(file=pdf_path)
chap10_index = get_index(chap10_pdf, "M2_Chap8_pdf")
chap10_engine = chap10_index.as_query_engine()

'''
Chap 11
'''
pdf_path = os.path.join("data", "Chapter 9.pdf")
chap11_pdf = PDFReader().load_data(file=pdf_path)
chap11_index = get_index(chap11_pdf, "M2_Chap9_pdf")
chap11_engine = chap11_index.as_query_engine()

'''
Chap 12
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 2_1 - LA SEGMENTATION.pdf")
chap12_pdf = PDFReader().load_data(file=pdf_path)
chap12_index = get_index(chap12_pdf, "M2_Script_Video_2_1")
chap12_engine = chap12_index.as_query_engine()

'''
Chap 13
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 2_2 - LE CIBLAGE.pdf")
chap13_pdf = PDFReader().load_data(file=pdf_path)
chap13_index = get_index(chap13_pdf, "M2_Script_Video_2_2")
chap13_engine = chap13_index.as_query_engine()

'''
Chap 14
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 2_3 - LE POSITIONNEMENT.pdf")
chap14_pdf = PDFReader().load_data(file=pdf_path)
chap14_index = get_index(chap14_pdf, "M2_Script_Video_2_3")
chap14_engine = chap14_index.as_query_engine()


''' Module 3'''

'''
Chap 15
'''
pdf_path = os.path.join("data", "Chapter 3.pdf")
chap15_pdf = PDFReader().load_data(file=pdf_path)
chap15_index = get_index(chap15_pdf, "M3_Chap3_pdf")
chap15_engine = chap15_index.as_query_engine()

'''
Chap 16
'''
pdf_path = os.path.join("data", "Chapter 7.pdf")
chap16_pdf = PDFReader().load_data(file=pdf_path)
chap16_index = get_index(chap16_pdf, "M3_Chap7_pdf")
chap16_engine = chap16_index.as_query_engine()

'''
Chap 17
'''
pdf_path = os.path.join("data", "Chapter 11.pdf")
chap17_pdf = PDFReader().load_data(file=pdf_path)
chap17_index = get_index(chap17_pdf, "M3_Chap11_pdf")
chap17_engine = chap17_index.as_query_engine()

'''
Chap 18
'''
pdf_path = os.path.join("data", "Chapter 12.pdf")
chap18_pdf = PDFReader().load_data(file=pdf_path)
chap18_index = get_index(chap18_pdf, "M3_Chap12_pdf")
chap18_engine = chap18_index.as_query_engine()

'''
Chap 19
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 3_1 - LE PRODUIT VU COMME UN PANIER D'ATTRIBUTS.pdf")
chap19_pdf = PDFReader().load_data(file=pdf_path)
chap19_index = get_index(chap19_pdf, "M3_Script_Video_3_1")
chap19_engine = chap19_index.as_query_engine()
'''
Chap 20
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 3_2 - LA COURBE DE CYCLE DE VIE PRODUIT.pdf")
chap20_pdf = PDFReader().load_data(file=pdf_path)
chap20_index = get_index(chap20_pdf, "M3_Script_Video_3_2")
chap20_engine = chap20_index.as_query_engine()

'''
Chap 21
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 3_3 - LE CAS DES NOUVEAUX PRODUITS.pdf")
chap21_pdf = PDFReader().load_data(file=pdf_path)
chap21_index = get_index(chap21_pdf, "M3_Script_Video_3_3")
chap21_engine = chap21_index.as_query_engine()

'''
Chap 22
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 3_4 - LE NOM DE MARQUE.pdf")
chap22_pdf = PDFReader().load_data(file=pdf_path)
chap22_index = get_index(chap22_pdf, "M3_Script_Video_3_4")
chap22_engine = chap22_index.as_query_engine()

''' Module 4 '''

'''
Chap 23
'''
pdf_path = os.path.join("data", "Chapter 13.pdf")
chap23_pdf = PDFReader().load_data(file=pdf_path)
chap23_index = get_index(chap23_pdf, "M4_Chap13_pdf")
chap23_engine = chap23_index.as_query_engine()

'''
Chap 24
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 4_1- LE ROLE DE LA DISTRIBUTION.pdf")
chap24_pdf = PDFReader().load_data(file=pdf_path)
chap24_index = get_index(chap24_pdf, "M4_Script_Video_4_1")
chap24_engine = chap24_index.as_query_engine()

'''
Chap 25
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 4_2 - LA DISTRIBUTION EN LIGNE, HORS LIGNE ET MULTICANAL.pdf")
chap25_pdf = PDFReader().load_data(file=pdf_path)
chap25_index = get_index(chap25_pdf, "M4_Script_Video_4_2")
chap25_engine = chap25_index.as_query_engine()


''' Module 5 '''

'''
Chap 26
'''
pdf_path = os.path.join("data", "Chapter 14.pdf")
chap26_pdf = PDFReader().load_data(file=pdf_path)
chap26_index = get_index(chap26_pdf, "M5_Chap14_pdf")
chap26_engine = chap26_index.as_query_engine()

'''
Chap 27
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 5_1 - LE CHOIX D'UN PRIX.pdf")
chap27_pdf = PDFReader().load_data(file=pdf_path)
chap27_index = get_index(chap27_pdf, "M5_Script_Video_5_1")
chap27_engine = chap27_index.as_query_engine()

'''
Chap 28
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 5_2 - LE PRIX DES NOUVEAUX PRODUITS.pdf")
chap28_pdf = PDFReader().load_data(file=pdf_path)
chap28_index = get_index(chap28_pdf, "M5_Script_Video_5_2")
chap28_engine = chap28_index.as_query_engine()

'''
Chap 29
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 5_3 - PRIX DE MARCHE ET PRIX FLEXIBLES.pdf")
chap29_pdf = PDFReader().load_data(file=pdf_path)
chap29_index = get_index(chap29_pdf, "M5_Script_Video_5_3")
chap29_engine = chap29_index.as_query_engine()


''' Module 6 '''

'''
Chap 30
'''
pdf_path = os.path.join("data", "Chapter 15.pdf")
chap30_pdf = PDFReader().load_data(file=pdf_path)
chap30_index = get_index(chap30_pdf, "M5_Chap15_pdf")
chap30_engine = chap30_index.as_query_engine()

'''
Chap 31
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 6_1 - LA COMMUNICATION MEDIA, HORS MEDIA ET HYBRIDE.pdf")
chap31_pdf = PDFReader().load_data(file=pdf_path)
chap31_index = get_index(chap31_pdf, "M6_Script_Video_6_1")
chap31_engine = chap31_index.as_query_engine()

'''
Chap 32
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 6_2 - LES OBJECTIFS DE COMMUNICATION.pdf")
chap32_pdf = PDFReader().load_data(file=pdf_path)
chap32_index = get_index(chap32_pdf, "M6_Script_Video_6_2")
chap32_engine = chap32_index.as_query_engine()

'''
Chap 33
'''
pdf_path = os.path.join("data", "RAN Marketing Script Video 6_3 - LA COMMUNICATION DIGITALE.pdf")
chap33_pdf = PDFReader().load_data(file=pdf_path)
chap33_index = get_index(chap33_pdf, "M6_Script_Video_6_3")
chap33_engine = chap33_index.as_query_engine()