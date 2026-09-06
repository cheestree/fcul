# Exercícios — Autenticação em trocas de mensagens

## Notação e pressupostos

- `A` e `B` são os participantes.
- `K_AB` é uma chave secreta conhecida apenas por `A` e `B`.
- `K_A` e `K_B` são chaves de longa duração que `A` e `B`, respetivamente, partilham com o KDC.
- `K_S` é uma chave de sessão nova, criada pelo KDC para `A` e `B`.
- `N_A` e `N_B` são *nonces* novos e imprevisíveis, gerados por `A` e `B`.
- `MAC_K(X)` autentica `X` com a chave `K`, mas não o cifra.
- `⟦X⟧_K` representa `X` cifrado e autenticado com AEAD usando `K`. Assume-se que cada utilização inclui um *nonce* AEAD adequado e que o recetor apenas aceita a mensagem se a *tag* for válida.
- O atacante pode observar, bloquear, modificar, reenviar e fabricar mensagens, mas não conhece as chaves secretas.

Em cada exercício:

1. descreve o objetivo e o funcionamento da troca;
2. indica se `A` autentica `B`;
3. indica se `B` autentica `A`;
4. identifica a mensagem exata em que ocorre cada autenticação;
5. justifica a resposta, distinguindo conhecimento de uma chave de **presença numa execução atual**.

---

## Exercício 1 — Autenticação unilateral

`A` e `B` partilham `K_AB`.

```text
1. A -> B: A
2. B -> A: N_B
3. A -> B: A, MAC_KAB("A" || "B" || N_B)
```

Analisa o protocolo seguindo os cinco pontos pedidos. Explica também para que serve `N_B`.

---

## Exercício 2 — Autenticação mútua

`A` e `B` partilham `K_AB`.

```text
1. A -> B: A, N_A
2. B -> A: B, N_B,
           MAC_KAB("B" || A || B || N_A || N_B)
3. A -> B: MAC_KAB("A" || A || B || N_A || N_B)
```

Analisa o protocolo seguindo os cinco pontos pedidos. Explica a utilidade de incluir:

- os dois *nonces*;
- as identidades `A` e `B`;
- os rótulos `"A"` e `"B"`.

---

## Exercício 3 — KDC, *ticket* e prova de posse

`A` partilha `K_A` com o KDC e `B` partilha `K_B` com o KDC. O KDC cria uma chave de sessão nova `K_S`.

```text
1. A -> KDC: A, B, N_A

2. KDC -> A: ⟦N_A, B, K_S, Ticket_B⟧_KA

   Ticket_B = ⟦A, B, K_S⟧_KB

3. A -> B: Ticket_B

4. B -> A: N_B, MAC_KS("B" || A || B || N_B)

5. A -> B: MAC_KS("A" || A || B || N_B)
```

Analisa o protocolo seguindo os cinco pontos pedidos. Indica ainda:

- o que `A` conclui ao aceitar a mensagem 2;
- o que `B` conclui ao abrir o *ticket* na mensagem 3;
- por que razão a mensagem 3, isoladamente, não prova que `A` está presente nesta execução.

---

## Exercício 4 — O *ticket* é suficiente?

Considere agora uma versão reduzida do exercício anterior:

```text
1. A -> KDC: A, B, N_A

2. KDC -> A: ⟦N_A, B, K_S, Ticket_B⟧_KA

   Ticket_B = ⟦A, B, K_S⟧_KB

3. A -> B: Ticket_B
```

Analisa o protocolo seguindo os cinco pontos pedidos. Depois considera o seguinte ataque:

```text
Execução antiga:
A -> B: Ticket_B

Execução posterior:
Atacante -> B: Ticket_B
```

O atacante não consegue abrir nem alterar o *ticket*. Mesmo assim, poderá fazer `B` acreditar incorretamente que `A` iniciou uma nova execução? Que mensagens acrescentarias para corrigir o problema e obter autenticação mútua?

---

# Soluções

> Tenta resolver todos os exercícios antes de consultar esta secção.

<details>
<summary><strong>Solução 1</strong></summary>

O protocolo realiza autenticação unilateral de `A` perante `B`.

- `B` autentica `A` ao aceitar a mensagem 3. Uma resposta correta mostra conhecimento de `K_AB`. Como o MAC inclui o `N_B` novo escolhido por `B`, a resposta está ligada à execução atual e não é a simples repetição de uma resposta antiga.
- `A` não autentica `B`. A mensagem 2 contém apenas um valor público; qualquer atacante poderia enviar um falso desafio a `A`. Não existe nenhuma mensagem em que `B` prove conhecer `K_AB`.
- `N_B` fornece frescura. `B` deve gerar um valor novo em cada execução e rejeitar reutilizações.
- As identidades no MAC ligam a prova aos participantes e dificultam a reutilização da resposta noutro contexto.

Resultado:

```text
A autentica B: não
B autentica A: sim, ao verificar a mensagem 3
```

</details>

<details>
<summary><strong>Solução 2</strong></summary>

O protocolo realiza autenticação mútua.

- `A` autentica `B` ao verificar o MAC da mensagem 2. O MAC prova conhecimento de `K_AB` e inclui `N_A`, que foi acabado de gerar por `A`; por isso, a resposta pertence à execução atual.
- `B` autentica `A` ao verificar o MAC da mensagem 3. A resposta inclui `N_B`, novo e escolhido por `B`, provando a presença de `A` nesta execução.
- Os dois *nonces* ligam as mensagens à mesma execução e fornecem frescura a ambos os lados.
- As identidades ligam as provas aos participantes pretendidos.
- Os rótulos de papel `"A"` e `"B"` fazem com que as respostas esperadas em cada direção sejam diferentes, ajudando a impedir ataques de reflexão.

Resultado:

```text
A autentica B: sim, ao verificar a mensagem 2
B autentica A: sim, ao verificar a mensagem 3
```

</details>

<details>
<summary><strong>Solução 3</strong></summary>

O KDC distribui `K_S`; o *ticket* permite que `B` a obtenha sem receber uma mensagem diretamente do KDC. As mensagens 4 e 5 fazem a prova de posse da chave de sessão.

- Ao abrir e validar a mensagem 2, `A` autentica a resposta do KDC: só o KDC e `A` conhecem `K_A`. A presença de `N_A` liga a resposta ao pedido atual, e `B` liga a chave ao destinatário pretendido.
- Ao abrir o *ticket* da mensagem 3, `B` conclui que o KDC criou `K_S` para comunicação entre `A` e `B`. Porém, ainda não sabe se quem apresentou o *ticket* conhece `K_S`: um atacante pode ter copiado um *ticket* antigo.
- `A` autentica `B` ao verificar a mensagem 4. O MAC mostra que o remetente conhece `K_S`; além de `A` e do KDC, apenas `B` deveria obtê-la abrindo `Ticket_B`.
- `B` autentica `A` ao verificar a mensagem 5. A resposta correta ao `N_B` mostra conhecimento de `K_S` e presença na execução atual.

Resultado entre `A` e `B`:

```text
A autentica B: sim, ao verificar a mensagem 4
B autentica A: sim, ao verificar a mensagem 5
```

Esta conclusão depende de confiar no KDC, de as chaves não estarem comprometidas e de `B` garantir que `N_B` é novo.

</details>

<details>
<summary><strong>Solução 4</strong></summary>

Esta versão distribui uma chave, mas não fornece autenticação mútua entre `A` e `B`.

- `A` não recebe qualquer mensagem de `B`; logo, não autentica `B`.
- O *ticket* diz a `B` que o KDC associou `K_S` à identidade de `A`, mas não prova que o remetente atual conhece `K_S` nem que `A` está presente.
- Um atacante pode repetir `Ticket_B`. Se `B` interpretar a simples receção do *ticket* como uma nova autenticação de `A`, está vulnerável a *replay*.

Portanto, no sentido de autenticação de uma entidade presente na execução:

```text
A autentica B: não
B autentica A: não
```

Uma correção é acrescentar um desafio-resposta em ambas as direções:

```text
4. B -> A: N_B, MAC_KS("B" || A || B || N_B)
5. A -> B: MAC_KS("A" || A || B || N_B)
```

Com esta correção, `A` autentica `B` na mensagem 4 e `B` autentica `A` na mensagem 5.

</details>
