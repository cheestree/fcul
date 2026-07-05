# Perguntas de Estudo - Segurança em Sistemas Distribuídos

---

## 1. Certificados e TLS 1.3

### Q1.
Um X.509 v3 apresenta assinatura válida, período de validade correto e cadeia até uma CA de confiança. O campo Subject Alternative Name não corresponde ao domínio acedido. O cliente TLS deve:

* A. Aceitar, porque a cadeia de certificação está válida e é suficiente.
* B. Aceitar, porque o período de validade está dentro do prazo.
* C. Rejeitar; a correspondência de nome é uma verificação obrigatória e independente da validade da assinatura.
* D. Renegociar automaticamente e pedir um certificado diferente ao servidor.
* E. Nenhuma das outras opções.

### Q2.
Qual campo do certificado X.509 protege diretamente a integridade de todos os outros campos do certificado?

* A. O número de série, porque é único e gerado pela CA.
* B. O campo extensions, porque implementa mecanismos genéricos de verificação.
* C. O subject name, porque identifica univocamente o titular.
* D. A assinatura digital, feita com a chave privada da CA, que cobre todos os campos.
* E. Nenhuma das outras opções.

### Q3.
Qual afirmação compara corretamente CRL e OCSP?

* A. OCSP envia periodicamente a lista completa de revogações; CRL responde a pedidos individuais em tempo real.
* B. CRL é uma lista de certificados revogados publicada pela CA; OCSP permite consulta pontual do estado de um certificado num servidor online.
* C. Ambos verificam se o servidor possui a chave privada, substituindo o CertificateVerify no TLS 1.3.
* D. CRL é consultada em tempo real antes de cada ligação; OCSP é descarregado periodicamente em lote.
* E. Nenhuma das outras opções.

### Q4.
No TLS 1.3, após o ServerHello, que informação permite a ambos os lados começar a derivar as chaves de handshake sem mais mensagens em claro?

* A. O client_random e server_random enviados em claro no hello, porque são usados diretamente como chave.
* B. O segredo partilhado obtido do ECDHE (e/ou PSK), combinado com o transcript via HKDF.
* C. O certificado do servidor, porque contém a chave pública de cifragem de sessão.
* D. O Finished, porque é a primeira mensagem que confirma o acordo de chaves.
* E. Nenhuma das outras opções.

### Q5.
Porque é que os dados enviados em 0-RTT no TLS 1.3 não têm forward secrecy e são vulneráveis a replay?

* A. Porque o servidor não possui certificado válido no momento de receber early data.
* B. Porque 0-RTT usa a chave de sessão anterior (derivada do PSK sem novo ECDHE) e o servidor não gerou nenhum valor fresco antes de receber os dados.
* C. Porque o Finished do servidor não é enviado antes dos dados de aplicação.
* D. Porque o número de sequência recomeça a 0 em cada sessão 0-RTT.
* E. Nenhuma das outras opções.

### Q6.
Qual o papel do mecanismo de resumption com NewSessionTicket no TLS 1.3?

* A. Permite ao servidor autenticar o cliente sem certificado em sessões futuras, eliminando a necessidade de PSK.
* B. O servidor envia um ticket que encapsula um PSK derivado da sessão; o cliente pode usá-lo em handshakes futuros para resumir sem um novo full handshake, podendo opcionalmente adicionar ECDHE para PFS.
* C. Substitui completamente o CertificateVerify em sessões subsequentes para aumentar eficiência.
* D. Garante que a sessão retomada usa exatamente as mesmas chaves de tráfego da sessão anterior.
* E. Nenhuma das outras opções.

---

## 2. IPsec e IKEv2

### Q7.
Um administrador quer que todo o tráfego TCP na porta 443 entre dois hosts seja cifrado com ESP, mas que o ICMP entre os mesmos hosts passe sem proteção. Que base de dados e que entidade devem ser configuradas para implementar esta política?

