# SRSD - Notes

## Symmetric Cryptography

Assumes that adversary:

- has access to the ciphertext.
- knows all details about the encryption algorithm, except for the key.
  
Attacks:

- Cryptanalysis: the study of analyzing information systems in order to understand hidden aspects of the systems. Gets either the plaintext or the key.
- Unconditionally secure: the ciphertext does not reveal any information about the plaintext, even if the adversary has unlimited computational resources. Example: One-time pad.
- Computationally secure: the ciphertext does not reveal any information about the plaintext, but only if the adversary has limited computational resources, as either the cost is too high or the time required is impractical.
    Example: AES.
- Brute-force attack: the adversary tries all possible keys until the correct one is found. The time required to perform a brute-force attack is proportional to the key length.

**Block Cipher algorithms**:

- transformation of a fixed-length block of plaintext into a fixed-length block of ciphertext using a symmetric key. Examples: AES, DES, 3DES.
- substitution cipher: replaces each element of the plaintext with a corresponding element of the ciphertext. Example: AES.
- transposition cipher: rearranges the elements of the plaintext to create the ciphertext. Example: DES.
- product cipher: combines both substitution and transposition ciphers to create a more secure encryption algorithm. Example: 3DES.
- Feistel cipher: a specific type of product cipher that uses a series of rounds to transform the plaintext into ciphertext. Each round consists of a substitution step and a permutation step. Example: DES.

**General principles**:

- number of rounds: the number of times the encryption algorithm is applied to the plaintext. More rounds generally provide better security, but also increase the computational cost.
- function F should be non-linear and complex to prevent linear and differential cryptanalysis and have good avalanche effect.
- should make it difficult to find the key

**DES**:

- 64-bit block cipher with a 56-bit key.
- vulnerable to brute-force attacks due to the small key size, and to differential and linear cryptanalysis due to the small number of rounds.
- Double DES: C = E(K2, E(K1, P)) where K1 and K2 are different keys and P = D(K1, D(K2, C)). Vulnerable to meet-in-the-middle attack.
- Triple DES: C = E(K1, D(K2, E(K1, P))) where K1 and K2 are different keys and P = D(K1, E(K2, D(K1, C))). Provides better security than Double DES, but is slower than AES. Brute-force requires trying 2^112 keys, but meet-in-the-middle attack requires only 2^56 keys. If K1 and K2 are the same, then it is equivalent to single DES.

**AES**:

- sub-key substitution and permutation.

**ARIA**:

- substitution, permutation and key-mixing.
- 128, 192, or 256-bit key size and a block size of 128 bits.
- 12/14/16 rounds for 128/192/256-bit keys, respectively.

**Cipher Modes**:

- **Electronic Codebook (ECB)**: each block of plaintext is encrypted independently. Vulnerable to pattern attacks.
- **Cipher Block Chaining (CBC)**: each block of plaintext is XORed with the previous ciphertext block before being encrypted. Requires an initialization vector (IV) for the first block. Provides better security than ECB, but is vulnerable to padding oracle attacks.
- **Cipher Feedback (CFB)**: converts a block cipher into a self-synchronizing stream cipher. Each block of plaintext is XORed with the previous ciphertext block before being encrypted. Requires an initialization vector (IV) for the first block. Provides better security than CBC, but is vulnerable to bit-flipping attacks.
- **Output Feedback (OFB)**: converts a block cipher into a synchronous stream cipher. Each block of plaintext is XORed with the output of the previous encryption operation. Requires an initialization vector (IV) for the first block. Provides better security than CFB, but is vulnerable to bit-flipping attacks.
- **Counter (CTR)**: generates a keystream by encrypting a counter value and XORing it with the plaintext. Provides better security than CBC, but requires a unique nonce for each encryption.

**Principles of Stream Cipher Algorithms**:

- faster and simpler than block ciphers.
- very little space in memory and power consumption.
- very small error propagation.
- inefficient software implementation.
- many are secret.

**LFSR (Linear Feedback Shift Register)**:

