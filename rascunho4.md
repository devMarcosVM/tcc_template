## Contextualização

A segurança de software é essencial para as organizações que dependem de sistemas de informação e automações em suas atividades. Vulnerabilidades no código ou em seus componentes podem comprometer dados e serviços, o que torna necessária a identificação de falhas ao longo do ciclo de vida das soluções. Para integrar essas verificações ao desenvolvimento e à entrega de software, a abordagem DevSecOps articula desenvolvimento, segurança e operações. As esteiras de integração e entrega contínuas, conhecidas pela sigla CI/CD, organizam etapas como construção, teste, empacotamento e implantação, nas quais podem ser incorporados controles sobre o código e suas dependências. As estratégias apresentadas por Chandramouli, Kautz e Torres-Arias (2024) para a segurança da cadeia de fornecimento de software oferecem uma referência para integrar esses controles. Nesse processo, as ferramentas de análise produzem evidências que precisam ser interpretadas pelos responsáveis humanos para orientar decisões sobre os riscos encontrados.

Em organizações com um portfólio de projetos e automações, esse acompanhamento envolve analisar evidências provenientes de diferentes repositórios e considerar as particularidades de cada solução. Os relatórios técnicos precisam ser relacionados à finalidade da aplicação, às dependências utilizadas e às políticas pertinentes, para que os achados possam orientar uma recomendação, aqui denominada parecer. Quando esse acompanhamento se apoia apenas na análise humana dos resultados de ferramentas tradicionais de DevSecOps, o esforço analítico tende a ser significativo, conforme discutem Zuev, Sakulin e Shmakova (2025) ao tratarem do aumento da carga cognitiva associado ao volume de informações de diferentes ferramentas e às restrições de tempo para avaliar riscos de segurança. O problema de interesse deste trabalho consiste em articular esses resultados, reunindo achados de diferentes dimensões de análise e interpretando-os de maneira que o responsável humano possa examinar a fundamentação do parecer produzido.

A diversidade das formas de criação das automações também compõe esse contexto de análise. Plataformas *low-code/no-code* (LCNC) permitem construir aplicações e automações com pouco ou nenhum código e favorecem o *citizen development*, isto é, a participação de usuários de negócio na criação de soluções. A adoção dessas práticas envolve benefícios e desafios organizacionais e técnicos, incluindo questões de segurança e governança (AJIMATI; CARROLL; MAHER, 2025). Quando as soluções incorporam inteligência artificial fora das estruturas de governança aprovadas pela organização, o fenômeno denominado *Shadow AI* envolve questões de privacidade dos dados e de responsabilidade sobre o uso da tecnologia (SILIC; SILIC; KIND-TRÜLLER, 2025). Essa variedade de autores, práticas e procedimentos de revisão pode ampliar a heterogeneidade do portfólio e tornar mais relevante o acompanhamento contínuo dos repositórios, com apoio de práticas de DevSecOps e de auditorias técnicas.

Diante do esforço que esse acompanhamento exige das pessoas, os Sistemas Multiagentes (SMA) oferecem uma possibilidade de organizar o apoio à análise por meio de agentes com responsabilidades especializadas. A comunicação estruturada permite solicitar informações e compartilhar evidências (LAZARIN et al., 2025), enquanto a definição explícita de papéis e procedimentos decisórios fornece uma base para organizar a colaboração humano-agente (AIT et al., 2025).

Na proposta deste trabalho, os agentes especialistas analisarão qualidade, segurança e dependências, e o agente de Requisitos e Documentação utilizará um modelo de linguagem para interpretar os artefatos corporativos e fornecer contexto aos demais. Por meio da comunicação direta *peer-to-peer* (P2P), os agentes poderão solicitar esclarecimentos e examinar informações de outra dimensão antes de encaminhar suas conclusões ao Agente Auditor. Este consolidará, por regras explícitas, um parecer que relacione a recomendação às evidências consideradas e às políticas aplicadas, identificando situações que demandem encaminhamento ao responsável humano.

Nesse recorte se insere o presente trabalho, que propõe desenvolver e aplicar uma prova de conceito (PoC) de arquitetura multiagente para apoiar a auditoria de repositórios do portfólio de automações da Empresa A, denominação adotada para preservar a identificação da organização. A auditoria compreenderá a coleta e a interpretação de evidências de qualidade de código, segurança e dependências em versões identificadas de repositórios autorizados. O foco da investigação será a articulação dessas evidências entre os agentes especialistas e a produção de pareceres fundamentados pelo Auditor, como apoio aos responsáveis humanos.

A aplicação será examinada por meio de uma avaliação observacional e descritiva, com registro dos achados, das interações entre agentes especialistas, das justificativas e dos pareceres. A padronização da coleta e a completude dos registros orientarão o planejamento, por adaptação das contribuições metodológicas de Zangirolami-Raimundo, Echeimberg e Leone (2018) e de Morshed, Tornetta III e Bhandari (2009) ao domínio de software. Serão examinadas a correspondência dos achados e do contexto documental com suas fontes, a vinculação das justificativas às evidências e às regras aplicadas e as informações incorporadas pelas interações P2P. A análise será complementada por uma apreciação humana estruturada da clareza, da coerência e da fundamentação dos pareceres, com acesso às evidências citadas, aos trechos documentais e às regras aplicadas. Essa apreciação não envolverá a repetição dos testes nem a produção de um parecer independente para comparação de categorias. A análise descreverá as contribuições e os limites observados, sem estimar efeitos causais.

# 2 Referencial Teórico

Este capítulo apresenta os conceitos que fundamentam o uso de uma arquitetura multiagente no apoio à auditoria de repositórios de automações. Inicialmente, são discutidas as evidências obtidas na análise dos artefatos de software e sua relação com o contexto DevSecOps. Em seguida, aborda-se o contexto de criação das automações em organizações, marcado por plataformas *low-code/no-code*, *citizen development* e *Shadow AI*. São então apresentados os sistemas multiagentes, os modelos de linguagem como capacidade de agentes, a comunicação entre participantes, as políticas de decisão, a fundamentação dos pareceres e a rastreabilidade dos registros. Por fim, são discutidos trabalhos relacionados e uma síntese das relações desses conceitos com a pesquisa.

## 2.1 Auditoria de Repositórios de Software

Um repositório reúne artefatos que podem ser examinados sob diferentes perspectivas, como o código-fonte, a declaração de dependências, os arquivos de configuração e a documentação. A análise desses elementos produz informações sobre características da solução e possíveis problemas, mas a recomendação sobre seu uso depende também da interpretação dos achados. Abordagens de apoio à decisão sobre segurança de código articulam resultados de ferramentas com critérios para formular uma recomendação ao responsável pela decisão (ZUEV; SAKULIN; SHMAKOVA, 2025).

