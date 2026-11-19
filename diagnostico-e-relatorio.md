# Diagnóstico e relatório das alterações (revisão 6, 16 nov. 2026)

Escopo desta revisão. Capítulos 1 a 5, materiais acadêmicos, planilha, fichamentos, PDFs locais e anotações da Profa. Milene. A pasta do protótipo não foi aberta, e nenhum código, teste, script ou documentação técnica foi lido nesta revisão.

Uma ressalva sobre a origem do Capítulo 5. A versão 5 da Seção sobre a prova de conceito foi escrita, em dias anteriores, com apoio em documentos do protótipo que li antes de você restringir o escopo. Nesta revisão não voltei a eles. Por isso, tudo o que o Capítulo 5 diz sobre a implementação passou a ser apresentado como declaração do autor, e o Quadro de evidências da prova de conceito registra "não apresentada" em todas as linhas.

## 1. Como ler a matriz

- **Natureza.** Fonte, método, coerência, redação, forma ou evidência de implementação.
- **Situação.** *Confirmado* (o problema foi visto no material), *a investigar* (há indício, falta conferir) ou *depende de você ou da orientação*.
- **Prioridade.** Alta (afeta a defesa do trabalho), média (afeta a clareza ou a precisão) ou baixa (forma).

## 2. Matriz de diagnóstico

### Capítulo 1 (não alterado no conteúdo)

Os treze acertos de forma já feitos na versão 5 foram mantidos, por exemplo `\citeonline(paulo2026)` com parênteses, "Dianto", "coleto" e "i.r.". Os problemas de conteúdo estão em `sugestoes-introducao.md` e não foram aplicados.

### Capítulo 2

| Seção | Trecho ou ponto | Natureza | Evidência | Situação | Ação na v6 | Prior. |
|---|---|---|---|---|---|---|
| 2.1 | Auditoria definida como avaliação independente, sem dizer se o trabalho pretende independência | Coerência | IEEE 1028, cláusula 8.1, vista por citação da NASA. Princípio da ISO 19011 visto em fonte secundária | Confirmado | Parágrafo novo que delimita o termo. O trabalho apoia a auditoria e não afirma realizar auditoria independente. Marcado `% CONFERIR` | Alta |
| 2.1.3 | Cadeia achado, evidência, contexto, parecer sem a conclusão do especialista | Coerência | Capítulo 5 usa "conclusão" como unidade que chega ao Auditor | Confirmado | Fecho reescrito com a cadeia completa e um exemplo curto | Alta |
| 2.1.3 | "14,8%" associado às esteiras | Fonte | Canedo et al. O percentual refere-se à automação limitada das ferramentas de verificação | Confirmado (corrigido desde a v5) | Mantida a redação corrigida | Alta |
| 2.3.1 | Fecho descrevia a solução em detalhe | Redação | Repetia o Capítulo 5 | Confirmado | Reduzido a duas frases. Acrescentada a separação de deveres de Mosciatti et al. | Média |
| 2.3.1 | "Controle semi-centralizado" apoiado em Moro et al. | Fonte | Só Flores (2005, p. 17-18) define o termo. De Moro et al. só o resumo foi visto | Confirmado | No Capítulo 2 a definição cita Flores. Moro fica para a combinação de agentes e P2P | Alta |
| 2.3.3 | Uso de modelo de linguagem sem tratar instruções contidas em documentos | Coerência | OWASP LLM01:2025 | Confirmado | Parágrafo sobre injeção indireta, com remissão ao Capítulo 5 | Média |
| 2.5 | Fechos enumeravam categorias de regra e campos do parecer | Redação | Repetição do Capítulo 5 | Confirmado | Reduzidos. As categorias ficaram só no Capítulo 5 | Média |
| 2.6 | Comparação com trabalhos relacionados era descritiva e curta | Método | Leitura dos nove PDFs em 16 nov. | Confirmado | Reescrita por trabalho, com problema, agentes e comunicação, consolidação, rastreabilidade e avaliação. Quadro comparativo novo | Alta |
| 2.6 | Afirmação de lacuna na literatura | Método | A lacuna só pode ser afirmada sobre o que foi lido | Confirmado | Posicionamento restrito aos nove trabalhos lidos | Alta |
| 2.6 | Zuev et al. com avaliação por especialistas | Fonte | O artigo relata amostra de cerca de 100 varreduras, sem julgamento de especialistas | Confirmado | Texto ajustado | Média |
| 2.6 | Yesil et al. "separa autorização e geração" | Fonte | Os agentes usam modelo de linguagem para validar permissões | Confirmado | Ressalva incluída | Média |
| 2.x | Definições clássicas (Wooldridge, Rao e Georgeff, Finin, FIPA, McCabe, Geiger) | Fonte | Entradas escritas de memória, segundo as suas notas | A investigar | Mantidas, sem citação direta. Listadas nas pendências | Média |

