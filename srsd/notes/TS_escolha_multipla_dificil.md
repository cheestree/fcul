# Tecnologias de Segurança - Compilado Difícil de Escolha Múltipla

Este conjunto cobre toda a matéria técnica dos slides. Cada pergunta tem uma única melhor resposta e inclui sempre a opção **E. Nenhuma das outras opções.**

O gabarito comentado encontra-se no fim. Para simular exame, responder primeiro sem o consultar.

## 1. Criptografia simétrica

### 1.

Um sistema cifra cada bloco primeiro com uma chave DES de 56 bits e depois com outra chave DES independente de 56 bits. Qual é a avaliação mais correta?

- A. A segurança passa necessariamente para 112 bits, porque o atacante tem de experimentar simultaneamente todos os pares de chaves.
- B. Um ataque meet-in-the-middle pode comparar valores intermédios, reduzindo muito o ganho face à estimativa ingénua de 112 bits.
- C. O esquema fica mais fraco do que DES simples, porque duas permutações sucessivas se anulam.
- D. O ataque só é possível se as duas chaves forem iguais.
- E. Nenhuma das outras opções.

### 2.

Em CBC, um atacante altera um único bit do bloco de cifra `C_i`, sem que exista autenticação. O que se espera após a decifragem?

- A. Apenas o mesmo bit de `P_i` é invertido; os restantes blocos não mudam.
- B. `P_i` permanece correto e `P_(i+1)` fica totalmente aleatório.
- C. `P_i` fica corrompido de forma imprevisível e o bit correspondente de `P_(i+1)` é invertido.
- D. Todos os blocos desde `P_i` até ao fim ficam necessariamente aleatórios.
- E. Nenhuma das outras opções.

### 3.

Duas mensagens são cifradas em CTR com a mesma chave e o mesmo nonce/contador inicial. O atacante conhece integralmente a primeira mensagem. Qual é a consequência mais direta?

- A. Só consegue verificar se as duas mensagens têm o mesmo comprimento.
- B. Recupera a chave AES, independentemente do número de rondas.
- C. Consegue alterar bits, mas não obtém informação sobre a segunda mensagem.
- D. Recupera o keystream usado e, na parte sobreposta, a segunda mensagem.
- E. Nenhuma das outras opções.

### 4.

Sobre XTS-AES aplicado a armazenamento, qual das afirmações A-D é correta?

- A. Fornece autenticação forte de cada setor e rejeita qualquer modificação maliciosa.
- B. Usa o mesmo resultado criptográfico para blocos de texto igual em posições diferentes, para facilitar deduplicação.
- C. Elimina a necessidade de chaves secretas, porque o tweak pode ser público.
- D. Foi concebido principalmente para proteger tráfego de rede com pacotes fora de ordem.
- E. Nenhuma das outras opções.

### 5.

Porque é que um LFSR isolado, apesar de poder ter período longo, não é normalmente adequado como gerador de keystream criptográfico?

- A. A sua estrutura linear permite reconstruir o estado a partir de saída suficiente; são necessárias construções não lineares ou cifras modernas.
- B. Não consegue produzir bits zero.
- C. Exige uma chave pública para inicializar o registo.
- D. Propaga um erro de transmissão por toda a mensagem.
- E. Nenhuma das outras opções.

## 2. Criptografia assimétrica, hashes, MAC e AEAD

### 6.

Para um hash ideal de 256 bits, qual é a ordem de grandeza genérica esperada para encontrar, respetivamente, uma colisão e uma preimagem?

- A. `2^256` e `2^128`.
- B. `2^128` e `2^256`.
- C. `2^128` e `2^128`.
- D. `2^256` e `2^256`, porque ambas exigem força bruta completa.
- E. Nenhuma das outras opções.

### 7.

Um protocolo cifra diretamente uma escolha pertencente a um conjunto de apenas dez mensagens possíveis usando RSA sem padding aleatório. Que problema é mais relevante?

- A. A determinismo permite cifrar as dez hipóteses com a chave pública e comparar; padding aleatório adequado combate este teste.
- B. A chave pública deixa de poder ser divulgada.
- C. O módulo `n` é automaticamente fatorizado ao observar dez cifras.
- D. A única correção é substituir RSA por um hash sem chave.
- E. Nenhuma das outras opções.

### 8.

Alice e Bob partilham uma chave e usam um MAC para autenticar contratos. Bob tenta depois provar a um juiz que Alice criou um contrato específico. Qual é a limitação essencial?

