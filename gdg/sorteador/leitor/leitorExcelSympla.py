from .leitor import Leitor 
from Participante import Participante 
import pandas as pd
import logging

class LeitorExcelSympla(Leitor):
    def ler(self, caminho, ingressosParaIgnorar=[], apenasComCheckin=True):
        try:
            dados= pd.read_excel(caminho, skiprows=7, usecols=["Nome", "Sobrenome", "Email", "Check-in", "Estado de pagamento", "Tipo de ingresso", "Nº ingresso"])
            dados.dropna(inplace=True) 
            dados = dados[~dados["Tipo de ingresso"].isin(ingressosParaIgnorar)]          
            validosParaSorteio = dados[(dados["Estado de pagamento"] == "Aprovado") & ( dados["Check-in"] == "Sim" if apenasComCheckin else True)]
            return [Participante(nome= row['Nome'], sobrenome= row['Sobrenome'], email=row["Email"], ingresso=row["Nº ingresso"]) for _, row in validosParaSorteio.iterrows()]
        except Exception as e:
            logging.error(f"Error reading the Excel file: {e}")
            return []