### Capítulo 3

| Seção | Trecho ou ponto | Natureza | Evidência | Situação | Ação na v6 | Prior. |
|---|---|---|---|---|---|---|
| Geral | Versões apresentadas como instaladas | Evidência | Não há registro acadêmico das versões em uso | Confirmado | Nota de abertura. As versões são as declaradas. Coluna "Situação e versão" com utilizada, selecionada ou candidata | Alta |
| 3.3.5 | SonarQube 9.9 sem ressalva | Fonte | A documentação da 9.9 informa que a versão não recebe mais correções | Confirmado | Ressalva incluída | Média |
| 3.3.6 | Semgrep, linguagens "suportadas pela comunidade" e limite de análise | Fonte | A página aberta em 16 nov. exibiu só dados dos produtos comerciais | A investigar | Mantido com `% CONFERIR` | Alta |
| 3.3.8 | Remissão a "critérios de aceitação das respostas documentais" sem destino | Coerência | A seção de destino não existia | Confirmado | Remissão aponta para a nova seção do agente documental no Capítulo 5 | Alta |
| 3.3.8 | Remissão a "associação documento e componente" sem destino | Coerência | Idem | Confirmado | Idem | Alta |
| Resumo | Bandit e Semgrep tratados da mesma forma | Coerência | Um é utilizado, o outro selecionado | Confirmado | Frase corrigida | Baixa |

### Capítulo 4

| Seção | Trecho ou ponto | Natureza | Evidência | Situação | Ação na v6 | Prior. |
|---|---|---|---|---|---|---|
| 4.2 | Busca descrita não coincide com a planilha | Método | Aba Articles com 240 registros importados em 11 set. 2026 (Web of Science 92, IEEE 85, Scopus 63). Aba Strings com 979 resultados de outras bases e variantes | Confirmado | Os dois conjuntos são descritos em separado, e o texto declara que não há vínculo documentado entre eles | Alta |
| 4.2 | Caminho de 240 para 38 e para 9 não explicado | Método | 38 mantidos (33 por IC1, 5 por IC2). Categorias das notas de 6 out. 2026 | Confirmado | Caminho descrito pelas categorias de leitura e pela leitura integral. Não reconstruí etapas que não estão registradas | Alta |
| 4.2 | IC2 e estudos conceituais | Método | IC2 original menciona comparação entre abordagens. Três dos nove trabalhos são conceituais | Confirmado | O texto informa que IC1 e IC2 foram aplicados como alternativos e que os nove entraram por IC1 | Alta |
| 4.2 | Snowballing declarado | Método | Não há registro do procedimento | Confirmado | Frase e citação de Wohlin retiradas | Alta |
| 4.2 | Triagem por uma única pessoa | Método | Planilha | Confirmado | Declarada como limitação | Média |
| 4.2 | 38 registros com situação "Pendente" | Método | Coluna da planilha | Depende de você | Registrado nas pendências | Média |
| 4.6 | Unidade de análise e reexecuções | Método | Texto anterior tratava execução e caso como iguais | Confirmado | Unidade definida como auditoria de um commit sob uma configuração. Reexecuções não são casos novos | Alta |
| 4.6 | Viés de seleção dos repositórios | Método | A existência de documentação era critério | Confirmado | Critério removido. A disponibilidade de documentação passa a ser característica registrada | Alta |
| 4.6 | Especialistas e instrumento | Método | Número, perfil e instrumento não definidos | Depende de você e da orientação | Instrumento proposto no Apêndice B. Número e perfil ficam como `[INSERIR]` | Alta |
| 4.6 | Denominadores, respostas ausentes, "em parte", divergências | Método | Medidas sem denominador | Confirmado | Tabela de medidas com numerador e denominador. "Em parte" não é somado a "sim". Divergências são relatadas | Alta |
| 4.6 | "Taxa de acerto" sem padrão de referência | Método | Não há gabarito. A aba Protocolo fala em concordância com avaliadores humanos | Confirmado | Operacionalizada como taxa de adequação percebida, com aviso de que não é acurácia | Alta |
| 4.6 | Análise qualitativa sem procedimento | Método | Texto anterior só a anunciava | Confirmado | Quatro passos de rotulagem descritos | Média |
| 4.6 | Limitações dispersas | Redação | | Confirmado | Seção própria | Média |
| 4.1 | Gil citado para natureza e abordagem | Fonte | O trecho de Gil trata de objetivos e procedimentos | Confirmado | No Capítulo 4, natureza e abordagem citam Gerhardt e Silveira, fonte ainda não aberta | Média |