- A. Um MAC não deteta alterações ao contrato.
- B. Um MAC só funciona sobre mensagens cifradas.
- C. O juiz consegue verificar o MAC com a chave pública de Alice.
- D. Como Bob também conhece a chave, poderia ter criado o MAC; o mecanismo não dá não repúdio perante terceiros.
- E. Nenhuma das outras opções.

### 9.

Qual descrição de CCM é correta?

- A. Usa CBC para confidencialidade e RSA para integridade.
- B. Usa apenas CTR; o contador fornece também autenticação por si só.
- C. Combina AES-CTR para confidencialidade com CBC-MAC para integridade/autenticação.
- D. Cifra os dados associados para os esconder, mas deixa o texto principal em claro.
- E. Nenhuma das outras opções.

### 10.

Alice e Bob executam ECDH efémero, assinam o transcript completo com chaves de longo prazo autenticadas e apagam os escalares efémeros. Qual das afirmações A-D é correta?

- A. A assinatura elimina a Perfect Forward Secrecy, pois usa uma chave de longo prazo.
- B. O protocolo esconde necessariamente as identidades de um atacante passivo.
- C. O compromisso posterior das duas chaves de assinatura permite recalcular os segredos ECDH antigos.
- D. A autenticação do transcript é dispensável, porque ECDH já impede MITM.
- E. Nenhuma das outras opções.

## 3. Autenticação, distribuição de chaves e palavras-passe

### 11.

Um cliente envia `MAC_K(timestamp)` para se autenticar em vários servidores que partilham `K`. Qual é a melhoria conjunta mais importante contra replay e reutilização noutro servidor?

- A. Cifrar o timestamp com a mesma chave depois de calcular o MAC, sem guardar estado.
- B. Incluir a identidade do servidor no valor autenticado e manter uma cache de timestamps já aceites dentro da janela de tolerância.
- C. Aumentar a tolerância de relógio e aceitar repetidamente qualquer timestamp dentro dela.
- D. Substituir o timestamp por um identificador fixo do cliente.
- E. Nenhuma das outras opções.

### 12.

Num protocolo de autenticação mútua, ambos os lados respondem a desafios com a mesma chave e exatamente o mesmo formato. Um atacante inicia uma segunda sessão para fazer a vítima responder ao desafio da primeira. Qual é a defesa estrutural mais adequada?

- A. Tornar os desafios públicos antes do protocolo.
- B. Usar desafios mais curtos para reduzir a superfície de ataque.
- C. Separar papéis, formatos ou chaves por direção e autenticar as identidades no valor respondido.
- D. Cifrar toda a comunicação com ECB.
- E. Nenhuma das outras opções.

### 13.

O servidor envia um nonce aleatório e o cliente responde `H(password || nonce)`. Um atacante passivo grava a troca. Qual é a análise correta?

- A. O atacante pode testar palpites de palavra-passe offline, pois o nonce e a resposta permitem validar cada palpite.
- B. O nonce transforma automaticamente a palavra-passe numa chave de alta entropia.
- C. Só o servidor pode testar palavras-passe, porque foi ele que escolheu o nonce.
- D. O esquema oferece Perfect Forward Secrecy se o nonce nunca se repetir.
- E. Nenhuma das outras opções.

### 14.

Um servidor quer mitigar floods de pedidos que o obrigam a reservar memória e executar operações assimétricas caras. Qual é o uso mais correto de um cookie anti-DoS?

- A. Guardar no servidor todo o estado do cliente antes de enviar o cookie.
- B. Usar um cookie constante para que todos os clientes legítimos o possam reutilizar.
- C. Enviar primeiro o certificado completo e só depois verificar o cookie.
- D. Devolver um valor imprevisível e verificável sem estado, exigindo que o cliente o repita antes do trabalho caro.
- E. Nenhuma das outras opções.

### 15.

Num esquema Lamport, o servidor espera atualmente `H^(i-1)(p)`. Um atacante interceta esse valor enviado pelo cliente e bloqueia a ligação antes de o servidor o receber. Qual das afirmações A-D é correta?

- A. O valor intercetado já não serve, porque só pode ser verificado antes de ser transmitido.
- B. O atacante precisa de inverter imediatamente a função hash para o usar.
- C. O servidor avança automaticamente para `H^(i-2)(p)`, apesar de não ter recebido nada.
- D. O uso de salt impede esta forma de roubo de uma palavra-passe de utilização única em trânsito.
- E. Nenhuma das outras opções.

### 16.

Qual é a vantagem essencial de EKE face a executar DH anónimo e, depois, enviar uma prova naïve baseada na palavra-passe?