Neste trabalho, a expressão **auditoria de repositórios** designa o procedimento delimitado de coleta, interpretação e consolidação de evidências sobre uma versão identificada dos artefatos. Assim, o parecer informa qual versão foi analisada, quais verificações foram realizadas e quais evidências fundamentam a recomendação. O procedimento constitui apoio à revisão técnica e não corresponde, por si só, a uma certificação integral do software.

### 2.1.1 Qualidade, segurança e evidências técnicas

A qualidade de um produto de software compreende propriedades que precisam ser especificadas e avaliadas de acordo com o uso pretendido. O resumo público da ISO/IEC 25010:2023 apresenta um modelo composto por características e subcaracterísticas destinado a apoiar a definição de requisitos e a avaliação da qualidade. Esse enquadramento ajuda a compreender por que uma única medida não representa, isoladamente, todas as propriedades relevantes de um produto (ISO/IEC, 2023).

Na análise automatizada, algumas dessas propriedades são examinadas por indicadores e regras sobre os artefatos. A complexidade ciclomática, por exemplo, considera os caminhos de controle do código e pode ser calculada de maneiras específicas para cada linguagem. Sua interpretação deve preservar a unidade medida, pois um valor agregado para um arquivo não descreve necessariamente uma função particular. A documentação das métricas permite conhecer o que foi calculado e em qual nível o resultado pode ser interpretado (SONARSOURCE, s.d.).

### 2.1.2 Análise de código e análise de componentes

A análise estática examina o código sem executar a aplicação, enquanto a análise dinâmica considera seu comportamento durante a execução, e essas abordagens observam aspectos diferentes e podem produzir informações complementares. Uma ferramenta pode identificar um padrão de código associado a um problema e indicar sua localização, enquanto a análise posterior examina o significado desse resultado no contexto da aplicação. A proposta de Zuev, Sakulin e Shmakova (2025) combina resultados estáticos e dinâmicos em um módulo de apoio à decisão, o que amplia as informações disponíveis, mas exige organizar os resultados para que possam sustentar uma decisão. Mesmo quando uma aplicação utiliza apenas parte dessas técnicas, o escopo do procedimento precisa indicar quais verificações foram efetivamente realizadas.

A análise do código desenvolvido pela organização também se distingue da análise dos componentes incorporados à solução. A análise de composição de software, ou *Software Composition Analysis* (SCA), está relacionada à identificação de riscos associados aos componentes de terceiros. Conhecer quais componentes e versões estão presentes é uma condição para relacioná-los às informações de risco disponíveis (SPRINGETT, s.d.).

### 2.1.3 DevSecOps e interpretação dos resultados

DevSecOps articula desenvolvimento, segurança e operações, incorporando preocupações de segurança ao processo de construção e entrega do software. As esteiras de integração e entrega contínuas organizam etapas nas quais código, componentes e outros artefatos são transformados até a disponibilização de uma versão, e a segurança da cadeia de fornecimento de software envolve examinar os elementos que participam dessas etapas e os controles aplicáveis às suas transformações (CHANDRAMOULI; KAUTZ; TORRES-ARIAS, 2024). A execução das verificações produz relatórios com localizações, classificações e métricas distintas, que ainda precisam ser relacionados a critérios de decisão para apoiar uma recomendação.

A interpretação conjunta dos resultados permite relacionar evidências de diferentes dimensões. Em um portfólio, a leitura conjunta das análises exige conservar a identificação dos repositórios, das versões e do escopo das verificações. Uma visão agregada precisa preservar o acesso aos achados que fundamentam cada parecer, para que diferenças de cobertura entre projetos possam ser reconhecidas.

## 2.2 Diversidade das Automações e Shadow AI

O desenvolvimento de aplicações pode envolver tanto profissionais de software quanto usuários de outras áreas da organização. As abordagens *low-code/no-code* (LCNC) reduzem a necessidade de programação manual e ampliam a participação desses usuários na criação de soluções, associada ao *citizen development*. A adoção dessas práticas envolve benefícios e desafios organizacionais e técnicos, incluindo questões de segurança e governança (AJIMATI; CARROLL; MAHER, 2025).

Nesse contexto, o uso de sistemas de inteligência artificial fora das estruturas de governança aprovadas pela organização é denominado *Shadow AI*. Esse fenômeno envolve questões de privacidade dos dados e de responsabilidade sobre o uso da tecnologia (SILIC; SILIC; KIND-TRÜLLER, 2025). A participação de usuários de negócio no desenvolvimento e o uso não autorizado de IA constituem aspectos distintos. Sua ocorrência em uma organização precisa ser identificada a partir das práticas e dos registros disponíveis.

Para o recorte desta pesquisa, a diversidade das formas de criação das automações compõe o contexto da auditoria. Independentemente da origem de uma solução, a interpretação dos achados exige conhecer os artefatos analisados, sua finalidade e as restrições pertinentes. A articulação entre evidências técnicas e documentais permite explicitar esse contexto na fundamentação do parecer e prepara a participação do agente de Requisitos e Documentação na arquitetura proposta. A caracterização do portfólio da Empresa A quanto à presença dessas práticas será feita com base nos registros institucionais disponíveis.

## 2.3 Sistemas Multiagentes

### 2.3.1 Agentes de software e responsabilidades

Agentes de software podem ser caracterizados por autonomia, capacidade de interação, resposta às mudanças percebidas e atuação orientada a objetivos. Na caracterização apresentada por Wooldridge e Jennings (1995), essas propriedades permitem distinguir o controle das ações e do estado do agente, sua relação com o ambiente e sua participação em interações com outros agentes.

Um sistema multiagente reúne agentes que atuam e interagem em um ambiente para alcançar objetivos individuais ou coletivos. As atividades podem envolver cooperação, coordenação e negociação, dependendo da organização e dos mecanismos de interação estabelecidos. O modelo permite tratar separadamente o comportamento de cada participante e as relações pelas quais o conjunto realiza suas atividades (LAZARIN et al., 2025).

A especialização permite distribuir atividades de análise entre participantes com responsabilidades delimitadas. Para esta pesquisa, interessa a articulação entre evidências técnicas e contexto documental, com coordenação da execução e consolidação das conclusões. Os papéis concretos dos agentes serão apresentados no capítulo da Proposta.

### 2.3.2 Modelos de agentes e coordenação