- a shift register whose input bit is a linear function of its previous state. The most commonly used linear function is the XOR operation.
- generates a pseudo-random sequence of bits that can be used as a keystream for encryption.
- vulnerable to known-plaintext attacks and correlation attacks.

**ChaCha20**:

- a stream cipher designed to provide better security and performance than traditional stream ciphers.
- uses a 256-bit key, 32-bit initialization vector, and a 96-bit nonce to generate a keystream that is XORed with the plaintext to produce the ciphertext.
- resistant to known-plaintext attacks, correlation attacks, and timing attacks.
- used in TLS 1.3.
- AES backup, 3x faster in in-software only implementations.

Types of random generators:

- **TRNG (True Random Number Generator)**: generates random numbers from a physical process, such as electronic noise or radioactive decay. Provides high-quality randomness, but is slow and expensive.
- **PRNG (Pseudo-Random Number Generator)**: generates random numbers from a deterministic algorithm, such as a linear congruential generator or a Mersenne Twister. Provides fast and efficient randomness, but is vulnerable to attacks if the algorithm is not secure or if the seed is known.
- **PRF (Pseudo-Random Function)**: a function that takes a secret key and an input value and produces a pseudo-random output value. Provides fast and efficient randomness, but is vulnerable to attacks if the key is not secure or if the input value is known.
- **BlumBlum-Shub**: a PRNG that is based on the difficulty of factoring large composite numbers via prime numbers.

## Asymmetric Cryptography

**One-way function**: Y = f (X) is easy, but X = f -1 (Y) is infeasible

**Trap-door one-way function**: Y = f K(X) is easy; X = f -1K(Y) becomes easy if K is known (but X = f -1K(Y) infeasible without knowing K)

**RSA**:

- given n = pq, where p and q are large primes, it is easy to compute n, but infeasible to factor n into p and q. 
- public key is (n, e) and the private key is (n, d), where e and d are chosen such that ed ≡ 1 (mod φ(n)), with φ(n) = (p-1)(q-1).
- vulnerable to brute-force attacks if p and q are not large enough, mathematical attacks if p and q are too close, and timing attacks if the implementation is not constant-time.

**Diffie-Hellman**:

- based on the discrete logarithm problem.
- MITM is solved by using a central directory, but replay attacks are still possible.
- given a prime p and a generator g, it is easy to compute g^a mod p, but infeasible to compute a given g^a mod p. 
- global parameters p and g are public, while a and b are private
- User A generates a parameter a and computes A = g^a mod p, while user B generates a parameter b and computes B = g^b mod p. They exchange A and B, and each computes the shared secret K.

**Elliptic Curve Diffie-Hellman**:

- based on the elliptic curve discrete logarithm problem.
- given an elliptic curve E over a finite field F, a point P on E, and a scalar k, it is easy to compute kP, but infeasible to compute k given P and kP.
- P is a public point, d is a random private key and Q is the public key.
- User A generates a parameter a and computes A = aP, while user B generates a parameter b and computes B = bP. They exchange A and B, and each computes the shared secret K = abP. Global parameters E and P are public, while a and b are private.

**Hash**:

- One-way function: H(X) is easy, but X = H -1(Y) is infeasible
- Collision-resistant: it is infeasible to find two different inputs X and Y such that H(X) = H(Y)
- Pre-image resistant: it is infeasible to find an input X such that H(X) = Y for a given output Y
- Second pre-image resistant: it is infeasible to find a different input Y such that H(X) = H(Y) for a given input X
- Vulnerable to birthday attacks: it is possible to find two different inputs X and Y such that H(X) = H(Y) with a probability of 0.5 after approximately 2^(n/2) hash computations, where n is the output length of the hash function
- Cryptoanalysis: finding collisions in the compression function.

**SHA-3**:

- Sponge construction: a cryptographic primitive that can be used to build hash functions, stream ciphers, and other cryptographic algorithms. It consists of a fixed-length state that is updated by absorbing input data and squeezing output data.

**MAC**:

- Message Authentication Code: a short piece of information used to authenticate a message and to provide integrity and authenticity assurances on the message. It is generated by applying a cryptographic hash function to the message and a secret key.