- A. EKE torna a palavra-passe pública, mas esconde os valores DH.
- B. EKE protege os valores DH com material derivado da palavra-passe, procurando impedir que uma captura forneça um verificador offline fiável para cada palpite.
- C. EKE dispensa qualquer segredo memorizado pelo utilizador.
- D. EKE garante segurança mesmo quando a palavra-passe tem entropia infinita, mas não quando é fraca.
- E. Nenhuma das outras opções.

### 17.

Um serviço acrescenta TOTP à palavra-passe. Qual é a conclusão de segurança mais rigorosa?

- A. TOTP impede qualquer phishing porque cada código só é válido uma vez.
- B. A segunda componente converte automaticamente o protocolo em autenticação mútua.
- C. TOTP melhora a resistência ao roubo isolado da palavra-passe, mas um adversário em tempo real pode encaminhar o código e sequestrar a sessão.
- D. Como usa HMAC, TOTP oferece não repúdio.
- E. Nenhuma das outras opções.

## 4. Kerberos V5

### 18.

Na resposta do AS, porque aparece `K_C,TGS` tanto dentro do TicketTGS como na parte cifrada para o cliente?

- A. O TGS precisa de obter a chave do ticket cifrado com `K_TGS`, enquanto o cliente precisa de a receber sob a sua chave de longo prazo; ambos ficam com a mesma chave de sessão.
- B. É uma redundância sem função de segurança, mantida apenas por compatibilidade.
- C. Permite ao cliente alterar livremente o conteúdo do ticket.
- D. Faz com que o AS deixe de conhecer a chave de sessão.
- E. Nenhuma das outras opções.

### 19.

Qual distingue corretamente o nonce do pedido AS do timestamp de um Authenticator Kerberos?

- A. Ambos são segredos de longo prazo e nunca atravessam a rede.
- B. O nonce substitui completamente a necessidade de relógios sincronizados em todo o Kerberos.
- C. O nonce liga a resposta do AS ao pedido; o timestamp do Authenticator demonstra uso fresco de um ticket/chave de sessão perante o serviço.
- D. O timestamp só define a validade do certificado X.509 do serviço.
- E. Nenhuma das outras opções.

### 20.

Um atacante obtém a chave de longo prazo de um único serviço Kerberos, mas não compromete `krbtgt`. Que capacidade está mais diretamente associada a um Silver Ticket?

- A. Forjar TGTs válidos para todos os serviços do realm.
- B. Forjar tickets para o serviço cuja chave foi comprometida, sem precisar da palavra-passe do utilizador.
- C. Recuperar automaticamente todas as chaves de utilizador do KDC.
- D. Renovar qualquer ticket indefinidamente, mesmo depois da expiração da chave do serviço.
- E. Nenhuma das outras opções.

### 21.

Qual combinação descreve melhor as flags de delegação e duração?

- A. Um ticket renewable pode ser usado em qualquer serviço, mesmo que não seja forwardable.
- B. Um ticket postdated é imediatamente válido e nunca precisa de validação pelo KDC.
- C. Um ticket proxiable entrega necessariamente ao serviço o TGT original do utilizador.
- D. Renewable prolonga uso dentro de limites mediante renovação; forwardable/proxiable controlam formas distintas de delegar direitos.
- E. Nenhuma das outras opções.

### 22.

Sobre a dependência de relógios em Kerberos V5, qual das afirmações A-D é correta?

- A. Só o AS usa tempo; TGS e serviços ignoram timestamps.
- B. A cifra simétrica sincroniza automaticamente os relógios dos intervenientes.
- C. A sincronização deixa de ser relevante assim que o cliente recebe um TGT.
- D. Aumentar sem limite a janela de aceitação preserva a mesma resistência a replay.
- E. Nenhuma das outras opções.

## 5. TLS 1.3 e certificados

### 23.

No handshake TLS 1.3 baseado em certificados, qual é a distinção mais correta entre `CertificateVerify` e `Finished`?

- A. `CertificateVerify` assina o transcript com a chave privada do certificado; `Finished` autentica o transcript com uma chave derivada do handshake e confirma posse das chaves.
- B. Ambos contêm a mesma assinatura RSA sobre o certificado da CA.
- C. `Finished` envia a chave de sessão em claro; `CertificateVerify` cifra-a.
- D. `CertificateVerify` protege apenas dados de aplicação, enquanto `Finished` substitui o Record Protocol.
- E. Nenhuma das outras opções.

### 24. - Rever

Qual afirmação compara corretamente modos PSK de TLS 1.3?

- A. PSK-only inclui sempre ECDHE implícito e oferece PFS fresca.
- B. PSK + ECDHE torna o `Finished` desnecessário.
- C. 0-RTT exige um novo ECDHE antes de o primeiro dado ser enviado e, por isso, não pode ser repetido.
- D. PSK + ECDHE pode acrescentar PFS; dados 0-RTT podem ser repetidos e não dependem de um novo segredo DH daquela ligação.
- E. Nenhuma das outras opções.

### 25.

Como é normalmente construído o nonce de um registo protegido em TLS 1.3?

- A. É escolhido livremente pela aplicação e enviado dentro do texto cifrado.
- B. Deriva da combinação do número de sequência com um IV estático; o contador reinicia quando as chaves mudam.
- C. É sempre igual ao `client_random` do handshake.
- D. É a assinatura do cabeçalho do registo.
- E. Nenhuma das outras opções.

### 26.

Qual das afirmações A-D sobre validação e revogação de certificados é correta?

- A. Uma assinatura de CA válida torna irrelevantes o nome do servidor e o período de validade.
- B. OCSP prova que o servidor possui a chave privada, substituindo `CertificateVerify`.
- C. Uma CRL contém obrigatoriamente todas as chaves privadas revogadas para permitir a sua deteção.
- D. Se a cadeia termina numa raiz confiável, o estado de revogação dos certificados intermédios nunca interessa.
- E. Nenhuma das outras opções.

### 27.

Porque é importante um encerramento autenticado como `close_notify`?

- A. Para renovar automaticamente o certificado do servidor.
- B. Para esconder o comprimento de todos os dados já enviados.
- C. Para distinguir um fim legítimo de uma ligação truncada por um atacante ou falha de rede.
- D. Para reutilizar números de sequência antigos na ligação seguinte.
- E. Nenhuma das outras opções.

## 6. IPsec e IKEv2

### 28.

Um túnel IPsec protege tráfego nos dois sentidos entre dois gateways. Quantas SAs IPsec são necessárias, no mínimo, para o tráfego bidirecional sob uma única política e porquê?

- A. Duas, porque cada SA é unidirecional.
- B. Uma, porque o SPI identifica simultaneamente ambos os sentidos.
- C. Três, uma para ESP, uma para AH e uma para IKE.
- D. Quatro, porque cada gateway precisa de uma SA de entrada e duas de saída.
- E. Nenhuma das outras opções.

### 29.

Qual é a relação correta entre SPD e SAD?

- A. A SAD decide se um pacote deve ser descartado, ignorado ou protegido antes de existir qualquer SA; a SPD só guarda chaves.
- B. A SPD associa seletores a ações/políticas; a SAD guarda parâmetros e estado das SAs ativas, como chaves, algoritmos e contadores.
- C. Ambas contêm apenas certificados e listas de revogação.
- D. A SPD é enviada em cada pacote ESP; a SAD é pública e distribuída por DNS.
- E. Nenhuma das outras opções.

### 30.

Qual afirmação sobre a cobertura de proteção em IPsec é correta?

- A. AH oferece confidencialidade do payload e ESP nunca pode autenticar.
- B. ESP em modo transporte cifra sempre o cabeçalho IP exterior completo.
- C. ESP em modo túnel deixa o pacote IP interior integralmente em claro.
- D. AH autentica payload e campos IP imutáveis/previsíveis; ESP pode dar confidencialidade e autenticação, mas o cabeçalho IP exterior não fica cifrado.
- E. Nenhuma das outras opções.

### 31.

Um pacote ESP chega com número de sequência ainda dentro da sliding window, nunca antes observado, mas com tag inválida. O recetor deve:

- A. Aceitá-lo, porque a janela anti-replay já provou frescura.
- B. Marcar o número como recebido e entregar o payload corrompido.
- C. Rejeitá-lo; estar na janela e não ser duplicado não substitui a verificação de autenticidade.
- D. Reiniciar a SA e reutilizar o contador a partir de zero.
- E. Nenhuma das outras opções.

### 32.

Sobre `IKE_SA_INIT` e `IKE_AUTH`, qual das afirmações A-D é correta?

- A. `IKE_SA_INIT` autentica definitivamente as identidades antes de trocar valores DH.
- B. `IKE_AUTH` ocorre em claro porque ainda não existem chaves derivadas.
- C. A primeira Child SA fica operacional antes de os pares se autenticarem.
- D. Cookies em `IKE_SA_INIT` substituem a autenticação por assinatura ou PSK.
- E. Nenhuma das outras opções.

### 33.

Ao criar uma nova Child SA com `CREATE_CHILD_SA`, quando é que esta pode obter PFS independente do segredo DH inicial?

- A. Quando a troca inclui um novo DH efémero e os respetivos segredos são apagados.
- B. Sempre, mesmo que apenas derive novas chaves do estado antigo sem novo DH.
- C. Apenas se usar AH em vez de ESP.
- D. Apenas se reutilizar o mesmo número de sequência da SA anterior.
- E. Nenhuma das outras opções.

## 7. Segurança de email

### 34.

Um email apresenta `From: ceo@empresa.pt`, mas foi entregue por um IP não autorizado para o domínio usado em `MAIL FROM`. O que SPF avalia diretamente?

- A. Se o corpo foi assinado pelo CEO.
- B. Se o domínio visível no cabeçalho `From` coincide com a identidade civil do remetente.
- C. Se o IP de ligação está autorizado pela política DNS do domínio do envelope.
- D. Se todos os saltos SMTP usaram TLS.
- E. Nenhuma das outras opções.

### 35. - Rever

Uma mailing list acrescenta um rodapé ao corpo e altera o assunto de uma mensagem com DKIM. Qual é a consequência mais provável?

- A. SPF passa automaticamente porque DKIM estava presente na mensagem original.
- B. A assinatura DKIM pode falhar se as partes alteradas estavam cobertas pela canonicalização/assinatura.
- C. O certificado S/MIME do destinatário é revogado.
- D. DMARC ignora sempre DKIM em mensagens de listas.
- E. Nenhuma das outras opções.

### 36.

O domínio visível em `From` é `empresa.pt`. SPF passa para `bounce.fornecedor.net` e DKIM passa com `d=empresa.pt`. Em termos gerais, que resultado pode satisfazer DMARC?

- A. O DKIM alinhado com `empresa.pt` pode satisfazer DMARC, mesmo que o domínio SPF que passou não esteja alinhado.
- B. DMARC exige simultaneamente SPF e DKIM alinhados.
- C. O SPF desalinhado invalida sempre um DKIM alinhado.
- D. DMARC só compara endereços IP e ignora domínios.
- E. Nenhuma das outras opções.

### 37.

Qual comparação entre STARTTLS SMTP e S/MIME é correta?

- A. STARTTLS dá necessariamente confidencialidade ponta a ponta entre MUAs.
- B. S/MIME só protege o salto entre dois MTAs adjacentes.
- C. Ambos impedem que servidores intermédios vejam metadados e endereços.
- D. STARTTLS protege saltos e pode sofrer downgrade/fallback; S/MIME protege o conteúdo ao nível do utilizador/MUA através dos intermediários.
- E. Nenhuma das outras opções.

### 38.

Pretende-se autenticação do remetente ao destinatário sem permitir que o destinatário prove a autoria a terceiros. Qual das afirmações A-D é correta?

- A. Uma assinatura digital pública é ideal precisamente porque qualquer terceiro a pode verificar.
- B. Cifrar com a chave pública do destinatário prova que só o remetente poderia ter criado a mensagem.
- C. SPF fornece autenticação criptográfica individual do autor do corpo.
- D. DKIM dá não repúdio pessoal do utilizador cujo endereço aparece em `From`.
- E. Nenhuma das outras opções.

## 8. WiFi / IEEE 802.11

### 39.

Dois clientes conhecem a mesma PMK e ligam-se ao mesmo AP em momentos diferentes. Porque devem obter PTKs diferentes?

- A. A derivação inclui, além da PMK, os nonces de ambas as partes e os endereços MAC, que variam ou ligam a chave à sessão/par.
- B. A PMK é publicada pelo AP após cada associação.
- C. A PTK é escolhida apenas pelo servidor RADIUS e enviada em claro.
- D. A GTK substitui a PTK em todo o tráfego unicast.
- E. Nenhuma das outras opções.

### 40.

Qual associação de subchaves da PTK está correta?

- A. KCK cifra dados; KEK assina certificados; TK deriva a palavra-passe.
- B. KCK cifra a GTK; KEK protege o MIC do handshake; TK só serve para broadcast.
- C. KCK autentica mensagens do handshake, KEK protege material de chave como a GTK e TK protege dados unicast.
- D. As três têm exatamente a mesma função e existem apenas por compatibilidade.
- E. Nenhuma das outras opções.

### 41.

Em CCMP, para que serve o Packet Number, além de participar na construção do nonce?

- A. Substitui a PMK na autenticação inicial.
- B. Permite deteção de replay através de controlo de sequência, em conjunto com a autenticação do frame.
- C. Transporta a chave AES cifrada para cada recetor.
- D. É reiniciado em cada frame retransmitida com a mesma chave.
- E. Nenhuma das outras opções.

### 42.