* A. A SAD, adicionando duas SAs: uma para TCP/443 e outra para ICMP com algoritmo nulo.
* B. A SPD, com duas entradas: uma ação PROTECT para TCP/443 e uma ação BYPASS para ICMP.
* C. A SPD para PROTECT e a SAD para BYPASS, respetivamente.
* D. Apenas o IKE, que determina automaticamente a política com base no tráfego observado.
* E. Nenhuma das outras opções.

### Q8.
Em que modo IPsec o cabeçalho IP original fica protegido dentro do payload ESP, e quem é o destinatário do cabeçalho IP exterior?

* A. Modo transporte; o destino é o host final.
* B. Modo túnel; o destino do cabeçalho exterior é o gateway IPsec.
* C. Modo transporte com AH; o destino é o gateway IPsec.
* D. Ambos os modos protegem igualmente o cabeçalho IP original.
* E. Nenhuma das outras opções.

### Q9.
Qual é a diferença fundamental entre AH e ESP em termos de cobertura de proteção?

* A. AH cifra o payload e autentica o cabeçalho IP; ESP apenas cifra sem autenticar.
* B. AH autentica o payload e campos IP imutáveis, mas não oferece confidencialidade; ESP pode oferecer confidencialidade e autenticação, mas não cobre o cabeçalho IP exterior.
* C. ESP autentica o cabeçalho IP exterior completo; AH não autentica nada fora do payload.
* D. AH e ESP são equivalentes no modo túnel; só diferem no modo transporte.
* E. Nenhuma das outras opções.

### Q10.
No IKEv2, qual é a função dos Cookies enviados pelo responder durante o IKE_SA_INIT, e o que eles não fazem?

* A. Autenticam definitivamente o iniciador antes da troca DH, substituindo o IKE_AUTH.
* B. Protegem o responder contra ataques DoS ao forçar o iniciador a provar que o seu endereço IP é real, sem alocar estado no responder; não autenticam identidades.
* C. Cifram os parâmetros DH da troca inicial para impedir eavesdropping.
* D. Substituem os nonces da troca DH, fornecendo frescura à SA criada.
* E. Nenhuma das outras opções.

### Q11.
Dois gateways têm uma IKE_SA ativa. O administrador decide criar manualmente uma nova Child SA com CREATE_CHILD_SA, incluindo uma troca DH efémera. Após apagar os segredos efémeros, esta nova Child SA tem PFS em relação a quê?

* A. Em relação à IKE_SA, porque esta protegeu o canal durante o CREATE_CHILD_SA.
* B. Em relação ao compromisso da IKE_SA ou das Child SAs anteriores: comprometer material de chave antigo não compromete as chaves desta nova Child SA.
* C. Não tem PFS porque as chaves são sempre derivadas do mesmo segredo DH inicial.
* D. Tem PFS apenas se usar AH em vez de ESP.
* E. Nenhuma das outras opções.

---

## 3. Segurança WiFi / IEEE 802.11

### Q12.
Numa rede WPA2-Enterprise, quem é responsável por autenticar o cliente e de que forma é essa autenticação tipicamente realizada?

* A. O AP autentica o cliente verificando a password diretamente na sua base de dados local.
* B. Um servidor RADIUS autentica o cliente via protocolo EAP (por exemplo, EAP-TLS com certificados), e entrega a PMK ao AP após sucesso.
* C. O cliente autentica-se apresentando a GTK correta durante o 4-way handshake.
* D. A autenticação é feita apenas com endereço MAC, sem criptografia adicional.
* E. Nenhuma das outras opções.

### Q13.
Numa rede WPA2-Personal, dois dispositivos com a mesma PSK associam-se ao mesmo AP. As suas PTKs são diferentes porque:

* A. O AP gera uma PMK diferente para cada cliente com base no endereço MAC.
* B. A derivação da PTK inclui, além da PMK, os nonces ANonce e SNonce (gerados aleatoriamente por sessão) e os endereços MAC, tornando cada PTK única e ligada ao par AP-cliente.
* C. A PTK é escolhida pelo servidor RADIUS e distribuída individualmente.
* D. A GTK substitui a PTK para cada novo cliente, garantindo unicidade.
* E. Nenhuma das outras opções.

