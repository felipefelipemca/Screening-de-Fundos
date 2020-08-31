import pandas as pd
import datetime
import numpy as np



lista_de_fundos = pd.read_excel('FI.xlsx')
hoje1 = datetime.date.today()
fmt = "%d/%m/%Y"
hoje2 = datetime.datetime.strftime(hoje1,fmt)

deltatempo = np.datetime64(hoje1) - lista_de_fundos.DT_CONST

lista_de_fundos.drop_duplicates(subset="CNPJ_FUNDO", keep='first', inplace=True)

resultado = lista_de_fundos[ ~lista_de_fundos['DENOM_SOCIAL'].str.contains("MASTER")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("CRÉDITO")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("CREDITO")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("ADVISORY")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("PRIVATE")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("ACESSO")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("ESPELHO")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("ACCESS")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("ITAÚ")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("ITAU")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("BRADESCO")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("BB")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("BANCO DO BRASIL")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("SICOOB")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("SANTANDER")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("SICREDI")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("CAIXA")
                             & ~lista_de_fundos['DENOM_SOCIAL'].str.contains("CRED")
                             & ~lista_de_fundos['CLASSE'].str.contains("Fundo de Renda Fixa", na=False) 
                             & (lista_de_fundos.FUNDO_EXCLUSIVO == "N")
                             & (lista_de_fundos.CONDOM == "Aberto")
                             & (lista_de_fundos.SIT == "EM FUNCIONAMENTO NORMAL")
                             & (lista_de_fundos.VL_PATRIM_LIQ > 50000000)
                             & (deltatempo > pd.Timedelta(1080,'D'))]



cotistas = pd.read_excel('novo_arq.xlsx')
cotistas.drop_duplicates(subset="CNPJ_FUNDO", keep='first', inplace=True)
cotistas = cotistas.drop(["DT_COMPTC", "VL_TOTAL", "VL_QUOTA", "VL_PATRIM_LIQ", "CAPTC_DIA", "RESG_DIA"], axis=1)

completo = pd.merge(left=resultado, right=cotistas, left_on='CNPJ_FUNDO',right_on='CNPJ_FUNDO')
completo = completo[(completo.NR_COTST > 250)]
completo.to_excel('Lista filtrada.xlsx')