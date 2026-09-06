# Exercícios — Autenticação em trocas de mensagens
## Exercicio 1

Serve para autenticar cada cliente. Neste caso, B autentica A pois alem dos IDs de ambos os clientes, tambem inclui o nonce do cliente B. A assinatura so pode ser verificada pelos clientes que tenham a chave partilhada K_AB, logo B pode verificar. O uso de um nonce serve para proteger contra ataques de replay.

## Exercicio 2

A troca autentica ambos os clientes com um protocolo de 3 mensagens. A autentica B na linha 2 e B autentica A na linha 3, visto partilharem a mesma chave e usarem os nonces respetivos para evitar ataques de replay. Os rotulos servem para proteger contra ataques de reflexao.

## Exercicio 3

A autentica a resposta do KDC na linha 2 e recebe o seu ticket, inclusive o ticket de B. A envia o ticket de B para B na linha 3, e B e A autenticam-se mutuamente na linha 4 e 5, visto partilharem a mesma chave de sessão K_S. O nonce serve para proteger contra ataques de replay.