**HMAC**:

- Hash-based Message Authentication Code: a specific type of MAC that uses a cryptographic hash function and a secret key. It is designed to be resistant to length extension attacks and provides strong security guarantees.

**CMAC**:

- Cipher-based Message Authentication Code: a specific type of MAC that uses a block cipher and a secret key. It is designed to provide strong security guarantees and is widely used in various cryptographic protocols.
- Uses AES or triple DES as the underlying block cipher.

**Encryption and Authentication**:

- Hash followed by encryption: E(K, M || h(M)) where h is a hash function, M is the message, and K is the encryption key. This provides both confidentiality and integrity.
- Authentication followed by encryption: E(K2, M || MAC(K1, M)) where K1 and K2 are different keys. This provides both confidentiality and integrity, but requires two keys.
- Encryption followed by authentication: C = E(K1, M), send (C, MAC(K2, C)) where K1 and K2 are different keys. This provides both confidentiality and integrity, but requires two keys.
- Independent encryption and authentication: (E(K1, M), MAC(K2, M)) where K1 and K2 are different keys. This provides both confidentiality and integrity, but requires two keys.

Counter with Cipher Block Chaining Message Authentication Code (CCM):

- mode of operation for symmetric key cryptographic block ciphers that provides both confidentiality and authenticity.
- combines the Counter (CTR) mode of encryption with the Cipher Block Chaining Message Authentication Code (CBC-MAC) for authentication.

## Authentication and Key Distribution (Simple Protocols)

**Unilateral authentication**:
- only one party is authenticated to the other party.
    Example: a client authenticates to a server using a password.
- the password sent can be vulnerable to eavesdropping, and then the attacker can impersonate the client to the server/other client.
- no guarantee that the client is communicating with the intended server, as the attacker can impersonate the server to the client.

**Attacks**:

- eavesdropping: the attacker intercepts the communication between two parties and can read the messages being exchanged.
- personify: the attacker impersonates one of the parties to the other party, and can send messages on behalf of the impersonated party.
- fake network address: the attacker can change the source address of the messages being sent, and can impersonate one of the parties to the other party.
- database attack: the attacker can gain access to the database of one of the parties, and can obtain sensitive information such as passwords or keys.
- session hijacking: the attacker can take over an existing session between two parties, and can send messages on behalf of one of the parties.

**Unilateral authentication with shared secret**:

- a message is sent, the other party responds with a **challenge**, and the first party responds with a response that is computed using the **shared secret** and the **challenge**.
- adversary can't get the **shared secret**.
- after initial connection, **hijacking is possible**, as the adversary can **intercept** the messages being exchanged and can send messages on behalf of one of the parties.
- **no authentication** of the other party, as the adversary can **impersonate** the other party to the first party.
- **offline attacks are possible** on the key, as the adversary can **intercept** the challenge and response messages, and can try to compute the **shared secret** using the intercepted messages.
- adversary can read the database of one of the parties, and can obtain sensitive information such as passwords or keys.
  **if sending the challenge encrypted with the shared key**:
- if the challenge is a recognizable quantity, the other user can get some guarantees that they are communicating with the intended party, as the adversary can't compute the response without knowing the shared secret.
- if the format is well-known, the adversary can get several encrypted messages and can try to compute the shared secret using the intercepted messages without having to listen to the challenge and response messages.
  **if sending an encrypted timestamp (ASSUMES SYNCHRONIZED CLOCKS)**:
- minimum number of messages.
- simplifies the protocol, no need for generation and storage of a challenge.
- used in request/response protocols (RPC).
- eavesdrop and replay attack vulnerable, as the adversary can intercept the messages being exchanged and can replay the messages to one of the parties immediately. Avoid with timestamp caching and interval checking.
- personify attack vulnerable if the key is intercepted and immediately replayed to another party. Avoid with encryption of the other party identifier and timestamp.
- personify attack vulnerable if the other party is convinced to set their clock to a time in the past, and then the adversary can replay the messages to one of the parties.
- clock sync needs to be done securely (not always possible).

  **if public key**: