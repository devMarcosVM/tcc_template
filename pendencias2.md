# Pendências (atualizado em 17 nov. 2026)

As pendências estão separadas por quem pode resolvê-las. As marcas `[INSERIR ...]`, `% PENDENTE` e `% CONFERIR` continuam nos arquivos `.tex`.

## A. Só você pode resolver

| # | O que falta | Onde entra | O que o texto afirma enquanto isso |
|---|---|---|---|
| A1 | **Confirmar as afirmações sobre M0 e M1.** A Seção 5.10 foi escrita a partir de documentos do protótipo que li antes da restrição de escopo. Você não me disse esse conteúdo, e eu não o verifiquei. Leia a seção e confirme ou corrija cada item da lista abaixo | 5.10, Tabela de marcos (4.4) e cronograma (4.7) | A seção fala na voz do trabalho, como se confirmada. Não entregue sem conferir |
| A2 | Evidência de uma execução do marco M1 (pergunta e resposta P2P, parecer gerado, data e commit), para um apêndice | 5.10.4 | `[INSERIR EVIDÊNCIA DA EXECUÇÃO]` |
| A3 | Perfil do portfólio da Empresa A e data do levantamento | 5.1 | Só os números da introdução |
| A4 | Autorização da Empresa A | 4.6 e 5.1 | Que o estudo depende de autorização |
| A5 | Políticas internas que podem ser citadas | 5.7 | As regras são demonstrativas |
| A6 | Número de repositórios e período da coleta | 4.6.2 | A regra de seleção, sem o tamanho do conjunto |
| A7 | Vínculo entre as 979 ocorrências da aba Strings e os 240 registros exportados. Situação "Pendente" dos 38 mantidos. Registro, na aba Protocolo, de que IC1 e IC2 são alternativos | 4.2 | Os dois conjuntos em separado. A regra dos critérios, confirmada por você em 17 nov. |
| A8 | Capa (ano), resumo, agradecimentos e Capítulo 6, que hoje são os do modelo, com "20XX", instruções de preenchimento e uma referência indefinida | Pré-textuais e Capítulo 6 | Fora do escopo desta revisão |
| A9 | Ver com os próprios olhos as duas citações diretas (OWASP Risk Rating e art. 46, § 2º da LGPD) e a página da citação de Paulo na introdução | 1.3, 2.1.3 e 2.5.1 | As aspas foram mantidas |

### Afirmações da Seção 5.10 a confirmar (item A1)

| Afirmação | Evidência que a sustentaria |
|---|---|
| Quatro agentes rodam em processos separados e trocam mensagens pelo servidor XMPP | Trecho do registro de mensagens, com remetentes e destinatários |
| O agente de Segurança faz uma consulta P2P ao de Qualidade e recebe a resposta | Pergunta e resposta registradas |
| A conclusão do agente de Segurança é conservada antes e depois da consulta | Trecho do registro de conclusões |
| No marco M1, o Agente Auditor aplica regras de um arquivo versionado e o agente de Segurança usa o Bandit | Arquivo de regras e parecer gerado |
| Testes automatizados cobrem regras, mensagens e normalização das evidências | Relatório dos testes, com data |
| A construção ocorreu em outubro de 2026 | Histórico do repositório |
| Os quatro aprendizados (servidor embutido, processos separados, granularidade do SonarQube, tamanho das mensagens) | Suas anotações |
| Versões das ferramentas na tabela do Capítulo 3 | Arquivos de configuração |

Situação de todas as linhas. Afirmação de implementação sem evidência documental apresentada. Isso não significa que a funcionalidade não exista.

## B. Decisões com a orientação

| # | Decisão | Onde entra |
|---|---|---|
| B1 | Número e perfil dos especialistas, e se o responsável pelo repositório participa | 4.6.4 |
| B2 | Comitê de ética e forma do termo de consentimento | 4.6.4 e Apêndice C |
| B3 | Manter "taxa de acerto" na introdução ou adotar "adequação percebida" | 1.5 |
| B4 | Grafia de "semi-centralizado" | Trabalho todo |
| B5 | Manter o exemplo ilustrativo e os apêndices propostos | 5.9 e apêndices |
| B6 | Versão do SonarQube, já que a 9.9 não recebe correções | 3.3.5 |
| B7 | Aplicar as sugestões da introdução | Capítulo 1 |
| B8 | Nome do Capítulo 6 | 1.6 |
| B9 | Fonte do roteiro de prova de conceito adotado pela orientação | 4.4 |

## C. Fontes

### C1. Resolvidas nesta rodada

| Fonte | Resultado |
|---|---|
| Semgrep | Confirmado na página da edição comunitária |
| OWASP Risk Rating | Frase confirmada, endereço atualizado |
| Entradas `semgrepDocs` e `semgrepLicensing` | Campo de ano preenchido como sem data |

### C2. Tentei e não consegui abrir. Precisam de acesso seu

| Fonte | O que conferir | Como |
|---|---|---|
| ISO 19011:2018 | Itens 3.9 a 3.11 e o princípio da independência | Plataforma da ISO no navegador, ou ABNT Coleção pela biblioteca da UnB |
| IEEE 1028-2008 | Cláusula 8.1 | IEEE Xplore pela rede da UnB |
| LGPD, art. 46 | Caput e § 2º | Portal do Planalto no navegador |
| Gerhardt e Silveira (2009) | Definições de abordagem qualitativa e de pesquisa aplicada, com página | PDF no repositório da UFRGS |
| Paulo (2026) | Página da citação direta e a afirmação sobre a revisão sistemática | PDF no repositório do ISEP |
| Wang et al. (2026) | Volume e páginas da versão publicada | IEEE Xplore |
| Yesil, Mosciatti e Sowan | DOI e dados de publicação | Página do editor |

Se você me enviar esses PDFs ou os trechos, eu faço a conferência.

### C3. Ainda posso tentar, se você quiser mais uma rodada

| Fonte | O que falta |
|---|---|
| Wooldridge e Jennings, Wooldridge, Rao e Georgeff, Finin et al., FIPA, McCabe, Geiger e Halfaker, Bordini et al., Runeson e Höst, Likert, Pagotto et al. | Dados bibliográficos em índices. As entradas foram escritas de memória |
| Ajimati et al. e Silic et al. | Referência completa |
| Moro et al. (2003) | Texto além do resumo |
| SPADE | Definição da plataforma na documentação |
| ISO/IEC 25010:2023 | Lista das características |
| OWASP Top 10:2025 | Ano da entrada |

## D. Arquivo original da bibliografia

A sua `bibliografia.bib` continua com a entrada `flores2005` corrompida. A correção está em `bibliografia-v6.bib`.