Um atacante captura o 4-way handshake de uma rede WPA2-Personal com uma palavra-passe fraca. Porque é que SAE do WPA3-Personal altera o tipo de ataque disponível?

- A. SAE envia a palavra-passe em claro apenas uma vez, impedindo capturas futuras.
- B. SAE elimina por completo palpites online e compromissos de endpoint.
- C. WPA2 não permite verificar palpites offline a partir do handshake capturado.
- D. No WPA2-PSK, a captura permite validar palpites offline; SAE foi desenhado para não fornecer esse verificador passivo reutilizável.
- E. Nenhuma das outras opções.

### 43.

Sobre a GTK e a hierarquia de grupo de 802.11i, qual das afirmações A-D é correta?

- A. Cada estação gera unilateralmente uma GTK diferente para transmitir broadcast ao AP.
- B. A GTK é a chave usada para autenticar o servidor RADIUS perante a estação.
- C. A GTK é enviada em claro na primeira mensagem do 4-way handshake.
- D. Comprometer uma PTK nunca afeta a entrega protegida de uma GTK a essa estação.
- E. Nenhuma das outras opções.

## 9. Bluetooth

### 44.

Dois dispositivos com Secure Simple Pairing só suportam Just Works. Qual é a garantia mais correta?

- A. O ECDH protege contra escuta passiva, mas a ausência de verificação autenticada deixa o emparelhamento exposto a MITM ativo.
- B. Há a mesma proteção MITM que em Numeric Comparison.
- C. A chave de ligação é enviada em claro, por isso nem escuta passiva é mitigada.
- D. Just Works exige introdução de um PIN aleatório de 128 bits.
- E. Nenhuma das outras opções.

### 45.

Em Numeric Comparison, os dois utilizadores confirmam que veem os mesmos seis dígitos. Que função de segurança desempenha esta ação?

- A. Aumenta a entropia da chave ECDH em exatamente 20 bits.
- B. Liga a interação humana aos valores públicos da troca, tornando a probabilidade de sucesso de um MITM cerca de 1 em 1 000 000 por tentativa.
- C. Cifra a chave privada de cada dispositivo com os seis dígitos.
- D. Substitui a necessidade de ECDH e gera a link key apenas do número mostrado.
- E. Nenhuma das outras opções.

### 46.

Qual diferença entre LE Legacy Pairing e LE Secure Connections é fundamental contra escuta do emparelhamento?

- A. Legacy usa RSA, enquanto Secure Connections usa DES.
- B. Ambos transportam sempre a LTK diretamente sob uma chave pública certificada.
- C. Secure Connections deriva a LTK através de ECDH; Legacy depende de key transport e pode permitir recuperação em modos fracos.
- D. Secure Connections elimina a necessidade de um modelo de associação para proteção MITM.
- E. Nenhuma das outras opções.

### 47.

Qual é o objetivo de um IRK em Bluetooth LE?

- A. Cifrar todos os dados de aplicação em substituição do AES-CCM.
- B. Assinar firmware com não repúdio público.
- C. Negociar o tamanho mínimo da chave BR/EDR.
- D. Permitir que pares autorizados resolvam endereços privados que mudam, reduzindo tracking por terceiros.
- E. Nenhuma das outras opções.

### 48.

Sobre unit keys no emparelhamento Bluetooth legado, qual das afirmações A-D é correta?

- A. São sempre diferentes para cada par porque ambos os dispositivos contribuem igualmente com aleatoriedade.
- B. O seu uso impede impersonação mesmo que a chave de um par seja comprometida.
- C. Só existem em LE Secure Connections e são derivadas por ECDH.
- D. São públicas por desenho e a segurança depende apenas do endereço Bluetooth.
- E. Nenhuma das outras opções.

## 10. RFID e passaportes eletrónicos

### 49.

Uma etiqueta RFID responde sempre com o mesmo identificador cifrado, usando a mesma chave e um modo determinístico. Mesmo sem decifrar, que risco permanece?

- A. O valor estático funciona como pseudónimo e permite correlacionar observações para tracking.
- B. A cifra transforma cada leitura num valor aleatório diferente por definição.
- C. O atacante recupera necessariamente a chave numa única leitura.
- D. A etiqueta torna-se imune a relay porque o identificador não está em claro.
- E. Nenhuma das outras opções.

### 50.

Qual associação entre mecanismos de e-passport está correta?

- A. BAC impede clonagem física por exigir uma assinatura nova do chip a cada leitura.
- B. PA autentica dinamicamente o chip com uma chave privada que nunca sai dele.
- C. PA deteta alteração dos dados assinados; AA prova posse de uma chave privada pelo chip; EAC acrescenta controlo forte para dados sensíveis e leitores autorizados.
- D. EAC deriva todas as chaves apenas da data de nascimento impressa.
- E. Nenhuma das outras opções.

### 51.

Um cartão de acesso executa challenge-response criptograficamente forte, mas um atacante junto à porta encaminha os bits em tempo real para um cúmplice junto do cartão legítimo. Qual é a análise correta?

- A. Trata-se de quebra da cifra por chosen-ciphertext.
- B. É um relay; nonces evitam respostas antigas, mas não provam proximidade. Distance bounding é uma mitigação específica.
- C. Aumentar o tamanho da chave elimina o encaminhamento.
- D. PA de e-passports impede qualquer relay sem restrições temporais.
- E. Nenhuma das outras opções.

### 52.

No protocolo RFID dos slides com SSDK, DT crescente e RSK, qual é a função principal da condição `DT > último_DT`?

- A. Esconder o tipo de etiqueta do leitor legítimo.
- B. Aumentar fisicamente a distância de leitura.
- C. Permitir que qualquer leitor resincronize a etiqueta para um valor menor.
- D. Dar frescura/ordenação e rejeitar reutilização de transações antigas, desde que o estado seja mantido corretamente.
- E. Nenhuma das outras opções.

### 53.

Sobre o caso SpeedPass estudado, qual das afirmações A-D é correta?

- A. Usava AES-256 certificado e foi quebrado apenas por falha biométrica.
- B. A chave secreta tinha 128 bits e nunca pôde ser testada offline.
- C. O identificador de 24 bits era a única informação secreta do sistema.
- D. O ataque exigia modificar fisicamente todos os leitores legítimos antes de observar qualquer troca.
- E. Nenhuma das outras opções.

## 11. Pagamentos eletrónicos, EMV, Bitcoin e E-Cash

### 54.

Qual comparação entre SDA, DDA e CDA é correta?

- A. SDA autentica dados estáticos assinados; DDA acrescenta uma resposta dinâmica a desafio; CDA liga ainda a autenticação dinâmica a dados da transação/criptograma.
- B. SDA usa uma chave privada única por transação, ao passo que DDA só verifica dados estáticos.
- C. CDA elimina a necessidade de o emissor autorizar transações online.
- D. DDA e CDA são formas de verificação do PIN do titular.
- E. Nenhuma das outras opções.

### 55.

Porque pode uma Yes Card ter sucesso num terminal EMV offline baseado em SDA e PIN offline?

- A. A Yes Card consegue forjar a assinatura da CA sobre novos dados arbitrários.
- B. O terminal envia sempre o PIN em claro ao banco, que responde “sim”.
- C. Dados SDA válidos podem ser copiados e o cartão falso pode mentir sobre a verificação do PIN; sem autorização online, o terminal não confirma um MAC do emissor antes de entregar os bens.
- D. SDA autentica dinamicamente o chip e, por isso, o ataque só funciona com a chave privada do cartão original.
- E. Nenhuma das outras opções.

### 56.

Qual sequência de papéis é correta numa autorização EMV online típica?

- A. O terminal cria ARQC; o cartão cria ARPC; o comerciante assina TC.
- B. O cartão cria ARQC para o emissor; o emissor devolve ARPC/ARC; o cartão pode gerar TC como resultado final.
- C. O emissor cria ATC e envia-o ao cartão para cada compra.
- D. ARQC é apenas a assinatura pública dos dados SDA e não inclui estado do cartão.
- E. Nenhuma das outras opções.

### 57.

Qual combinação de falhas facilita um ataque pre-play contra EMV?

- A. Um Unpredictable Number forte e a vinculação autenticada do identificador do terminal.
- B. DDA com desafio imprevisível e dados do terminal cobertos ponta a ponta.
- C. Um ATC monotónico no cartão, por si só, mesmo com todos os restantes campos imprevisíveis e ligados.
- D. Nonce previsível/manipulável e insuficiente vinculação dos dados/identidade do terminal no criptograma validado pelo emissor.
- E. Nenhuma das outras opções.

### 58.

Sobre a resistência de Bitcoin a double spending, qual das afirmações A-D é correta?

- A. A assinatura de uma transação impede matematicamente o proprietário de assinar dois gastos incompatíveis.
- B. A primeira transação observada por qualquer nó vence sempre, independentemente da cadeia posterior.
- C. O Merkle root esconde todas as transações dos restantes participantes.
- D. Reescrever um bloco antigo exige apenas recalcular o hash desse bloco, não os blocos seguintes.
- E. Nenhuma das outras opções.

### 59.

Como conciliam as blind signatures e a base de dados de serial numbers dois objetivos distintos de E-Cash?

- A. A assinatura cega dificulta ligar levantamento e pagamento; o banco continua a detetar gasto duplo ao rejeitar um serial já depositado.
- B. A assinatura cega esconde o valor da moeda do próprio banco, que deixa de poder validá-la.
- C. A base de seriais permite ao comerciante recuperar a identidade civil de qualquer cliente.
- D. O serial é reutilizado por todas as moedas do mesmo valor para reduzir armazenamento.
- E. Nenhuma das outras opções.

## 12. Questões transversais

### 60.

Qual afirmação distingue corretamente replay de relay?

- A. Um nonce fresco impede ambos, porque qualquer mensagem encaminhada passa a ser antiga.
- B. Replay reutiliza uma execução antiga; relay encaminha em tempo real uma execução legítima. Frescura combate o primeiro, mas proximidade exige mecanismos adicionais.
- C. Relay exige sempre descobrir a chave secreta, replay nunca.
- D. São nomes diferentes para o mesmo ataque de colisão de hash.
- E. Nenhuma das outras opções.

### 61.

Qual condição comum permite PFS em protocolos como TLS, IKE e trocas autenticadas genéricas?

- A. Cifrar o segredo de sessão diretamente com uma chave pública estática e arquivar a cifra.
- B. Derivar todas as sessões apenas de uma PSK de longo prazo.
- C. Usar DH efémero autenticado, apagar os expoentes/escalares efémeros e não tornar as chaves antigas deriváveis só a partir do segredo de longo prazo.
- D. Reutilizar o mesmo valor DH para facilitar live partner reassurance.
- E. Nenhuma das outras opções.

### 62.

Um protocolo recebe uma chave pública por uma rede controlada pelo atacante e usa-a imediatamente para verificar assinaturas ou executar DH. Qual é o problema transversal?

- A. Chaves públicas têm de permanecer confidenciais para serem seguras.
- B. Uma chave maior resolve automaticamente a substituição da chave.
- C. O hash da chave recebido pelo mesmo canal hostil fornece autenticação independente.
- D. Sem uma âncora autenticada - certificado, diretório confiável ou segredo prévio - o atacante pode substituir a chave e interpor-se.
- E. Nenhuma das outras opções.

### 63.

Qual combinação associa corretamente autenticação de domínio e autenticação de utilizador no email?

- A. SPF assina o corpo pelo utilizador; S/MIME autoriza o IP do MTA.
- B. DKIM prova necessariamente que uma pessoa específica escreveu cada linha do corpo.
- C. DMARC cifra o conteúdo para os destinatários e oculta o assunto.
- D. SPF/DKIM/DMARC tratam sobretudo legitimidade e alinhamento de domínios; S/MIME pode autenticar o remetente ao nível do utilizador mediante certificados.
- E. Nenhuma das outras opções.

### 64.

Qual das afirmações A-D exprime corretamente a relação entre confidencialidade e integridade?

- A. Qualquer cifra segura deteta automaticamente alterações à cifra.
- B. A reutilização de nonce em CTR só prejudica integridade, nunca confidencialidade.
- C. Um MAC torna a mensagem confidencial porque esconde o seu conteúdo.
- D. Autenticação de origem torna desnecessária a frescura contra replay.
- E. Nenhuma das outras opções.

---

---

## Gabarito

**1.** B  
**2.** C  
**3.** D  
**4.** E  
**5.** A  
**6.** B  
**7.** A  
**8.** D  
**9.** C  
**10.** E *(ESTAVA ERRADA)*  
**11.** B  
**12.** C  
**13.** A  
**14.** D  
**15.** E  
**16.** B  
**17.** C *(ESTAVA ERRADA)*  
**18.** A  
**19.** C  
**20.** B  
**21.** D  
**22.** E *(ESTAVA ERRADA)*  
**23.** A  
**24.** D  
**25.** B  
**26.** E  
**27.** C  
**28.** A  
**29.** B  
**30.** D  
**31.** C  
**32.** E  
**33.** A *(Estava errado)*  
**34.** C  
**35.** B  
**36.** A *(estava errado)*  
**37.** D  
**38.** E  
**39.** A  
**40.** C *(estava errada)*  
**41.** B  
**42.** D  
**43.** E  
**44.** A  
**45.** B  
**46.** C  
**47.** D  
**48.** E  
**49.** A  
**50.** C  
**51.** B  
**52.** D  
**53.** E  
**54.** —  
**55.** —  
**56.** —  
**57.** —  
**58.** —  
**59.** —  
**60.** —  
**61.** —  
**62.** —  
**63.** —  
**64.** —