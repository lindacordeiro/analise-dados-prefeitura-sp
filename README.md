# Prova de Análise de Dados - Prefeitura de SP

Essa análise de dados em Python foi desenvolvida para uma prova de estágio feita em Maio de 2026 para <br>
a Prefeitura de SP. <br>

## Análises Realizadas:
### 1. Qual a quantidade de servidores na Prefeitura? 
Considerando o dado que "Considere que cada linha da tabela extraída representa 1 servidor, ou seja, 1 funcionário público" não precisamos filtrar dados.
> Utilizei a sintaxe .shape que retorna a quantidade de linhas de dados do csv.
```python
total_serv = dados.shape[0]
```
'128499'

### 2. Qual a quantidade de servidores cujo cargo básico é Analista de Políticas Públicas Gestão Governamental?
> Utilizei primeiro um filtro pela coluna "Cargo Básico" filtrando pelo cargo "ANALISTA POLITICAS PUBLICAS GESTAO GOVERNAMENTAL". 
> Se fizermos apenas isso retornará a lista completa, adicionei a sintaxe .sum() para retornar a quantidade de funcionários com esse cargo.
```python
qtdd = dados["CARGO_BASICO"].str.contains("ANALISTA POLITICAS PUBLICAS GESTAO GOVERNAMENTAL", case=False).sum()
```
'185'

### 3. Qual o percentual de servidores do sexo feminino na Prefeitura?
> Mesma ideia base da questão anterior, filtrei inicialmente pela coluna "SEXO" que continha "FEMININO" e depois pedi a soma de linhas que apresentavam esse valor. 
> No print aproveitei o valor encontrado na 1ª questão para obter o percentual de funcionárias do sexo feminino comparado ao total de funcionários.
```python
mulheres = dados["SEXO"].str.contains("FEMININO", case=False).sum()
```
'73.16%'

### 4. Qual o percentual de servidores cuja escolaridade do cargo básico é Superior Completo?
qtdd_sup_comp = dados["ESCOL_CARGO_BASICO"].str.contains("SUPERIOR COMPLETO", case=False).sum()
print(f"{(qtdd_sup_comp/total_serv):.2%}")


# 8. Qual a quantidade de servidores cuja relação jurídico-administrativa é "Efetivo
efetivos = dados["REL_JUR_ADM"].str.contains("EFETIVO", case=False).sum()
print(efetivos)


# 9. Qual a sigla Secretaria com menor percentual de servidores efetivos?
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


#10. Qual a Subprefeitura com menor quantidade de servidores?
print(dados_efetivos["SECRET_SUBPREF"].value_counts().idxmin())


#11. Qual o percentual de servidores efetivos diante da quantidade total de servidores?
print(f"{(efetivos/total_serv):.2%}")


#12. Quantos servidores com deficiência tem na Prefeitura?
pcd = dados["PCD"].str.contains("SIM", case=False).sum()
print(pcd)


#13. Quantos Procuradores Municipais são, também, Secretários Adjuntos? 
# (Existe o cargo Secretário Executivo Adjunto e Secretário Adjunto, considerei os 2)
print(len(dados[
    (dados['SUBGRUPO'] == 'PROCURADOR') &
    (dados['CARGO_COMISSAO'].str.contains('SECRETARIO', case=False, na=False)) &
    (dados['CARGO_COMISSAO'].str.contains('ADJUNTO', case=False, na=False))
]))


#14. Entre as pessoas com cargo em comissão do tipo "CDA", quantos % são "CDA-1"?
cda = dados[
    (dados['REL_JUR_ADM'].str.contains('COMISSAO', case=False, na=False)) &
    (dados['REF_CARGO_BAS'].str.contains('CDA', case=False, na=False))
]

total_cda = len(cda)
cda_1 = len(cda[cda['REF_CARGO_BAS']=='CDA-1'])
percent_cda1 = cda_1/total_cda
print(f"{percent_cda1:.2%}")

<img 
    align="left" 
    alt="Python" 
    title="Python"
    width="30px" 
    style="padding-right: 10px;" 
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
/>
<img 
    align="left" 
    alt="Git" 
    title="Git"
    width="30px" 
    style="padding-right: 10px;" 
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" 
/>