Uma organização multiagente não é determinada apenas pela quantidade de componentes. É necessário explicitar o estado mantido pelos participantes, os objetivos de suas atividades e os mecanismos pelos quais respondem às informações recebidas. O modelo *Belief-Desire-Intention* (BDI) representa crenças como conhecimento e percepções do agente, desejos como objetivos e intenções como compromissos assumidos com objetivos selecionados. Planos estabelecem maneiras de agir para persegui-los (LAZARIN et al., 2025).

Em uma aplicação de controle de acesso documental, verificações especializadas podem ser distribuídas entre agentes BDI, enquanto a lógica de autorização é expressa em planos inspecionáveis. A separação entre extração de informação, verificação de políticas e decisão final permite atribuir responsabilidades distintas aos participantes (YESIL; TEZEL; CHALLENGER, 2026).

Esses conceitos oferecem referências para compreender a organização dos agentes. Neste trabalho, a fundamentação central está na especialização dos participantes, na comunicação entre eles e na consolidação explícita dos resultados, sem pressupor a adoção integral de uma arquitetura cognitiva específica.

### 2.3.3 Modelos de linguagem em agentes

Modelos de linguagem podem participar de arquiteturas de agentes como recursos de interpretação de informações, o que faz deles uma possível capacidade de um agente e não uma definição suficiente de sistema multiagente. A interpretação de documentos é uma das possibilidades de uso, e sistemas de recuperação aumentada por geração relacionam a geração de respostas a informações recuperadas de fontes externas. Na aplicação de Yesil, Tezel e Challenger (2026), os LLMs fornecem serviços de extração de informações documentais, enquanto a decisão de autorização permanece em uma camada de regras explícitas. Essa separação oferece uma referência para distinguir a interpretação de conteúdo da autoridade para decidir.

Nesta pesquisa, o modelo de linguagem será empregado apenas no agente de Requisitos e Documentação, responsável por fornecer contexto documental aos especialistas. O modelo interpretará os documentos textuais disponíveis a partir de consultas dos especialistas motivadas pelos achados das ferramentas. As respostas deverão indicar os trechos utilizados e a relação entre as informações recuperadas e o componente analisado. Os demais agentes, inclusive o Auditor, operam por regras explícitas. Esse uso conecta a interpretação dos artefatos à comunicação entre agentes e à fundamentação das conclusões encaminhadas ao Auditor.

### 2.3.4 Contextualização documental dos achados

A contextualização documental é entendida, neste trabalho, como a associação entre um achado técnico e informações documentadas sobre o componente ao qual ele se refere, o que envolve a localização do achado, a identificação do componente, sua finalidade, os requisitos pertinentes e a criticidade declarada nos artefatos. A separação entre extração documental e decisão, exemplificada por Yesil, Tezel e Challenger (2026), oferece uma referência para organizar esse processamento, e sua aplicação à auditoria de repositórios constitui uma escolha da proposta.

Como uma menção genérica a uma funcionalidade em um documento não estabelece, por si só, quais arquivos a implementam, e uma criticidade declarada difere de uma classificação inferida, as regras dessa associação são detalhadas no capítulo da Proposta.

## 2.4 Comunicação e Cooperação entre Agentes

### 2.4.1 Mensagens, finalidade e transporte

A comunicação permite que agentes compartilhem informações e formulem solicitações relacionadas às suas atividades. Para que a troca possa ser interpretada, é necessário considerar tanto o conteúdo transmitido quanto sua finalidade. Linguagens de comunicação como KQML representam intenções comunicativas, permitindo distinguir, por exemplo, o fornecimento de uma informação de uma consulta dirigida a outro participante (LAZARIN et al., 2025).

A finalidade da mensagem, sua representação e seu transporte correspondem a aspectos diferentes. Lazarin et al. (2025) apresentam uma arquitetura que transporta mensagens KQML por protocolos de correio eletrônico, traduzindo os elementos entre a linguagem dos agentes e o formato utilizado no envio. O trabalho ilustra que o canal de comunicação pode ser escolhido sem eliminar a necessidade de uma estrutura que permita aos participantes interpretar a mensagem.

A interpretação de uma troca depende da identificação dos participantes, da finalidade comunicativa e do conteúdo relacionado à solicitação. O formato de representação das mensagens e o protocolo de transporte materializam aspectos diferentes dessa interação, cuja especificação será apresentada nos capítulos de Suporte Tecnológico e Proposta.

### 2.4.2 Interações P2P e reavaliação das conclusões

A comunicação *peer-to-peer* (P2P) é empregada neste trabalho no sentido de troca lógica direta entre agentes especialistas. Uma pergunta formulada por Segurança poderá ser encaminhada a Qualidade ou a Requisitos e Documentação, cuja resposta retornará ao solicitante. A existência de coordenação da etapa ou de um servidor de transporte não modifica, por si só, essa relação lógica entre os participantes.

A cooperação ocorre quando as informações compartilhadas contribuem para uma atividade conjunta, preservando as responsabilidades de cada agente. Ela pode assumir a forma de uma consulta contextual, na qual um especialista solicita uma informação que outro tem condições de fornecer e examina sua pertinência antes de concluir a própria análise. A possibilidade de cooperação, coordenação e negociação integra o contexto de interação dos sistemas multiagentes (LAZARIN et al., 2025).

Na auditoria, uma consulta pode relacionar um alerta às medidas de qualidade do mesmo arquivo ou à finalidade documentada do componente. O valor analítico da interação está na informação acrescentada à conclusão e na possibilidade de examinar sua origem. Uma resposta pode fundamentar a manutenção da conclusão ou sua revisão segundo os critérios aplicáveis.

A interpretação das interações exige considerar seu contexto e sua finalidade. Ao estudar bots da Wikipédia, Geiger e Halfaker (2017) identificaram que interações anteriormente classificadas como conflitos eram, em muitos casos, atividades rotineiras e colaborativas. Essa contribuição oferece uma referência para examinar o significado das trocas entre agentes, além de sua frequência. Na presente pesquisa, o registro das perguntas, das respostas e das conclusões permitirá identificar quais informações foram compartilhadas e como foram incorporadas à análise dos especialistas, distinguindo também a ausência de resposta da indisponibilidade da informação.

Neste recorte, uma consulta seguida de resposta será descrita como intercâmbio ou contextualização de evidências. O termo negociação será reservado a mecanismos que explicitem propostas, critérios e procedimentos de resolução de divergências. Essa distinção evita atribuir ao sistema um processo decisório mais amplo do que aquele efetivamente especificado.

