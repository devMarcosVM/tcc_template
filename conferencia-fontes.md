# Conferência de fontes (15 nov. 2026)

Legenda. **Conferida** significa que abri a fonte nesta sessão e vi o trecho. **Parcial** significa que vi só parte (resumo, citação em outra página ou índice). **Não conferida** significa que os dados vêm de memória ou de sessões anteriores.

## Fontes conferidas nesta sessão

| Chave | Fonte | O que foi visto | Situação |
|---|---|---|---|
| nistSsdf | NIST SP 800-218 (SSDF 1.1) | Autores Souppaya, Scarfone e Dodson, fevereiro de 2022. PW.7 (revisar ou analisar o código para identificar vulnerabilidades e verificar conformidade). PW.7.2 (registrar e triar os problemas). O documento não menciona DevSecOps | Conferida |
| blackIr8397 | NIST IR 8397 | Seção 2.3, análise estática independe da execução, análise dinâmica é baseada em execução. Seção 2.11, "Check Included Software Components", com SCA e vulnerabilidades conhecidas | Conferida |
| johnson2013 | Johnson et al., ICSE 2013 | Páginas 672 a 681. Entrevistas com 20 desenvolvedores. Falsos positivos e apresentação dos alertas como barreiras | Conferida |
| rajapakse2022 | Rajapakse, Zahedi, Babar e Shen | Versão arXiv. Definição de DevSecOps (seção 2.3). 54 estudos. Segurança como requisito não funcional e esforço manual (seção 1). Falsos positivos (seção 4.3.1) | Conferida no arXiv. Volume e DOI da revista não conferidos |
| chandramouli2024 | NIST SP 800-204D | Autores Chandramouli, Kautz e Torres-Arias, fevereiro de 2024. DevSecOps com esteiras CI/CD. SCA citado na seção 5.1.4. Não menciona a NVD | Conferida |
| owaspRiskRating | OWASP Risk Rating Methodology | Seis etapas. Fatores de impacto no negócio na etapa 3. "Ultimately, the business impact is more important". Autor Jeff Williams, sem data | Conferida |
| iso19011 | ISO 19011:2018 | Definições de evidência de auditoria e de achados de auditoria | Parcial, vista em coleção de terminologia da ERA que reproduz a norma |
| ieee1028 | IEEE 1028-2008 | Finalidade da auditoria, cláusula 8.1 | Parcial, vista em citação literal do NASA Software Engineering Handbook |
| iso25010 | ISO/IEC 25010:2023 | Resumo público. Modelo com nove características | Conferida (resumo) |
| sonarMetrics99 | Documentação SonarQube, definições de métricas | Complexidade ciclomática, contador por divisão do fluxo, variação por linguagem | Conferida na versão 9.8 |
| sonarAnalysis99 | Documentação SonarQube 9.9, tarefas de segundo plano | A análise só está completa quando a tarefa termina | Conferida |
| semgrepDocs | Documentação Semgrep, linguagens da edição comunitária | Python, JavaScript, TypeScript e PHP como "community supported", análise limitada a uma função | Conferida |
| semgrepLicensing | Documentação Semgrep, licenças | Motor LGPL 2.1. Regras sob Semgrep Rules License 1.0, só para uso interno | Conferida |
| spadeDocs | Documentação SPADE 4.1.4 | Plataforma em Python sobre XMPP, comportamentos, asyncio, qualquer servidor XMPP | Conferida |
| palanca2020 | Palanca et al., IEEE Access 8 | Dados bibliográficos | Parcial, conteúdo não lido |
| rfc6120 | RFC 6120 | Resumo, março de 2011 | Conferida |
| omgUml | OMG UML 2.5.1 | Versão, dezembro de 2017, descrição | Conferida |
| plantumlSequence | PlantUML | Diagramas definidos em texto | Conferida |
| ollamaContext | Documentação Ollama | Contexto maior exige mais memória | Conferida |
| moro2003 | Moro, Ouksel e Sartori | Autores, título, páginas 1 a 14, livro de 2003 | Parcial, conteúdo não lido |
| canedo2026 | Canedo et al., Computers & Security | Resumo, 88 profissionais | Parcial (12 nov.) |
| groth2013 | W3C PROV-Overview | Definição de proveniência | Conferida (12 nov.) |
| zuev2025 | Zuev, Sakulin e Shmakova | PDF local. Experimento com cerca de 100 varreduras | Conferida |