### Q14.
O que é o 4-way handshake no WPA2/802.11i e qual o seu propósito principal?

* A. Estabelecer a PMK entre o cliente e o servidor RADIUS.
* B. Confirmar que ambos os lados possuem a mesma PMK (sem a revelar), derivar a PTK, e distribuir a GTK ao cliente de forma protegida.
* C. Negociar o algoritmo de cifragem (CCMP ou TKIP) entre o cliente e o AP.
* D. Autenticar o AP perante o servidor RADIUS antes de aceitar clientes.
* E. Nenhuma das outras opções.

### Q15.
Em CCMP (AES-CCM), o nonce usado por cada frame é construído a partir do Packet Number (PN) e do endereço MAC. O que acontece se o PN for reiniciado para a mesma chave?

* A. O AP descarta silenciosamente os frames com PN repetido, sem efeito na segurança.
* B. A proteção de integridade é reforçada porque o mesmo nonce em frames diferentes cria redundância verificável.
* C. A reutilização de nonce em AES-CTR (componente do CCM) pode comprometer completamente a confidencialidade, revelando o XOR dos dois plaintexts.
* D. Apenas a proteção anti-replay falha; a confidencialidade mantém-se.
* E. Nenhuma das outras opções.

### Q16.
O SAE (Dragonfly) no WPA3-Personal utiliza um protocolo PAKE. Qual propriedade fundamental o distingue do PSK simples do WPA2?

* A. O SAE envia a palavra-passe cifrada com a chave pública do AP, protegendo-a de eavesdropping.
* B. O SAE é um protocolo de acordo de chave autenticado que não produz verificadores passivos reutilizáveis, impedindo ataques de dicionário offline sobre capturas da troca de autenticação.
* C. O SAE elimina por completo a necessidade de palavra-passe, usando apenas certificados.
* D. O SAE garante que a palavra-passe nunca é derivada em chave de sessão, evitando reutilização.
* E. Nenhuma das outras opções.

---

## 4. Segurança de Email

### Q17.
Um email tem `From: cfo@empresa.pt`. SPF passa para o domínio `newsletter.empresa.pt` (domínio do MAIL FROM). DKIM passa com `d=newsletter.empresa.pt`. O domínio visível em From é `empresa.pt`. Qual o resultado DMARC?

* A. DMARC passa porque SPF passou para um subdomínio de empresa.pt.
* B. DMARC passa porque DKIM passou para um subdomínio de empresa.pt.
* C. DMARC falha: nem SPF nem DKIM estão alinhados com o domínio organizacional `empresa.pt` (dependendo da política de alinhamento relaxed/strict).
* D. DMARC ignora DKIM quando SPF passou.
* E. Nenhuma das outras opções.

### Q18.
S/MIME usa criptografia ao nível do MUA. Qual das seguintes afirmações sobre S/MIME é correta?

* A. S/MIME cifra os metadados SMTP (endereços From e To) além do corpo.
* B. Uma mensagem S/MIME cifrada com a chave pública do destinatário garante confidencialidade ponta-a-ponta, mas não prova a identidade do remetente por si só.
* C. S/MIME e PGP são interoperáveis porque ambos usam o mesmo formato de certificado.
* D. S/MIME autentica o servidor SMTP mas não o utilizador remetente.
* E. Nenhuma das outras opções.

### Q19.
Qual é a diferença entre o `From` SMTP (envelope) e o `From` do cabeçalho da mensagem, e porque é relevante para segurança?

* A. São sempre idênticos; a distinção é apenas terminológica.
* B. O `From` do envelope (`MAIL FROM`) é usado pelo SPF e indica o caminho de retorno; o `From` do cabeçalho é o que o utilizador vê. Um atacante pode preencher os dois com valores diferentes, criando spoofing visível.
* C. O `From` do cabeçalho é verificado pelo SPF; o do envelope é verificado pelo DKIM.
* D. O `From` do envelope é visível ao utilizador; o do cabeçalho é apenas interno ao MTA.
* E. Nenhuma das outras opções.