## 2.5 Governança e Apoio à Decisão

### 2.5.1 Políticas, regras e responsabilidades

A governança de projetos de software envolve tornar explícitos os papéis, as responsabilidades e os procedimentos pelos quais decisões são tomadas. Uma política pode estabelecer quem participa, sobre qual escopo atua e quais condições orientam a resolução de uma decisão. A representação estruturada desses elementos permite que o procedimento seja interpretado e, em determinadas condições, executado por um mecanismo computacional. Em uma auditoria, essa representação permite relacionar os achados a critérios identificáveis e exige que o escopo e a versão da política sejam conhecidos (AIT et al., 2025).

No contexto de sistemas multiagentes normativos, regras podem representar obrigações, permissões e proibições. O processamento dessas normas é distinto da aplicação de sanções, que exige representar consequências e mecanismos próprios de execução. A separação entre norma, identificação de conformidade e consequência é relevante para compreender quais responsabilidades são atribuídas aos agentes (YAN et al., 2025).

A aplicação de uma política exige distinguir o texto que expressa uma diretriz de sua representação executável. Recuperar uma passagem de um documento corporativo permite localizar uma orientação; estabelecer as condições que produzirão determinada categoria de parecer exige especificação própria. Na proposta, as regras de decisão serão previamente definidas e versionadas, com identificação de sua origem e de seu escopo. Regras demonstrativas e regras institucionais deverão ser distinguidas.

### 2.5.2 Pareceres e delimitação da decisão

O apoio à decisão organiza informações e critérios para produzir uma recomendação examinável. Em segurança de código, essa organização pode separar a coleta dos resultados, seu processamento e a decisão proposta ao usuário, de modo que a recomendação decorra da relação estabelecida entre os dados e o modelo de decisão, preservando o papel do responsável pelo software. Nesse contexto, a categoria de um parecer deve ser interpretada junto com o escopo verificado e com o estado das ferramentas, pois falhas de coleta ou informações insuficientes limitam a conclusão sobre o que foi examinado (ZUEV; SAKULIN; SHMAKOVA, 2025).

Um parecer pode reunir os achados, as conclusões especializadas, o contexto documental disponível e as regras que fundamentam a categoria atribuída. A justificativa será organizada em uma estrutura predefinida a partir desses elementos. O Auditor consolida essa relação por regras explícitas e pode indicar situações que demandem encaminhamento ao responsável pelo software. A leitura do parecer permite examinar a relação entre as justificativas, as evidências apresentadas e a recomendação. Nesta pesquisa, essa relação também será objeto de apreciação humana estruturada, cujos critérios e procedimentos serão definidos na Metodologia.

### 2.5.3 Explicabilidade, proveniência e rastreabilidade

A explicabilidade interessa à compreensão de como uma conclusão foi produzida e de quais elementos permitem examiná-la. No recorte do projeto, ela será operacionalizada pela justificativa que relaciona o parecer aos achados e às regras aplicadas. A proveniência descreve a origem das informações utilizadas, e a rastreabilidade permite seguir suas relações e localizar os registros necessários à reconstrução do procedimento. A organização de tarefas, a vinculação às fontes e o registro da execução são elementos discutidos em propostas de fluxos governáveis e auditáveis (ROUSEK, 2026).

A presença de uma justificativa bem redigida não assegura que ela seja sustentada pelas evidências. Fluxos apoiados por modelos de linguagem podem produzir afirmações sem suporte, e o registro da origem das informações não elimina a necessidade de examinar sua adequação à conclusão. Por isso, a vinculação entre evidência, processamento e resultado precisa ser preservada e inspecionável (ROUSEK, 2026).

Quando um modelo de linguagem participa da interpretação documental, a rastreabilidade abrange os documentos consultados, os trechos recuperados, as entradas e as respostas produzidas, além da identificação do modelo e de sua configuração. Esses registros tornam examinável a origem do contexto incorporado às conclusões. Em aplicações de apoio à decisão, trilhas de decisão também conservam etapas e encaminhamentos relevantes. Sua utilidade para conformidade e responsabilização depende de avaliação específica, como reconhecem Sowan et al. (2026) ao delimitar os resultados de AEGIS-Chain.

## 2.6 Trabalhos Relacionados

Esta seção aproxima a fundamentação das soluções investigadas na literatura. Os trabalhos são discutidos segundo o problema tratado, a organização da solução e os elementos pertinentes à proposta. A relação temática não implica equivalência de domínio, de método ou de resultado.

### 2.6.1 Apoio à decisão sobre evidências de software

Zuev, Sakulin e Shmakova (2025) apresentam uma abordagem híbrida que utiliza resultados de análises estática e dinâmica em um módulo de apoio à decisão sobre segurança de código. O trabalho relaciona relatórios de vulnerabilidades, critérios de processamento e uma recomendação de incorporação de código. Para esta pesquisa, a aproximação está na passagem dos resultados das ferramentas para uma decisão fundamentada. A solução descrita não estabelece o intercâmbio P2P entre especialistas de auditoria que constitui o foco desta proposta.

GateLens, apresentado por Khoee et al. (2026), trata da análise de dados de releases de software automotivo. A arquitetura utiliza álgebra relacional como representação intermediária entre consultas em linguagem natural e código executável. Seu interesse para o TCC está na possibilidade de inspecionar as transformações entre entrada e resultado, o que se aproxima da necessidade de verificar o que um modelo de linguagem produz a partir de evidências estruturadas. Contudo, a unidade avaliada é a consulta sobre dados tabulares, e a solução não depende de orquestração multiagente.

### 2.6.2 Comunicação e consolidação por agentes especializados

Lazarin et al. (2025) desenvolvem uma arquitetura de comunicação baseada em Jason para troca de mensagens KQML por IMAP e SMTP. A contribuição pertinente está na representação da intenção comunicativa e na integração entre agentes e um meio de transporte. O domínio de agentes embarcados e interação por correio eletrônico é distinto da auditoria de repositórios, e o trabalho não estabelece um protocolo para interpretar achados de scanners.

Yesil, Tezel e Challenger (2026) apresentam uma arquitetura BDI para controle de acesso em recuperação aumentada por geração multimodal. Verificações textuais e visuais produzem sinais de autorização que são combinados por um agente de decisão. A separação entre extração, verificação e consolidação oferece uma referência para organizar responsabilidades. A combinação por disjunção lógica responde ao problema de autorização tratado pelos autores; a auditoria requer critérios próprios de consolidação.

### 2.6.3 Políticas e fluxos governáveis

