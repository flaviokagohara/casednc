# casednc
Repositório destinado para resolução do case da escola DNC 

Tive algumas dúvidas sobre como os dados serão utilizados. Então entendo que valeria entender um pouco melhor com o time da Zebrinha Azul sobre que tipo de informações eles estariam procurando, e entender se as APIs que nos foram passadas terão os dados necessários para poder impulsionar o seu negócio.

Agora olhando para o case em si. Irei passar como foi a parte de código e como estava pensando nos próximos passos.

- Foi bem tranquilo utilizar as API's e tentei separar o código em 3 seções para poderem ser utilizados posteriormente. Bastou ler as documentações e fazer cadastro nas plataformas para poder criar minhas chaves, e poder consultar as API's recomendadas. 
- A partir daí, eu não sei se conseguiria ser tão prático, dado que como não sei muito bem como esses dados serão usados, e nem quais dados vamos necessitar, fica um pouco difícil saber como filtrar, mas à princípio, fazendo uma suposição, entendo que poderia fazer uma limpeza na hora de disponibilizar os dados da API me concentrando apenas na duração do percuso, ao utilizar a API do maps, e sobre a de clima, poderia desconsiderar informações como ventos e nuvens, caso precise tirar algo.
- Pensando na integração em si, poderia deixar esse código rodando no Airflow, caso já tivessemos um, ou caso contrário, colocaria para rodar um cronjob para rodar esse código de 1 em 1 hora(esse seria o valor 'default', vale a pena entender a necessidade e tempo de tomada de decisão do time da Zebrinha para poder definir o melhor período de frequência).
- Esse cronjob poderia escrever em um tópico no kafka, e após isso, poderíamos fazer uma integração do kafka com o BigQuery(pensando que utillizamos essas ferramentas).
- E para deixar nossa integração mais robusta, poderíamos criar um monitoramento, talvez no Datadog, para poder analisar o nosso tópico do kafka, e nos alertar caso essa integração não esteja recebendo mensagens no tempo determinado para rodar o cronjob.
- A partir do momento que os dados estivem no nosso BigQuery(ou qualquer outro tipo de datawarehouse), poderemos pensar em modelagem, mas gostaria de utilizar a modelagem de no mínimo 3 camadas que acho que funciona bem. Essas 3 camadas consistem em uma camada de dados crus(raw) e duas camadas de dados normalizados(kitchen), uma contendo dados com o estado mais atual de determinado "id" e outra que contém os dados históricos desse "id", que com isso temos uma boa base para trabalhar e investigar futuros problemas. E o "id" aqui, poderia ser as cidades, dado que utilizamos majoritamente esse dado para fazer as consultas de API's.
- E sobre a parte de visualização de dados, caso seja necessário disponibilizar, vale entender qual a ferramenta de DataViz utilizada pela Zebrinha Azul, e poder fazer as visualizações, mas aí vale entender com o time de negócio da Zebrinha Azul, que insights esperam tirar dos dados, e qual o objetivo do uso dos dados.

PS: ainda não adicionei uma função main.py, mas a ideia no main, seria juntar os dados dos códigos, ou na verdade, só escrever no tópico do kafka, então ainda faltaria as variáveis do kafka e tudo mais. 

PS2: na pressa acabei commitando direto na main, que não é certo, deveria ter bloqueado isso no repositório, mas vou adicionar esse commit para me retratar hehe. 