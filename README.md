# backdoor-algorithm

Um backdoor é um tipo de vulnerabilidade de segurança que permite a um invasor acessar um sistema ou rede de forma não autorizada. 
Isso pode ser feito de várias maneiras, como através de um código malicioso ou de uma configuração inadequada do sistema.

Esse código cria um servidor que escuta a porta 1234 e aceita conexões de clientes. 
Quando um cliente se conecta, o servidor fica em loop aguardando por comandos para executar. 
Quando um comando é recebido, o servidor o executa e envia o resultado de volta para o cliente. 
Isso permite que o invasor envie comandos para o sistema de forma remota e obtenha o resultado da execução.