Ait et al. (2025) propõem uma DSL para representar participantes, papéis, escopos e procedimentos de governança em projetos de software. A proposta inclui um mecanismo de decisão e uma prova de conceito. Sua contribuição para o presente trabalho está na explicitação de como uma regra se relaciona aos participantes e ao contexto em que deve ser aplicada. O artigo não demonstra a eficácia de pareceres de auditoria de repositórios.

Yan et al. (2025) tratam da representação de normas e sanções em uma arquitetura normativa BDI. A distinção entre identificação de conformidade, decisão e aplicação de consequências é relevante para delimitar o Auditor. Essa distinção permite caracterizar a emissão de uma recomendação separadamente da execução de consequências.

Rousek (2026) apresenta um framework conceitual para fluxos governáveis de apoio à decisão em defesa, articulando decomposição de tarefas, proveniência e controle delimitado. A obra oferece elementos para especificar registros e responsabilidades, mas declara não realizar validação empírica do framework. Sua contribuição será utilizada como referência conceitual, preservando a diferença entre o domínio de defesa e a aplicação em repositórios de automações.

### 2.6.4 Separação de funções e registros de decisão

Mosciatti et al. (2026) desenvolvem uma arquitetura multiagente para operações de segurança de dispositivos e aplicações com interfaces web, demonstrada na rotação de credenciais. Os agentes possuem funções e permissões delimitadas, incluindo uma fase própria de validação do resultado. A separação de funções oferece uma referência para limitar o alcance das ações de cada participante. O estudo distingue a validação interna da verificação humana empregada em sua avaliação. Para esta pesquisa, a contribuição considerada é a organização das responsabilidades e das verificações internas.

Sowan et al. (2026) apresentam AEGIS-Chain, uma arquitetura de apoio à decisão em cadeias de suprimentos com etapas de processamento, limites operacionais, escalonamento humano e trilhas de decisão. A contribuição pertinente está no registro do processo e na identificação de situações que demandam encaminhamento. A avaliação por simulação e o domínio de cadeias de suprimentos limitam a transferência de seus resultados. Os próprios autores reconhecem que a utilidade dos registros para conformidade e responsabilização permanece sem validação empírica.

### 2.6.5 Síntese e posicionamento da proposta

| Trabalho | Elemento pertinente | Distinção em relação à proposta |
|---|---|---|
| Zuev, Sakulin e Shmakova (2025) | Integração de resultados de análises com apoio à decisão | Não estabelece o P2P entre especialistas de auditoria |
| Khoee et al. (2026) | Representação intermediária inspecionável entre linguagem natural e resultado | Trata de consultas sobre releases, sem depender de orquestração multiagente |
| Lazarin et al. (2025) | Mensagens com finalidade comunicativa explícita | Emprega Jason, KQML e transporte por correio eletrônico em outro domínio |
| Yesil, Tezel e Challenger (2026) | Verificações especializadas e consolidação por regras | Trata de autorização multimodal, e sua regra de fusão não define a política do Auditor |
| Ait et al. (2025) | Representação de papéis, escopo e procedimentos decisórios | Propõe uma DSL de governança, sem avaliar os pareceres deste domínio |
| Yan et al. (2025) | Representação de normas e consequências | Implementa capacidades normativas e sanções que não se confundem com emitir um parecer |
| Rousek (2026) | Proveniência e controle delimitado de fluxos | Apresenta um framework conceitual, sem validação empírica |
| Mosciatti et al. (2026) | Separação de funções e permissões | Executa operações de segurança por interfaces web, em vez de analisar repositórios |
| Sowan et al. (2026) | Trilhas de decisão e encaminhamento de situações | Avalia simulações de cadeias de suprimentos, com limites declarados para a utilidade dos registros |

A proposta articula esses elementos na auditoria de repositórios de automações. Os especialistas examinam evidências técnicas e compartilham informações por comunicação P2P. O agente de Requisitos e Documentação utiliza um modelo de linguagem para recuperar e interpretar contexto documental pertinente aos componentes analisados, conservando os trechos e as relações que sustentam suas respostas. O Auditor consolida as conclusões e aplica regras explícitas para produzir um parecer fundamentado. O interesse da investigação está em descrever as interações, a incorporação do contexto e a rastreabilidade dos pareceres nas condições observadas.

## 2.7 Considerações Finais do Capítulo

A auditoria de repositórios envolve evidências técnicas e informações sobre a finalidade e os requisitos das soluções. Os sistemas multiagentes oferecem uma forma de distribuir responsabilidades, enquanto a comunicação entre especialistas permite compartilhar informações pertinentes às conclusões individuais. A interpretação documental apoiada por modelos de linguagem pode fornecer contexto a essas interações. A consolidação por regras explícitas estabelece a relação entre as conclusões e a categoria do parecer.

Esses conceitos fundamentam uma arquitetura voltada à produção de pareceres cuja origem possa ser examinada. A proveniência das evidências, o registro das interações e a vinculação às regras permitem analisar a rastreabilidade do procedimento. As tecnologias que materializam esses elementos serão descritas no capítulo de Suporte Tecnológico, os procedimentos de coleta e análise, na Metodologia, e os papéis, os fluxos e as regras da solução, no capítulo da Proposta.

# 3 Suporte Tecnológico

Este capítulo apresenta as ferramentas utilizadas ou previstas para a elaboração da monografia, a modelagem da arquitetura e o desenvolvimento da prova de conceito. A seção de apoio geral descreve os recursos de redação e organização bibliográfica. Em seguida, são apresentados o suporte à modelagem dos agentes e as tecnologias de implementação, comunicação, análise de software e interpretação documental. Ao final, um quadro sintetiza a finalidade e a situação de adoção dos principais componentes.

## 3.1 Ferramentas de Apoio Geral

### 3.1.1 LaTeX

LaTeX é um sistema de preparação de documentos que oferece recursos para composição de textos científicos, referências cruzadas, figuras, tabelas e bibliografias (THE LATEX PROJECT, s.d.). Neste trabalho, será utilizado para organizar e formatar a monografia a partir do template adotado pelo curso. Os arquivos de texto dos capítulos, as referências bibliográficas e as figuras serão reunidos nesse projeto de redação.

### 3.1.2 Zotero

Zotero é um gerenciador de referências que permite reunir registros bibliográficos, organizar fontes em coleções e associar arquivos e notas aos itens cadastrados (ZOTERO, s.d.). Seu uso no trabalho apoia a organização do acervo consultado e a recuperação dos documentos utilizados na fundamentação.

