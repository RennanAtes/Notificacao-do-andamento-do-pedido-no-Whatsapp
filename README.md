# Notificacao-do-andamento-do-pedido-no-Whatsapp
Código que envia o Status do pedido do cliente via Whatsapp, por exemplo: Pedido pendente, pedido aprovado, faturando, em viagem ... Todas as mensagens podem ser personalizadas.

Projeto próprio para estudo, se forem usar cuidado com a LGPD, você precisa ter autorização para utilizar os dados do seu cliente!

Ferramenta que se conecta no banco de dados da empresa, e atualiza os clientes sobre a atualização de rastreio da sua encomenda. A lógica por trás do sistema é passar por todos os pedidos do banco de dados e salvar dentro de uma planilha local, assim quando o pedido do banco de dados for diferente do pedido que esta na planilha local, quer dizer que ouve alguma alteração, depois disso ele passa por uma verificação dessa mudança, e se estiver de acordo com as condições definidas pelo seu negocio, ele vai abrir o whatsapp e enviar a mensagem que você definiu anteriormente. 