### Capítulo 5

| Seção | Trecho ou ponto | Natureza | Evidência | Situação | Ação na v6 | Prior. |
|---|---|---|---|---|---|---|
| Abertura | Especificação, estágio da prova de conceito e dado da empresa misturados | Coerência | | Confirmado | Nota de abertura declara os três tipos de afirmação | Alta |
| 5.4 | Separação entre Orquestrador e Auditor justificada por independência de auditoria | Fonte | A IEEE 1028 trata de independência de quem audita, não de componentes de software | Confirmado | Justificativa trocada por separação de responsabilidades (Yesil et al., Mosciatti et al.), com a ressalva explícita | Alta |
| 5.4 | "P2P" sem distinguir relação lógica e transporte | Coerência | As mensagens passam por servidor XMPP | Confirmado | Parágrafo novo. P2P designa a consulta direta entre especialistas, e não a ausência de servidor | Alta |
| 5.5 | Estados de encerramento | Coerência | Não havia tratamento de execução parcial ou com falha | Confirmado | Seção e quadro novos, com o efeito de cada estado sobre a recomendação | Alta |
| 5.6 | Agente documental "não participa da recomendação" | Coerência | O contexto que ele produz altera fatos usados pelas regras | Confirmado | Reescrito. Ele não emite a recomendação, mas influencia os fatos | Alta |
| 5.6 | Associação documento, componente e arquivo. Criticidade declarada ou inferida. Verificação de trechos. Informação ausente ou conflitante. Instruções em documentos. Registro no parecer | Coerência | Pontos pedidos na revisão e ausentes do texto | Confirmado | Seção nova com seis subseções, apresentada como especificação proposta | Alta |
| 5.7 | Regras demonstrativas e institucionais | Coerência | Não há políticas da Empresa A apresentadas | Confirmado e depende de você | Distinção explícita. `[INSERIR POLÍTICAS]` mantido | Alta |
| 5.7 | Precedência entre regras e encaminhamento humano | Coerência | | Confirmado | Consequência da precedência descrita. Cinco condições de encaminhamento | Alta |
| 5.8 | Falta de exemplo completo | Redação | | Confirmado | Exemplo ilustrativo, declarado como sintético | Média |
| 5.9 | Afirmações sobre M0 e M1 | Evidência de implementação | Afirmação de implementação sem evidência documental apresentada | Depende de você | Texto atribui as afirmações ao autor. Quadro de evidências com "não apresentada" | Alta |
| 5.2 | Perfil do portfólio da Empresa A | Evidência | Só os dados da introdução | Depende de você | `[INSERIR]` mantido | Alta |

## 3. O que foi corrigido

