# --Importando os dados
import pandas as pd
dados = pd.read_csv("prefeitura-fev.CSV", encoding="latin1", sep=";")

# 1. Qual a quantidade de servidores na Prefeitura? #(Considerando o dado que "Considere que cada 
# linha da tabela extraída representa 1 servidor, ou seja, 1 funcionário público" não precisamos filtrar dados)
total_serv = dados.shape[0]
print(total_serv)


# 2. Qual a quantidade de servidores cujo cargo básico é Analista de Políticas Públicas Gestão Governamental?
qtdd = dados["CARGO_BASICO"].str.contains("ANALISTA POLITICAS PUBLICAS GESTAO GOVERNAMENTAL", case=False).sum()
print(qtdd)


# 3. Qual o percentual de servidores do sexo feminino na Prefeitura?
mulheres = dados["SEXO"].str.contains("FEMININO", case=False).sum()
print(f"{(mulheres/total_serv):.2%}")


# 4. Qual o percentual de servidores cuja escolaridade do cargo básico é Superior Completo?**"""
qtdd_sup_comp = dados["ESCOL_CARGO_BASICO"].str.contains("SUPERIOR COMPLETO", case=False).sum()
print(f"{(qtdd_sup_comp/total_serv):.2%}")


# 5. Qual a quantidade de servidores cuja relação jurídico-administrativa é "Efetivo
efetivos = dados["REL_JUR_ADM"].str.contains("EFETIVO", case=False).sum()
print(efetivos)


# 6. Qual a sigla Secretaria com menor percentual de servidores efetivos?
# --Menor percentual será a sigla de MENOR QTDD dentre os efetivos
dados_efetivos = dados[dados['REL_JUR_ADM'] == 'EFETIVO']
qtdd_efetivos_sigla = dados_efetivos["SIGLA"].value_counts()
print(qtdd_efetivos_sigla.idxmin())

#não foi necessário para responder porém irei deixar como extra o database com os percentuais
"""
resultado = pd.DataFrame({
    "quantidade": qtdd_efetivos_sigla,
    "percentual": (qtdd_efetivos_sigla / qtdd_efetivos_sigla.sum()) * 100
})
resultado["percentual"] = resultado["percentual"].round(2)
"""


#7. Qual a Subprefeitura com menor quantidade de servidores?
print(dados_efetivos["SECRET_SUBPREF"].value_counts().idxmin())


#8. Qual o percentual de servidores efetivos diante da quantidade total de servidores?
print(f"{(efetivos/total_serv):.2%}")


#9. Quantos servidores com deficiência tem na Prefeitura?
pcd = dados["PCD"].str.contains("SIM", case=False).sum()
print(pcd)


#10. Quantos Procuradores Municipais são, também, Secretários Adjuntos? 
# (Existe o cargo Secretário Executivo Adjunto e Secretário Adjunto, considerei os 2)
print(len(dados[
    (dados['SUBGRUPO'] == 'PROCURADOR') &
    (dados['CARGO_COMISSAO'].str.contains('SECRETARIO', case=False, na=False)) &
    (dados['CARGO_COMISSAO'].str.contains('ADJUNTO', case=False, na=False))
]))


#11. Entre as pessoas com cargo em comissão do tipo "CDA", quantos % são "CDA-1"?
cda = dados[
    (dados['REL_JUR_ADM'].str.contains('COMISSAO', case=False, na=False)) &
    (dados['REF_CARGO_BAS'].str.contains('CDA', case=False, na=False))
]

total_cda = len(cda)
cda_1 = len(cda[cda['REF_CARGO_BAS']=='CDA-1'])
percent_cda1 = cda_1/total_cda
print(f"{percent_cda1:.2%}")


#tabela completa de cada cda, não foi necessário para a resolução da questão!
"""resultado = pd.DataFrame({
    "quantidade": cda["REF_CARGO_BAS"].value_counts(),
    "percentual": ((cda["REF_CARGO_BAS"].value_counts()) / total_cda) * 100
})
resultado["percentual"] = resultado["percentual"].round(2)
"""