### Q20.
Um utilizador quer que as suas mensagens sejam verificáveis como suas apenas pelo destinatário, sem possibilidade de o destinatário provar a terceiros que foi o utilizador a enviá-las. Qual mecanismo satisfaz este requisito?

* A. Assinatura digital com chave privada RSA, porque apenas o utilizador pode gerar a assinatura.
* B. DKIM, porque a assinatura é feita pelo domínio do utilizador e verificável publicamente.
* C. Um MAC com chave simétrica partilhada entre remetente e destinatário: ambos podem gerar e verificar, mas nenhum pode provar a terceiros qual dos dois o criou.
* D. Cifrar com a chave pública do destinatário, porque só ele pode decifrar e verificar a origem.
* E. Nenhuma das outras opções.

### Q21.
O ARC (Authenticated Received Chain) foi desenvolvido para resolver que problema específico com DKIM?

* A. O DKIM não cobre o cabeçalho `Subject`, tornando-o vulnerável a modificação.
* B. Quando um intermediário (como uma mailing list) modifica a mensagem, a assinatura DKIM original quebra; ARC preserva o resultado de autenticação original em cada salto, permitindo que o recetor final avalie a cadeia de confiança.
* C. O DKIM não protege contra ataques de replay; ARC adiciona nonces por salto.
* D. ARC substitui DMARC em domínios que não publicam registos SPF.
* E. Nenhuma das outras opções.

---

## 5. Bluetooth

### Q22.
Qual afirmação sobre a organização de rede Bluetooth BR/EDR está correta?

* A. Um master pode ter até 255 dispositivos ativos simultaneamente no mesmo piconet.
* B. Um piconet tem no máximo 8 dispositivos ativos (1 master + 7 slaves); dispositivos adicionais ficam em estado parked.
* C. Num scatternet, um dispositivo não pode ser simultaneamente master num piconet e slave noutro.
* D. O scatternet aumenta o número de slaves ativos num único piconet.
* E. Nenhuma das outras opções.

### Q23.
No Secure Simple Pairing (SSP), qual modo de associação NÃO protege contra ataques MITM ativos?

* A. Numeric Comparison.
* B. Passkey Entry.
* C. Just Works.
* D. Out of Band (OOB) com canal resistente a MITM.
* E. Nenhuma das outras opções.

### Q24.
No SSP com Numeric Comparison, o valor de 6 dígitos exibido em ambos os dispositivos serve para:

* A. Ser introduzido pelo utilizador como PIN de autenticação no dispositivo sem ecrã.
* B. Derivar a link key final, substituindo o segredo DH.
* C. Permitir ao utilizador confirmar que ambos os lados calcularam o mesmo segredo DH, tornando a probabilidade de MITM não detetado de 1 em 1 000 000.
* D. Cifrar os nonces trocados durante a autenticação Stage 1.
* E. Nenhuma das outras opções.

### Q25.
Qual é a principal vulnerabilidade de segurança das unit keys em Bluetooth, quando comparadas com combination keys?

* A. As unit keys são muito curtas (32 bits) para resistir a ataques de força bruta modernos.
* B. Como a unit key é gerada por um único dispositivo e reutilizada com todos os pares, qualquer dispositivo que a obtenha pode escutar todas as comunicações desse dispositivo e impersoná-lo.
* C. As unit keys não suportam o protocolo de autenticação E1, ficando sem proteção de integridade.
* D. As unit keys expiram após cada sessão, obrigando a uma re-inicialização custosa.
* E. Nenhuma das outras opções.

### Q26.
O protocolo de autenticação legado de Bluetooth (anterior à v4.1) fornece autenticação mútua?