1. Justificativa da separação entre Orquestrador e Auditor.
2. Papel do agente documental na recomendação.
3. Descrição da busca bibliográfica, agora fiel à planilha, com a retirada do snowballing.
4. Unidade de análise, critério de seleção dos repositórios e medidas com denominador.
5. "Taxa de acerto" operacionalizada sem tratá-la como acurácia.
6. Remissões sem destino no Capítulo 3.
7. Afirmações sobre Zuev et al. e Yesil et al. ajustadas ao que os artigos relatam.
8. Entrada `flores2005` da sua bibliografia, que estava corrompida. O campo `url` continha a lista de objetivos da introdução, com `\begin{itemize}`, e era a causa do erro de compilação "Use of \itemize doesn't match its definition".

## 4. O que foi acrescentado

- Capítulo 2. Parágrafo sobre independência, cadeia completa do achado ao parecer, injeção indireta e quadro comparativo dos trabalhos relacionados.
- Capítulo 3. Classificação da situação de cada tecnologia.
- Capítulo 4. Subseções de unidade de análise, seleção, coleta, apreciação, tratamento, análise qualitativa e limitações. Tabela de medidas.
- Capítulo 5. Estados de encerramento, seção do agente documental, condições de encaminhamento humano, exemplo ilustrativo e quadro de evidências da prova de conceito.
- Apêndices. Ficha de registro da auditoria, instrumento de apreciação e roteiro do termo de consentimento, todos identificados como propostas.
- Bibliografia. Entrada `owaspLlm01`.

## 5. O que foi reduzido ou retirado

- Fechos das Seções 2.3 e 2.5 que repetiam a solução.
- Explicações repetidas dos agentes nos Capítulos 2, 3 e 4, substituídas por remissões ao Capítulo 5.
- Frase sobre snowballing e citação de Wohlin.
- Argumento de independência baseado na IEEE 1028 no Capítulo 5.
- Documentação como critério de seleção dos repositórios.

## 6. Verificação das fontes

O registro por fonte está em `banco-de-citacoes.md`, com a situação real de cada uma. Em resumo.

- **Texto completo aberto nesta revisão (PDF local).** Zuev, Yesil, Ait, Yan, Rousek, Sowan, Mosciatti, Khoee, Lazarin, Morshed e Zangirolami-Raimundo.
- **Trecho pertinente lido por ferramenta que devolve paráfrase.** Flores, Oliveira, Carvalho, Canedo, Wang (versão arXiv), NIST CSF 2.0, OWASP SAMM, NISTIR 8312, OWASP Top 10:2025, CWE, OWASP LLM01, métricas do SonarQube 9.9, contexto do Ollama, trecho de Gil e Boeg.
- **Só resumo ou metadados.** Paulo, Moro, ISO/IEC 25010, Palanca.
- **Só por fonte secundária.** IEEE 1028, ISO 19011, LGPD (guias oficiais) e Pagotto.
- **Não verificadas nesta revisão.** As registradas como conferidas por você em datas anteriores e as entradas escritas de memória. Não aceitei essas marcações como verificação minha.
- **Não reconfirmada.** A afirmação sobre a edição comunitária do Semgrep.

## 7. Estado da compilação

O PDF foi compilado no modelo institucional, com 111 páginas e bibliografia gerada pelo abnTeX2. Restam dois avisos.

- Referência indefinida `met-atividades-primeira-etapa`, no seu arquivo do Capítulo 6, que está fora do escopo.
- Ano ausente nas entradas `semgrepDocs` e `semgrepLicensing`.

Os elementos pré-textuais e o Capítulo 6 do PDF são os do seu modelo, sem alteração.

## 8. Limites desta revisão

- A prosa não foi alisada frase a frase em todos os trechos. Nas partes novas dos Capítulos 4 e 5 ainda há parágrafos curtos em sequência.
- As figuras foram refeitas em dias anteriores e não foram alteradas agora.
- Há 24 entradas da bibliografia sem citação no texto, entre elas os exemplos do modelo. O abnTeX2 só imprime as citadas.