Os registros bibliográficos serão conferidos quanto à autoria, ao título, ao ano e à identificação da publicação. A planilha de levantamento permanecerá como registro dos critérios e das decisões de seleção, distinguindo os estudos selecionados da literatura complementar. O gerenciamento das referências auxilia esse processo, enquanto a análise de pertinência e do conteúdo das fontes integra os procedimentos metodológicos da pesquisa.

## 3.2 Ferramentas de Modelagem

### 3.2.1 draw.io

O draw.io, também conhecido como diagrams.net, será utilizado para elaborar as representações visuais da arquitetura e das interações entre agentes. A ferramenta permite conservar os diagramas em formato editável e exportar figuras em formatos como SVG e PDF, adequados à preparação dos materiais da monografia (DRAW.IO, s.d.).

A modelagem compreenderá uma visão da arquitetura, com os agentes e suas relações com ferramentas e documentos, e diagramas de sequência para representar a ordem das mensagens. Esses diagramas permitirão explicitar a distribuição das tarefas, as consultas P2P, o compartilhamento de contexto e o encaminhamento das conclusões ao Auditor. Diagramas de atividades poderão complementar a representação dos fluxos que envolvem decisões, falhas ou informação insuficiente.

As representações distinguirão a arquitetura alvo do recorte implementado no protótipo inicial. Os arquivos editáveis serão conservados para acompanhar a evolução do projeto, e as figuras serão apresentadas e discutidas no capítulo da Proposta. O emprego da ferramenta apoia a comunicação do modelo; a definição das responsabilidades e das regras de interação permanece como atividade de projeto.

## 3.3 Ferramentas de Desenvolvimento


### 3.3.1 Python

Python será utilizado na implementação dos agentes, dos adaptadores das ferramentas e do processamento dos registros da auditoria. A biblioteca `asyncio` disponibiliza recursos para programação assíncrona, comunicação de rede e controle de subprocessos, pertinentes às atividades de envio de mensagens e acompanhamento das ferramentas externas (PYTHON SOFTWARE FOUNDATION, s.d.).

A escolha da linguagem está articulada à utilização de SPADE e à integração dos componentes da prova de conceito. O protótipo inicial registra o uso de Python 3.13.7. Essa versão identifica o ambiente de desenvolvimento já empregado; as versões efetivamente utilizadas na aplicação da pesquisa serão conservadas junto aos registros de execução.

A linguagem de implementação da arquitetura é independente das linguagens dos repositórios analisados. A cobertura de Python, TypeScript e PHP dependerá das ferramentas, dos artefatos disponíveis e da configuração de cada análise. A demonstração inicial utiliza um repositório sintético Python, constituindo um recorte de implementação anterior à aplicação em repositórios autorizados da Empresa A.

### 3.3.2 SPADE

SPADE, sigla de *Smart Python Agent Development Environment*, é uma plataforma de sistemas multiagentes desenvolvida em Python e baseada em XMPP. Sua documentação apresenta um modelo de agentes organizado por comportamentos e apoiado em `asyncio`, além da possibilidade de utilizar servidores XMPP externos (SPADE, s.d.).

Na prova de conceito, SPADE será empregado na construção dos agentes e no envio e recebimento de mensagens. O protótipo inicial utiliza a versão 4.1.4 e mantém quatro participantes em processos separados: Orquestrador, Qualidade, Segurança e Auditor. O agente de Requisitos e Documentação integra a arquitetura alvo e será acrescentado na etapa de interpretação documental.

Essa separação permite conservar a identidade dos participantes e acompanhar a origem das mensagens. As consultas P2P são encaminhadas entre especialistas; o Orquestrador organiza a execução, e o Auditor recebe as conclusões para consolidação. O emprego de SPADE fornece a infraestrutura de agentes, enquanto os comportamentos e os critérios de análise são especificados pelo projeto.

### 3.3.3 XMPP e Prosody

O transporte das mensagens utilizará XMPP, protocolo empregado por SPADE. Prosody é o servidor selecionado para o ambiente inicial, com recursos documentados de configuração, módulos e certificados para a operação do serviço (PROSODY, s.d.). Cada agente utilizará uma identidade própria para participar da comunicação.

A comunicação P2P adotada corresponde à relação lógica entre os agentes que formulam e respondem às consultas. O servidor transporta as mensagens, preservando a possibilidade de uma solicitação de Segurança ser respondida diretamente por Qualidade ou por Requisitos e Documentação. A presença desse serviço é compatível com o intercâmbio entre especialistas definido na proposta.

O protótipo registra os identificadores das auditorias e das solicitações para relacionar perguntas, respostas e conclusões. Tempos de espera e estados de falha permitem identificar interações não concluídas. Esses registros serão utilizados na análise do funcionamento da arquitetura, conforme os procedimentos definidos na Metodologia.

### 3.3.4 Docker Compose

Docker Compose permite definir e executar aplicações compostas por múltiplos contêineres, reunindo configurações de serviços, redes e volumes em um arquivo YAML (DOCKER, s.d.). No protótipo, esse recurso organiza os serviços de infraestrutura necessários à comunicação e à análise de código.

As configurações do ambiente serão conservadas para identificar os serviços utilizados e suas versões. As credenciais de acesso serão fornecidas por configuração externa ao código-fonte, incluindo variáveis de ambiente para os tokens exigidos pelas ferramentas. Essa organização permite distinguir os parâmetros públicos de execução dos valores de acesso que não devem integrar os relatórios da pesquisa.

### 3.3.5 SonarQube e SonarScanner

SonarQube produz medidas de qualidade e ocorrências de violação das regras de análise. Sua documentação informa que a cobertura depende da linguagem e da edição utilizada. O SonarScanner realiza a análise configurada e envia um relatório ao servidor, cujo processamento ocorre de forma assíncrona (SONARSOURCE, s.d.).

No protótipo inicial, SonarQube fornece as evidências consultadas pelo agente de Qualidade. O adaptador acompanha o processamento da tarefa e relaciona os resultados à análise e à revisão do repositório. Assim, a conclusão da execução do scanner não é tomada isoladamente como indicação de que os resultados já estão disponíveis para consulta.

As medidas conservam sua granularidade. Um resultado agregado por arquivo será interpretado nesse nível, sem atribuição automática a uma função específica. O estado do *Quality Gate* será conservado como informação da ferramenta; a categoria do parecer será determinada pelas regras do Auditor.

O ambiente inicial registra SonarQube Community 9.9.8.100196 e SonarScanner CLI 8.1.0.6389. A cobertura efetiva dos repositórios selecionados será verificada antes da aplicação. Esses números documentam o ambiente empregado e não representam uma recomendação geral de implantação institucional.