* A. Sim; ambos os dispositivos verificam o SRES simultaneamente usando a mesma link key.
* B. Não; apenas o verifier autentica o claimant. Para mutualidade seria necessário executar o protocolo duas vezes com papéis trocados.
* C. Sim; o AU_RAND é enviado em ambas as direções e funciona como prova mútua.
* D. Não, porque o protocolo legado usa apenas hashing sem chave (sem MAC).
* E. Nenhuma das outras opções.

### Q27.
Porque é o LE Legacy Pairing (versões 4.0 e 4.1) considerado inseguro?

* A. Não usa qualquer função criptográfica; os dados são trocados em claro.
* B. Os métodos Just Works e Passkey Entry derivam a Temporary Key (TK) de forma vulnerável a eavesdropping (TK = 0 em Just Works), e a LTK é distribuída por key transport em vez de key agreement.
* C. Usa RSA-512, considerado insuficiente para dispositivos pós-2010.
* D. A fase de autenticação é omitida para reduzir o consumo de energia.
* E. Nenhuma das outras opções.

### Q28.
No LE Secure Connections (v4.2), o que muda fundamentalmente em relação ao LE Legacy Pairing?

* A. A LTK é gerada apenas pelo initiator e distribuída ao responder.
* B. O ECDH (P-256) é usado para um key agreement genuíno, e os 4 modos de associação do SSP (Numeric Comparison, Just Works, OOB, Passkey) são aplicados para resistência a MITM.
* C. O protocolo elimina a fase de pairing, usando apenas chaves pré-partilhadas de fábrica.
* D. A LTK é derivada diretamente do endereço MAC, sem troca de valores DH.
* E. Nenhuma das outras opções.

### Q29.
Em Bluetooth, a negociação do tamanho da chave de cifragem pode ser reduzida durante o setup. Qual o risco e a mitigação correta?

* A. Não há risco; chaves menores apenas reduzem desempenho.
* B. Um atacante pode forçar um downgrade para chaves mínimas (1 byte), tornando a cifragem trivialmente quebrada; a mitigação é definir um parâmetro de "minimum key size" nos dispositivos.
* C. A chave de cifragem nunca pode ser inferior a 64 bits, por especificação do protocolo.
* D. O risco é apenas teórico porque o downgrade requer acesso físico ao dispositivo.
* E. Nenhuma das outras opções.

---

## 6. RFID

### Q30.
Qual é a diferença fundamental entre tags RFID passivas e ativas em termos de fonte de energia e distância de leitura?

* A. Tags passivas têm bateria e transmitem ativamente; tags ativas dependem do campo eletromagnético do leitor.
* B. Tags passivas obtêm energia por indução do campo do leitor (Near Field), operando a curta distância; tags ativas têm bateria própria e podem comunicar a maior distância.
* C. Tags passivas usam frequências UHF exclusivamente; tags ativas usam LF ou HF.
* D. Ambas funcionam de forma idêntica, diferindo apenas no tamanho físico.
* E. Nenhuma das outras opções.

### Q31.
No Basic Access Control (BAC) dos e-passaportes, qual é a função da chave derivada por OCR da página do passaporte?

* A. Cifrar o número de série biométrico antes de o enviar ao leitor.
* B. Garantir que apenas um leitor com acesso visual ao passaporte aberto pode iniciar a comunicação RFID protegida, limitando leituras remotas não autorizadas.
* C. Substituir a necessidade de autenticação mútua entre chip e leitor.
* D. Permitir ao chip do passaporte verificar a identidade do país do leitor.
* E. Nenhuma das outras opções.

### Q32.
A BAC key pode ser vulnerável a ataques de força bruta porque:

* A. O algoritmo Triple-DES usado é considerado inseguro para este contexto.
* B. A chave é frequentemente derivada do número do passaporte, data de nascimento e data de validade — valores com entropia limitada e parcialmente previsíveis ou observáveis.
* C. O protocolo BAC não usa nonces, permitindo ataques de replay que reduzem o espaço de pesquisa.
* D. A chave é transmitida em claro na fase inicial do protocolo.
* E. Nenhuma das outras opções.

