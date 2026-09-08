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
```python
128499
```

### 2. Qual a quantidade de servidores cujo cargo básico é Analista de Políticas Públicas Gestão Governamental?
> Utilizei primeiro um filtro pela coluna "Cargo Básico" filtrando pelo cargo "ANALISTA POLITICAS PUBLICAS GESTAO GOVERNAMENTAL". 
> Se fizermos apenas isso retornará a lista completa, adicionei a sintaxe .sum() para retornar a quantidade de funcionários com esse cargo.
```python
qtdd = dados["CARGO_BASICO"].str.contains("ANALISTA POLITICAS PUBLICAS GESTAO GOVERNAMENTAL", case=False).sum()
```
```python
185
```

### 3. Qual o percentual de servidores do sexo feminino na Prefeitura?
> Mesma ideia base da questão anterior, filtrei inicialmente pela coluna "SEXO" que continha "FEMININO" e depois pedi a soma de linhas que apresentavam esse valor. <br>
> No print aproveitei o valor encontrado na 1ª questão para obter o percentual de funcionárias do sexo feminino comparado ao total de funcionários. <br>
> No print adicionei a formatação para duas casas decimais.
```python
mulheres = dados["SEXO"].str.contains("FEMININO", case=False).sum()
print(f"{(mulheres/total_serv):.2%}")
```
```python
73.16%
```

### 4. Qual o percentual de servidores cuja escolaridade do cargo básico é Superior Completo?
> O filtro que utilizei nessa e em outras questões que exigem essa lógica de filtragem funciona da seguinte forma: <br>
> nome_dado_a_base_de_dados["NOME_COLUNA_A_SER_FILTRADA"].str.contains("NOME TERMO A FILTRAR", case=False) <br>
> Quando filtramos apenas assim a biblioteca Pandas retornará a lista de linhas que contém a informação que pedimos para filtrar, para retornar a quantidade de linhas precisamos adicionar o comando ".sum()".
```python
qtdd_sup_comp = dados["ESCOL_CARGO_BASICO"].str.contains("SUPERIOR COMPLETO", case=False).sum()
print(f"{(qtdd_sup_comp/total_serv):.2%}")
```
```python
9.74%
```

### 5. Qual a quantidade de servidores cuja relação jurídico-administrativa é "Efetivo
```python
efetivos = dados["REL_JUR_ADM"].str.contains("EFETIVO", case=False).sum()
print(efetivos)
```
```python
111952
```

### 6. Qual a sigla Secretaria com menor percentual de servidores efetivos?
> Para resolver essa fiz 3 filtros diferentes: <br>
> 1º: filtrei pelos servidores com "REL_JUR_ADM" "EFETIVO"
```python
dados_efetivos = dados[dados['REL_JUR_ADM'] == 'EFETIVO']
```
> Depois utilizei a sintaxe .value_counts() agrupando pela coluna "SIGLA" assim retorna a quantidade de linhas por sigla.
```python
qtdd_efetivos_sigla = dados_efetivos["SIGLA"].value_counts()
```
> No print adicionei mais uma sintaxe, a .idmin(), ela retornará qual sigla com a menor quantidade de servidores efetivos. Como o exercício não pediu o percentual e sim qual sigla esse formato resolve nosso problema.
```python
print(qtdd_efetivos_sigla.idxmin())
```
```python
SMJ
```

### 7. Qual a Subprefeitura com menor quantidade de servidores?
> Segui o mesmo raciocínio da questão anterior podem diretamente em uma única linha.
```python
print(dados_efetivos["SECRET_SUBPREF"].value_counts().idxmin())
```
```python
SECRETARIA MUNICIPAL DE JUSTICA
```

### 8. Qual o percentual de servidores efetivos diante da quantidade total de servidores?
> Essa foi bem simples, dividi o valor encontrado da 5ª questão (Quantidade de servidores efetivos) pelo valor encontrado na 1ª questão (Total de servidores) e formatei para obter duas casas decimais.
```python
print(f"{(efetivos/total_serv):.2%}")
```
```python
87.12%
```

### 9. Quantos servidores com deficiência tem na Prefeitura?
> Essa questão segue a mesma lógica de raciocínio das questões 2, 3 e 4 por exemplo.
```python
pcd = dados["PCD"].str.contains("SIM", case=False).sum()
print(pcd)
```
```python
929
```

### 10. Quantos Procuradores Municipais são, também, Secretários Adjuntos? 
>(Existe o cargo Secretário Executivo Adjunto e Secretário Adjunto, considerei os 2) <br>
> Para essa questão precisei criar mais de um filtro para atender a demanda da questão, nesse caso podemos utilizar a sintaxe: <br>
> nome_da_base_de_dados[
>  (nome_da_base_de_dados["NOME_COLUNA_A_SER_FILTRADA_1"].str.contains("NOME TERMO A FILTRAR_1", case=False)) &
>  (nome_da_base_de_dados["NOME_COLUNA_A_SER_FILTRADA_2"].str.contains("NOME TERMO A FILTRAR_2", case=False))
> ]
> 
> Lembrando que precisamos adicionar o conector "&" para cada novo filtro que precisamos acrescentar.

```python
print(len(dados[
    (dados['SUBGRUPO'] == 'PROCURADOR') &
    (dados['CARGO_COMISSAO'].str.contains('SECRETARIO', case=False, na=False)) &
    (dados['CARGO_COMISSAO'].str.contains('ADJUNTO', case=False, na=False))
]))
```
```python
2
```

### 11. Entre as pessoas com cargo em comissão do tipo "CDA", quantos % são "CDA-1"?
> Mesmo raciocínio da questão anterior com a adição do calculo de percentual.
```python
cda = dados[
    (dados['REL_JUR_ADM'].str.contains('COMISSAO', case=False, na=False)) &
    (dados['REF_CARGO_BAS'].str.contains('CDA', case=False, na=False))
]

total_cda = len(cda)
cda_1 = len(cda[cda['REF_CARGO_BAS']=='CDA-1'])
percent_cda1 = cda_1/total_cda
print(f"{percent_cda1:.2%}")
```
```python
13.80%
```

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