### 3.3.6 Bandit

Bandit é uma ferramenta voltada à identificação de problemas comuns de segurança em código Python. Seu processamento constrói uma árvore sintática abstrata dos arquivos e aplica verificações sobre seus nós, produzindo um relatório dos achados (BANDIT, s.d.).

A versão 1.9.4 foi integrada ao protótipo inicial como fonte de evidências para Segurança. Os resultados preservam a identificação da regra, a localização e as classificações emitidas pela ferramenta. O especialista pode consultar medidas do SonarQube referentes ao mesmo arquivo para contextualizar um achado, conservando a distinção entre complexidade e evidência de vulnerabilidade.

A utilização de Bandit está delimitada aos arquivos Python. A análise de repositórios TypeScript e PHP exige ferramentas e configurações correspondentes às linguagens presentes. O protótipo não executa a aplicação auditada nem modifica seus arquivos para obter os resultados desses scanners.

### 3.3.7 Ferramentas para Dependências e Ampliação de Cobertura

A dimensão de dependências requer identificar componentes e versões para relacioná-los a informações sobre vulnerabilidades conhecidas. A integração correspondente ainda não compõe o protótipo inicial. As ferramentas apresentadas a seguir são candidatas à ampliação e deverão ser selecionadas conforme os manifestos e os gerenciadores encontrados nos repositórios.

| Ferramenta | Aplicação prevista | Condição de utilização |
|---|---|---|
| pip-audit | Consulta de vulnerabilidades conhecidas em dependências Python | Identificação das dependências e versões em formato compatível |
| npm audit | Auditoria de dependências de projetos que utilizam npm, inclusive aplicações TypeScript | Presença de estrutura de dependências compatível com npm |
| Composer audit | Consulta de avisos de segurança associados a pacotes gerenciados por Composer | Projeto PHP que utilize Composer e permita identificar as versões analisadas |
| Trivy | Verificações adicionais de vulnerabilidades, segredos e configurações, conforme alvo e modo | Seleção explícita do escopo e dos formatos suportados |

As funções dessas ferramentas são descritas em suas documentações oficiais (PYTHON PACKAGING AUTHORITY, s.d.; NPM, s.d.; COMPOSER, s.d.; AQUA SECURITY, s.d.). A seleção final deverá evitar a interpretação de relatórios sobrepostos como evidências independentes de um mesmo problema. Também deverá conservar a data da consulta e a identificação das fontes de informação utilizadas.

Os adaptadores serão configurados para coleta de evidências. Comandos de correção automática, atualização de pacotes ou execução da aplicação não integram esse procedimento. A ausência de um manifesto compatível será registrada como limitação de cobertura, e não como ausência de vulnerabilidades.

### 3.3.8 Modelo de Linguagem e Execução Local

O agente de Requisitos e Documentação utilizará um modelo de linguagem para interpretar documentos textuais a partir das consultas dos especialistas. A aplicação apresentada por Yesil, Tezel e Challenger (2026) oferece uma referência para separar a extração de informações documentais da decisão orientada por regras. Nesta proposta, o modelo fornecerá contexto, enquanto a categoria do parecer permanecerá vinculada às regras do Auditor.

A execução local será considerada como alternativa para disponibilizar o modelo ao agente de Requisitos e Documentação. Entre os recursos em avaliação está o Ollama, que oferece uma interface de programação para integração de aplicações com modelos executados localmente (OLLAMA, s.d.-a). Nessa configuração, o agente encaminhará as consultas ao serviço de inferência e receberá as respostas para processamento e registro. A comunicação com esse serviço complementará a comunicação entre agentes realizada por SPADE.

A seleção do modelo considerará a capacidade de interpretar documentos em português, a fundamentação das respostas nos trechos fornecidos, o reconhecimento de informação insuficiente, o tempo de resposta e o consumo de memória. O tamanho do contexto também será considerado, pois sua ampliação aumenta a memória necessária à execução (OLLAMA, s.d.-b). Esses critérios orientarão a escolha de uma configuração compatível com a tarefa de contextualização documental, a ser examinada pelos procedimentos definidos na Metodologia.

A execução local permitirá organizar o processamento dos documentos no ambiente definido para a pesquisa, observadas as condições de acesso e tratamento dos dados da organização. A adoção do Ollama e a escolha do modelo permanecem condicionadas à verificação de sua adequação à tarefa. Serão registrados a identificação e a versão do modelo, a quantização, quando utilizada, o tamanho de contexto e os parâmetros de geração, juntamente com as entradas e as respostas produzidas. Esses registros apoiarão a rastreabilidade das condições em que o contexto documental foi obtido.

A integração deverá receber a consulta do especialista, identificar os documentos pertinentes e conservar os trechos utilizados na resposta. O uso de recuperação aumentada por geração é uma possibilidade de implementação; sua adoção, o mecanismo de busca e a eventual necessidade de indexação serão especificados após a definição do corpus documental. Não há banco vetorial escolhido nesta etapa.

O suporte técnico deverá permitir registrar informação insuficiente, resposta sem apoio documental e conflito entre fontes. Esses estados são necessários para distinguir um contexto recuperado de uma conclusão que não pôde ser sustentada. Os critérios de aceitação das respostas e a ligação entre arquivos e componentes serão detalhados na Proposta.

### 3.3.9 Versionamento, Registros e Apresentação

Git será empregado na identificação das revisões dos repositórios examinados e no acompanhamento das alterações do projeto. O sistema conserva o histórico dos repositórios, permitindo relacionar o código a uma revisão identificada (GIT, s.d.). Na auditoria, o identificador do commit integrará os registros utilizados para delimitar a versão analisada.

O protótipo utiliza arquivos JSON para evidências e pareceres e registros JSONL para eventos da execução. As regras do Auditor são armazenadas em YAML, permitindo conservar a política utilizada em cada auditoria. Esses formatos constituem escolhas de implementação voltadas à organização dos dados e à inspeção posterior do procedimento.

As dependências do código incluem Pydantic, HTTPX e PyYAML. No projeto, elas apoiam, respectivamente, a validação estrutural dos dados, as consultas HTTP às ferramentas e o carregamento da configuração de políticas. A validação de estrutura verifica a forma dos registros; a análise de sua fundamentação depende também das relações entre evidências, contexto e regras.