### Q33.
A Passive Authentication (PA) do e-passaporte detecta que ameaça, e qual a sua limitação principal?

* A. Detecta leitura remota não autorizada; limitação: não funciona sem ligação à internet.
* B. Detecta alterações dos dados do chip após emissão (via assinatura da CA do país); limitação: não impede clonagem, porque os dados e a assinatura podem ser copiados para outro chip.
* C. Detecta leitores não autorizados; limitação: requer que o leitor apresente um certificado atualizado.
* D. Detecta passaportes expirados; limitação: não verifica dados biométricos.
* E. Nenhuma das outras opções.

### Q34.
No ataque de relay ao controlo de acesso físico com RFID, por que é que um protocolo de challenge-response criptográfico não é suficiente para o prevenir?

* A. Porque os algoritmos criptográficos usados nos cartões são demasiado fracos.
* B. Porque um atacante com um cúmplice pode retransmitir os desafios e respostas em tempo real entre o leitor e o cartão legítimo, sem quebrar a criptografia — o cartão responde corretamente sem estar fisicamente presente.
* C. Porque o leitor não autentica a sua identidade perante o cartão.
* D. Porque os protocolos RFID enviam o ID em claro antes do challenge-response.
* E. Nenhuma das outras opções.

### Q35.
No protocolo zero-knowledge de autenticação RFID descrito nos slides, qual o papel do DT (nonce crescente) e porque é essencial?

* A. É usado para cifrar o SSDK durante o transporte, impedindo que o leitor o descubra.
* B. Funciona como proteção anti-replay: o tag só aceita pedidos em que DT > DT_last, impedindo a reutilização de pedidos interceptados anteriormente.
* C. É o identificador público do tag, enviado em claro para o leitor localizar o SSDK correto na sua base de dados.
* D. Garante que o RSK é único por sessão, mesmo que o SSDK seja comprometido.
* E. Nenhuma das outras opções.

### Q36.
No caso do SpeedPass (ExxonMobil), qual foi a falha de segurança fundamental que permitiu o ataque descrito nos slides?

* A. A chave de 40 bits e o algoritmo de cifragem proprietário (não público) foram suficientemente pequenos para serem quebrados por força bruta com hardware paralelo, após reversão do algoritmo.
* B. A comunicação entre o tag e o leitor não usava qualquer forma de cifragem.
* C. O ID de 24 bits era o mesmo para todos os tags de um lote, permitindo impersonação trivial.
* D. O protocolo não usava nonces, mas como o algoritmo era seguro isso não era explorado.
* E. Nenhuma das outras opções.

---

## 7. Pagamentos Eletrónicos

### Q37.
O EMV divide a autenticação em três fases. Qual é o objetivo da fase de Card Authentication?

* A. Verificar que o utilizador conhece o PIN correto associado ao cartão.
* B. Confirmar que os dados do cartão não foram alterados desde a emissão, verificando assinaturas criptográficas do emissor via CA.
* C. Autorizar a transação junto do banco emissor e obter o ARPC.
* D. Negociar os algoritmos criptográficos suportados entre cartão e terminal.
* E. Nenhuma das outras opções.

### Q38.
Qual a principal vulnerabilidade do Static Data Authentication (SDA) no EMV?

* A. Usa criptografia simétrica, que é mais fácil de quebrar do que assimétrica.
* B. Como apenas verifica dados estáticos assinados pelo emissor, esses dados podem ser copiados para outro cartão ("Yes Card"), que os apresenta como se fossem genuínos.
* C. O terminal não valida a cadeia de certificados até à CA, aceitando qualquer assinatura.
* D. A SAD inclui o PIN em claro, expondo-o se o cartão for fisicamente lido.
* E. Nenhuma das outras opções.

### Q39.
O Dynamic Data Authentication (DDA) resolve a principal fraqueza do SDA de que forma?

