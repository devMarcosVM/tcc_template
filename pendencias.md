# Pendências que dependem de você ou da orientação

Cada item informa o que falta, por que falta, onde entra e o que o texto pode afirmar enquanto o item não chega. Nenhuma pendência foi apagada do texto. As marcas `[INSERIR ...]`, `% PENDENTE` e `% CONFERIR` continuam nos arquivos.

## A. Dados que só você tem

| # | O que falta | Por que falta | Onde entra | O que se pode afirmar sem isso |
|---|---|---|---|---|
| A1 | Perfil do portfólio da Empresa A (repositórios por linguagem, origem e documentação) e a data do levantamento | Depende de levantamento autorizado | 5.2 | Apenas os números da introdução, como informação do autor |
| A2 | Autorização da Empresa A para uso dos repositórios e para a menção, mesmo anonimizada | Não há documento entre os materiais | 4.6 e 5.2 | Que o estudo depende de autorização. Não se afirma que ela existe |
| A3 | Políticas internas de segurança que podem ser citadas | Não apresentadas | 5.7 | As regras do texto são demonstrativas. Não se afirma que refletem política da empresa |
| A4 | Número de repositórios e período da coleta | Depende de A2 | 4.6 | A regra de seleção, sem o tamanho do conjunto |
| A5 | Evidência da execução do marco M1 no cenário sintético (parecer gerado, data, commit) | Afirmação de implementação sem evidência documental apresentada | 5.9 e Quadro de evidências | Que o autor declara ter concluído M0 e M1. Não se conclui que a funcionalidade não existe |
| A6 | Versões instaladas das ferramentas | Sem registro acadêmico | Capítulo 3 | Versões declaradas ou selecionadas |
| A7 | Vínculo entre as buscas da aba Strings (979 resultados) e os 240 registros exportados, e a situação "Pendente" dos 38 mantidos | A planilha não registra | 4.2 | Os dois conjuntos, descritos em separado |

## B. Decisões com a orientação

| # | Decisão | Onde entra | Estado no texto |
|---|---|---|---|
| B1 | Número e perfil dos especialistas, e se o responsável pelo repositório participa | 4.6 | `[INSERIR]`. O instrumento do Apêndice B é uma proposta |
| B2 | Necessidade de submissão a comitê de ética e forma do termo de consentimento | 4.6 e Apêndice C | Roteiro proposto. O texto não afirma aprovação |
| B3 | Manter "taxa de acerto" ou adotar "adequação percebida" | 1.5 e 4.6 | Capítulo 4 define o termo. Introdução não alterada |
| B4 | Grafia de "semi-centralizado" | Trabalho todo | Mantida a forma da introdução |
| B5 | Manter ou não o exemplo ilustrativo e os apêndices | 5.8 e apêndices | Incluídos, identificados como sintético e como propostas |
| B6 | Versão do SonarQube, já que a 9.9 não recebe correções | 3.3.5 | Ressalva incluída |
| B7 | Aplicar ou não as sugestões da introdução | Capítulo 1 | Em arquivo separado |
| B8 | Nome do Capítulo 6 | 1.6 | Não alterado |

## C. Fontes a conferir antes da entrega

| # | Fonte | O que conferir | Situação atual |
|---|---|---|---|
| C1 | ISO 19011:2018 | Definições de evidência, achado e conclusão, e o princípio da independência, na plataforma pública da ISO | Só fontes secundárias |
| C2 | IEEE 1028-2008 | Cláusula 8.1 na própria norma | Citação secundária (NASA) |
| C3 | Semgrep | Classificação das linguagens na edição comunitária e limite da análise | Não reconfirmada |
| C4 | Paulo (2026) | Página da citação direta, ou conversão em paráfrase | Só o resumo |
| C5 | LGPD, art. 46 | Texto no portal do Planalto | Visto em guias oficiais |
| C6 | Gerhardt e Silveira (2009) | Páginas sobre abordagem e natureza | Não aberta |
| C7 | Likert (1932) e Pagotto et al. (2016) | Dados bibliográficos | De memória e por fonte secundária |
| C8 | Wooldridge e Jennings, Wooldridge, Rao e Georgeff, Finin et al., FIPA, McCabe, Geiger e Halfaker, Bordini et al., Runeson e Höst | Dados bibliográficos e páginas | Entradas escritas de memória |
| C9 | Ajimati et al. e Silic et al. | Referência completa e localizador | Não verificadas |
| C10 | Moro et al. (2003) | Se o texto sustenta o que a introdução lhe atribui | Só o resumo |
| C11 | Wang et al. (2026) | Volume e páginas na versão publicada | Conferida a versão arXiv |
| C12 | Yesil, Mosciatti e Sowan | DOI e dados de publicação na página do editor | PDFs lidos, DOI não aberto |
| C13 | OWASP Top 10:2025, `semgrepDocs` e `semgrepLicensing` | Ano das entradas | Ano ausente em duas |
| C14 | SPADE | Definição da plataforma na documentação da versão usada | Só o índice foi visto |
| C15 | ISO/IEC 25010:2023 | Lista das características, se for citada | Só o resumo público |
| C16 | Lazarin et al. e Yan et al. | Páginas da versão publicada | PDFs locais são manuscritos |

## D. Fora do escopo, mas visível no PDF

- O Capítulo 6 do modelo tem uma referência indefinida, `met-atividades-primeira-etapa`.
- A sua `bibliografia.bib` original continua com a entrada `flores2005` corrompida. A correção está só em `bibliografia-v6.bib`. Se continuar usando o arquivo original, corrija o campo `url` dessa entrada.