## Correções em relação ao que estava antes

- **SSDF.** A ordem dos autores é Souppaya, Scarfone, Dodson. As duas outras IAs erraram (uma inventou "Murugesan", a outra trocou a ordem).
- **Rajapakse.** O primeiro autor é Roshan N. Rajapakse, e há um quarto autor, Haifeng Shen. A primeira IA errou os dois pontos.
- **NIST SP 800-204D.** Não menciona a NVD, ao contrário do que a primeira IA afirmou.
- **NIST SP 800-53A Rev. 5.** É de janeiro de 2022. Não uso mais essa fonte, porque a ISO 19011 define evidência e achado de forma direta.
- **Chess e McGraw (2004).** Saiu do texto. O NIST IR 8397 cobre análise estática e dinâmica na mesma seção, e foi conferido.
- **Moro et al.** O livro é de 2003. O workshop é que foi em 2002. A chave no `.bib` passou a ser `moro2003`.
- **Semgrep.** O texto antigo dizia "melhor esforço". A documentação diz "suportadas pela comunidade", sem prioridade em atualizações, e limita a edição comunitária à análise dentro de cada função. O Cap. 3 agora registra as duas limitações.

## O que ainda precisa de você

1. **IEEE 1028-2008.** Ler a cláusula 8.1 pelo IEEE Xplore, com o acesso da UnB. Só vi a citação feita pela NASA.
2. **ISO 19011:2018.** Abrir os termos na plataforma pública da ISO (Online Browsing Platform) e conferir as duas definições.
3. **Oliveira (2026).** Pedir o PDF à Milene. A monografia não foi localizada, e a citação está como comentário no `.tex`.
4. **Wang et al. (2026).** O link fornecido (https://ieeexplore.ieee.org/document/11207716) bloqueou o acesso nesta atualização. Autoria completa, título e veículo continuam pendentes; a indicação foi preservada em comentários na bibliografia e na introdução. **Flores (2005)** foi localizado no [PDF da UFRJ](https://pantheon.ufrj.br/server/api/core/bitstreams/12c0c07b-2ad0-40eb-8a3a-5c09f6db863b/content): Roberto Costa Flores, *Redes Peer-to-Peer: um estudo sobre aspectos de segurança e mobilidade*, monografia de especialização, NCE/UFRJ, Rio de Janeiro, 2005. Capa, folha de rosto e resumo conferidos; entrada `flores2005` e citação na introdução adicionadas.
5. **Moro, Ouksel e Sartori (2003).** Ler o capítulo antes de afirmar algo além do título.
6. **Rajapakse et al.** Conferir volume 141, número do artigo 106700 e DOI na página da revista.
7. **McCabe (1976) e Palanca et al. (2020).** Conferir no IEEE Xplore.
8. **Fontes clássicas de sessões anteriores.** Wooldridge e Jennings (1995), Wooldridge (2009), Rao e Georgeff (1995), Finin et al. (1994), FIPA (2002), Geiger e Halfaker (2017), Bordini et al. (2007). Os dados do `.bib` vieram de memória.
9. **Canedo et al. (2026).** Ler o artigo inteiro. Só vi o resumo.
10. **Documentações do Cap. 3 não reconferidas hoje.** LaTeX, Zotero, draw.io, asyncio, Prosody, Docker Compose, Ollama (interface de programação), pip-audit, npm audit, Composer audit, Trivy e Git. Conferir a data de acesso de cada uma no `.bib`.
11. **Chave `sonarMetrics99`.** Verificar se a entrada aponta para a página de definições de métricas.

## Decisões que continuam em aberto com a Milene

- Ela fala em "taxa de acerto dos agentes". O sistema não dá veredito, então é preciso combinar o que será medido.
- Ela fala em especialistas em segurança, com TCLE. O texto atual prevê um avaliador, que é o responsável humano.
- Ela descreve o controle semi-centralizado no Auditor. No diagrama, o Orquestrador distribui as tarefas e o Auditor consolida.

## Revisão do referencial teórico nesta atualização

Foram conferidas as 35 chaves citadas no capítulo: todas possuem entrada em `latex/bibliografia.bib`. A cópia `referencial-teorico.tex` da raiz recebeu as mesmas correções do arquivo efetivamente compilado, `latex/editaveis/referencial-teorico.tex`.

- **Geiger e Halfaker (2017):** substituído o título provisório “Wikipedia Bots / Trace Ethnography” pelo título do artigo, acrescentando periódico, volume, número, identificador do artigo e DOI. [Página do autor](https://stuartgeiger.com/articles/2017-09-12-conflict-bots-cscw/) confirma o argumento sobre interações rotineiras e colaborativas.
- **McCabe (1976):** corrigida a definição para caminhos linearmente independentes no grafo de fluxo de controle. Seção II do [artigo original, cópia na TUM](https://wwwbroy.in.tum.de/lehre/vorlesungen/vse/WS2004/1976_mccabet_complexity_measure.pdf) consultada. Isso atualiza a pendência anterior sobre o conteúdo de McCabe; o DOI continua sem reconferência no IEEE.
- **SonarQube:** descrição compatível com a [documentação 9.9](https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/metric-definitions), agora consultada diretamente. Resolvida a pendência sobre a URL dessa entrada.
- **NIST:** confirmadas a análise estática/dinâmica na seção 2.3 do [IR 8397](https://doi.org/10.6028/NIST.IR.8397) e a revisão, registro e triagem em PW.7/PW.7.2 do [SSDF](https://doi.org/10.6028/NIST.SP.800-218).
- **Achados:** explicitada como convenção deste trabalho a denominação de achados candidatos para ocorrências ainda não verificadas; evitada a equiparação automática entre alerta de ferramenta e achado confirmado de auditoria.
- **Moro e Flores:** incluída a citação de Flores e atualizado o comentário de pendência. As fontes não são usadas para alegar que controle semicentralizado é obrigatório ou preferível em todo SMA.
- **P2P:** delimitado como interação lógica entre especialistas. A [documentação SPADE](https://spade-mas.readthedocs.io/en/latest/readme.html) confirma o uso de XMPP e servidores. O texto distingue esse transporte da distribuição das responsabilidades.
- **Lazarin:** mantido 2025, ano da citação editorial recomendada pela [Springer](https://link.springer.com/chapter/10.1007/978-3-031-70415-4_15), apesar da publicação online em novembro de 2024. Autores, volume e páginas conferidos.
- **Rousek:** [resumo editorial](https://journals.lka.lt/journal/cndcgs/article/2344/info) confirma a natureza conceitual, decomposição de tarefas, proveniência e controle delimitado. Não equivale à leitura integral.
- **OWASP e W3C:** consultadas as páginas de [avaliação de riscos](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology) e [PROV-Overview](https://www.w3.org/TR/prov-overview/). Mantidas as respectivas atribuições; o projeto não afirma implementar integralmente esses modelos.
- **ISO 25010:** página pública confirma o modelo da edição 2023; isso não constitui consulta ao texto integral da norma.
- **Sowan:** corrigida a concordância para autor único.

### Limites desta revisão

A existência de uma entrada BibTeX não comprova o conteúdo da fonte. Esta revisão não certifica integralmente os 35 trabalhos. Permanecem as pendências de Wang e Oliveira. Também não foram reconferidas integralmente as afirmações específicas dos trabalhos de Zuev, Yesil, Ait, Yan, Khoee, Mosciatti, Sowan, Canedo, Ajimati e Silic; as atribuições existentes foram preservadas e devem ser confrontadas com os respectivos PDFs antes da entrega. As consultas aos DOIs de Ait, Yan, Khoee e Canedo não retornaram o conteúdo nesta sessão. FIPA bloqueou acesso. A definição de auditoria da IEEE 1028 e as definições da ISO 19011 continuam com as limitações registradas anteriormente.


## Atualização: Wang identificado

Resolvida a pendência bibliográfica de Wang: `wang2026`, *Internet of Agents: Fundamentals, Applications, and Challenges*, IEEE Transactions on Cognitive Communications and Networking, v. 12, p. 4476–4501, 2026, DOI 10.1109/TCCN.2025.3623369. Dados finais fornecidos pelo usuário, título/volume/páginas/DOI confirmados no [IEEE](https://ieeexplore.ieee.org/document/11207716/); os nove autores e o resumo foram conferidos no [arXiv](https://arxiv.org/abs/2505.07176). Esta atualização substitui as pendências bibliográficas anteriores sobre Wang. Conteúdo conferido no resumo, sem leitura integral. Citações inseridas na introdução e no referencial teórico.