* A. Usando cifragem simétrica em vez de assimétrica, tornando a verificação mais rápida.
* B. Exigindo que o cartão assine um nonce gerado pelo terminal com a sua chave privada, provando a presença do cartão físico e impedindo a cópia estática de dados.
* C. Enviando a SAD cifrada com a chave do terminal em vez de assinada pelo emissor.
* D. Eliminando a necessidade de CA, verificando diretamente com o banco emissor online.
* E. Nenhuma das outras opções.

### Q40.
No ataque Pre-Play ao EMV, qual é a falha fundamental explorada?

* A. A chave simétrica entre o cartão e o emissor é extraída por análise de potência (SPA/DPA).
* B. O Unpredictable Number (UN) gerado pelo terminal é previsível ou manipulável, permitindo obter antecipadamente um ARQC válido para um UN futuro e reutilizá-lo numa transação fraudulenta.
* C. O PIN é enviado em claro entre terminal e banco emissor.
* D. O algoritmo AES no cartão é vulnerável a colisões de hash na geração do ARQC.
* E. Nenhuma das outras opções.

### Q41.
No E-Cash (DigiCash), qual é o objetivo da blind signature durante o levantamento de uma moeda?

* A. Permitir ao banco assinar eficientemente sem gastar recursos computacionais.
* B. Permitir ao cliente obter uma moeda validamente assinada pelo banco sem que o banco conheça o número de série específico que assinou, garantindo anonimato mesmo em caso de conluio banco-vendedor.
* C. Garantir que o vendedor não pode reutilizar a moeda depois de a receber.
* D. Proteger o canal de comunicação cliente-banco contra eavesdropping.
* E. Nenhuma das outras opções.

### Q42.
No E-Cash, como é prevenido o double-spending?

* A. Cada moeda inclui a identidade cifrada do cliente, permitindo rastreio em caso de reutilização.
* B. O banco mantém uma base de dados dos números de série das moedas já gastas; ao depositar, o vendedor apresenta a moeda e o banco rejeita serial# já vistos.
* C. As moedas têm validade de 24 horas, após a qual expiram automaticamente.
* D. O cliente assina cada transação com a sua chave privada, ligando cada pagamento à sua identidade.
* E. Nenhuma das outras opções.

### Q43.
No E-Cash, porque é que o cliente não deve receber troco num pagamento?

* A. O protocolo não suporta tecnicamente a transferência de múltiplas moedas.
* B. O banco, ao emitir moedas de troco, associa-as a esse depósito específico; cruzando com a informação do vendedor, pode ligar o cliente ao pagamento, comprometendo o anonimato.
* C. As moedas de troco teriam de ser emitidas pelo vendedor, que não tem autorização do banco.
* D. O troco exigiria uma ligação adicional online ao banco, comprometendo a disponibilidade.
* E. Nenhuma das outras opções.

### Q44.
Na Bitcoin, qual o papel da proof-of-work na integridade da blockchain?

* A. Autentica criptograficamente a identidade dos mineiros perante os outros nós.
* B. Garante que criar um bloco exige trabalho computacional significativo, tornando a alteração de blocos passados impraticável (exigiria refazer todo o trabalho subsequente), e permite que a cadeia mais longa represente o consenso dos nós honestos.
* C. Cifra as transações dentro de cada bloco para garantir privacidade dos pagamentos.
* D. Gera os pares de chaves usados nas transações de cada utilizador.
* E. Nenhuma das outras opções.

### Q45.
Na Bitcoin, o anonimato é baseado em que mecanismo, e qual a sua limitação?

* A. As transações são cifradas com a chave pública do destinatário; limitação: o emissor é sempre identificável.
* B. Os endereços são hashes de chaves públicas sem ligação nominal; limitação: todas as transações são públicas na blockchain, permitindo análise de grafos para associar endereços a identidades, especialmente em transações com múltiplos inputs.
* C. Os valores das transações são ocultados por commitments criptográficos; limitação: os endereços de entrada são sempre visíveis.
* D. Cada transação usa uma chave simétrica efémera; limitação: a chave pode ser recuperada por análise de timing.
* E. Nenhuma das outras opções.