A identificação do commit, das ferramentas e das configurações permitirá relacionar o parecer à versão examinada. Os resultados originais dos scanners serão conservados junto às evidências normalizadas e às mensagens pertinentes. A organização do relatório deverá permitir localizar a fonte de uma afirmação e acompanhar sua participação na conclusão.

Para a apreciação humana estruturada, será preparado um material de leitura com o parecer, as evidências citadas, os trechos documentais e as regras acionadas. O instrumento de registro das apreciações será definido na Metodologia. A pessoa avaliará a clareza, a coerência e a fundamentação desse material, sem realizar uma nova auditoria independente.

A apresentação consolidada das auditorias poderá incluir um painel, acompanhado dos relatórios detalhados. A tecnologia dessa interface ainda não foi selecionada. Sua definição deverá preservar o acesso às evidências e às limitações de cada execução, para que a visão agregada não oculte diferenças de cobertura entre repositórios.

## 3.4 Resumo do Capítulo

O suporte tecnológico articula recursos de redação e organização bibliográfica, modelagem e implementação. Python e SPADE sustentam os agentes; Prosody viabiliza o transporte das mensagens; e SonarQube e Bandit fornecem as evidências do protótipo inicial. A interpretação documental e a ampliação da análise de dependências serão integradas nas etapas seguintes, conforme a seleção dos componentes e o escopo dos repositórios.

| Tecnologia ou recurso | Categoria | Finalidade no trabalho | Versão ou situação |
|---|---|---|---|
| LaTeX | Apoio geral | Redação e formatação da monografia | Projeto de redação existente; distribuição a registrar |
| Zotero | Apoio geral | Organização do acervo e das referências | Em uso; versão a registrar |
| draw.io | Modelagem | Arquitetura e sequências de interação | Uso previsto; versão a registrar |
| Python | Desenvolvimento | Implementação dos agentes e adaptadores | 3.13.7 no protótipo inicial |
| SPADE | Desenvolvimento | Comportamentos e mensagens dos agentes | 4.1.4 no protótipo inicial |
| Prosody | Desenvolvimento | Servidor XMPP | 13.0 nightly build 100 no protótipo inicial |
| Docker Compose | Desenvolvimento | Configuração dos serviços | Utilizado; versão a registrar |
| SonarQube Community | Desenvolvimento | Medidas e achados de código | 9.9.8.100196 no protótipo inicial |
| SonarScanner CLI | Desenvolvimento | Envio das análises ao SonarQube | 8.1.0.6389 no protótipo inicial |
| Bandit | Desenvolvimento | Análise de segurança em Python | 1.9.4 no protótipo inicial |
| pip-audit, npm audit, Composer audit e Trivy | Desenvolvimento | Ampliação da cobertura de análise | Candidatos; seleção e integração pendentes |
| Ollama e modelo de linguagem | Desenvolvimento | Serviço de interpretação documental | Em avaliação; modelo a selecionar |
| Git | Desenvolvimento | Histórico e identificação das revisões | Utilizado; versão a registrar |
| JSON, JSONL e YAML | Formatos de apoio à implementação | Evidências, eventos e políticas | Utilizados no protótipo inicial |
| Painel e material de leitura dos pareceres | Apresentação | Consulta aos resultados e às evidências | Tecnologia da interface e instrumento a definir |

Fonte: elaboração do autor, a partir do projeto e dos registros do protótipo inicial.

As versões indicadas documentam o ambiente já empregado e serão atualizadas conforme a configuração efetiva da aplicação da pesquisa. Os procedimentos de avaliação e apreciação humana serão definidos na Metodologia. A arquitetura, os diagramas de interação e os critérios de consolidação dos pareceres serão detalhados na Proposta.
@misc{pythonAsyncio,
  author = {{Python Software Foundation}},
  title = {asyncio — Asynchronous I/O},
  url = {https://docs.python.org/3.13/library/asyncio.html},
  urlaccessdate = {5 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{spadeDocs,
  author = {{SPADE}},
  title = {SPADE 4.1.4 documentation},
  url = {https://spade-mas.readthedocs.io/en/latest/readme.html},
  urlaccessdate = {5 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{prosodyDocs,
  author = {{Prosody}},
  title = {Documentation},
  url = {https://prosody.im/doc/},
  urlaccessdate = {5 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{dockerCompose,
  author = {{Docker}},
  title = {Docker Compose},
  url = {https://docs.docker.com/compose/},
  urlaccessdate = {5 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{sonarAnalysis99,
  author = {{SonarSource}},
  title = {SonarQube Server 9.9: Analysis overview},
  url = {https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/overview},
  urlaccessdate = {5 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{banditDocs,
  author = {{Bandit}},
  title = {Bandit documentation},
  url = {https://bandit.readthedocs.io/en/latest/},
  urlaccessdate = {5 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{pipAuditDocs,
  author = {{Python Packaging Authority}},
  title = {pip-audit},
  url = {https://github.com/pypa/pip-audit},
  urlaccessdate = {5 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{npmAuditDocs,
  author = {{npm}},
  title = {npm audit: CLI v11},
  url = {https://docs.npmjs.com/cli/v11/commands/npm-audit/},
  urlaccessdate = {5 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{composerAuditDocs,
  author = {{Composer}},
  title = {Command-line interface: audit},
  url = {https://getcomposer.org/doc/03-cli.md#audit},
  urlaccessdate = {5 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{trivyDocs,
  author = {{Aqua Security}},
  title = {Trivy: Overview},
  url = {https://trivy.dev/docs/latest/guide/},
  urlaccessdate = {5 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{ollamaApi,
  author = {{Ollama}},
  title = {Introduction: API reference},
  url = {https://docs.ollama.com/api/introduction},
  urlaccessdate = {5 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{ollamaContext,
  author = {{Ollama}},
  title = {Context length},
  url = {https://docs.ollama.com/context-length},
  urlaccessdate = {5 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{latexProject,
  author = {{The LaTeX Project}},
  title = {An introduction to LaTeX},
  url = {https://www.latex-project.org/about/},
  urlaccessdate = {6 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{zoteroGuide,
  author = {{Zotero}},
  title = {The Basics},
  url = {https://www.zotero.org/support/quick_start_guide},
  urlaccessdate = {6 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{drawioExport,
  author = {{draw.io}},
  title = {Supported export formats},
  url = {https://www.drawio.com/docs/manual/export/export-diagram/},
  urlaccessdate = {6 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}

@misc{gitAbout,
  author = {{Git}},
  title = {About Git},
  url = {https://git-scm.com/about},
  urlaccessdate = {6 nov. 2026},
  note = {Documentação online; data de publicação não identificada}
}
