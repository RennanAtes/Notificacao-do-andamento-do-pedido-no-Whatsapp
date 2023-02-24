import webbrowser
import keyboard
import time
def EnviarMensagem(num,situtransporte,nome,Pagamento,produto,ValorDoProduto,Transportadora,urlrastreio):

    print ("Está no EnviarMensagem")
    num = str(num)
    num = ("+"+num)
    #print (num)
    ver = False
    msgdatransp = False
    quebrarlinha = "%0A"


    print (nome,Transportadora, Pagamento, situtransporte)
    if Pagamento:
        Pagamento = Pagamento.lower()
    if situtransporte:
        situtransporte = situtransporte.lower()


    if situtransporte == "novo":
        msg = f"Olá, *{nome}*!{quebrarlinha}{quebrarlinha}Obrigado por comprar com a gente, recebemos o pedido do produto *{produto}* no valor de R${ValorDoProduto} e agora estamos aguardando a confirmação do pagamento.{quebrarlinha}{quebrarlinha}Até breve😉{quebrarlinha}"
        ver = True
    elif situtransporte == "aprovado":
        msg = f"Olá, *{nome}*!{quebrarlinha}{quebrarlinha}O pagamento do produto *{produto}* acabou de ser aprovado.✅{quebrarlinha}{quebrarlinha}O pedido vai ser preparado para envio, assim que tiver novidades eu volto aqui para te avisar!{quebrarlinha}{quebrarlinha}Até breve😉"
        ver = True
    if Transportadora == "Correios Sedex":
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'Favorita':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'FCBLOG':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'Moovlog Sem cubagem':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'TransLaguna':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'Ux Delivery':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == '4A Logística':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == '4A Logistica Express':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == '4A Logística Express':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'Brasil Web':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'BRASIL WEB TRANSPORTES E LOGISTICA LTDA.':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'Direcional':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'DominaLog':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'DOMINALOG EXPRESS LOGISTICA INTEGRADA LTDA':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'FL Brasil':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'Log+':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'Magalu Entregas':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'Mindlog Transportes':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'Moovlog':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'Pajuçara Transportes':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'Reunidas':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'SC Logística Inteligente':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    elif Transportadora == 'STL Express':
        msgdatransportadora = f"Você pode rastrear o pedido sempre que quiser. Acesse: 👇 {urlrastreio}"
        msgdatransp = True
    if msgdatransp:
        if situtransporte == 'em viagem':
            msg = f"Olá, *{nome}*!{quebrarlinha}{quebrarlinha}Temos uma ótima notícia!{quebrarlinha}{quebrarlinha}O seu produto *{produto}* no valor de R${ValorDoProduto} já esta em viagem!🚚{quebrarlinha}{quebrarlinha}Você pode acompanhar o pedido sempre que quiser. É só clicar aqui: {msgdatransportadora} {quebrarlinha}{quebrarlinha}Até breve😉{quebrarlinha}"
            ver = True
        elif situtransporte == "entregue":
            msg = f"Olá *{nome}*!{quebrarlinha}{quebrarlinha}Eu estava acompanhando a entrega do seu produto *{produto}*, e verificamos que ele já foi entregue!🚀{quebrarlinha}{quebrarlinha}Espero que a sua experiência com a nossa loja tenha sido incrível!{quebrarlinha}{quebrarlinha}Até breve😉{quebrarlinha}"
            ver = True
        elif situtransporte == "coletando":
            msg = f"Olá *{nome}*!{quebrarlinha}{quebrarlinha}Estava olhando o seu pedido, e vim avisar que o seu produto *{produto}* já foi coletado!🚚{quebrarlinha}{quebrarlinha}Você pode acompanhar o pedido sempre que quiser. É só clicar aqui: {msgdatransportadora} {quebrarlinha}{quebrarlinha} Até breve😉{quebrarlinha}"
            ver = True
        elif situtransporte == "faturando":
            msg = f"Olá *{nome}*!{quebrarlinha}{quebrarlinha}Estava olhando o seu pedido, e vim avisar que o seu produto *{produto}* está faturando!🚚{quebrarlinha}{quebrarlinha}Você pode acompanhar o pedido sempre que quiser. É só clicar aqui: {msgdatransportadora} {quebrarlinha}{quebrarlinha}Até breve😉{quebrarlinha}"
            ver = True
    if ver:
        webbrowser.open_new(f"https://web.whatsapp.com/send?phone={num}&text={msg}")
        time.sleep(7)
        keyboard.press("Enter")
        time.sleep(2)
        keyboard.press_and_release("ctrl+w")
    else:
        print("")

