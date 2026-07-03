# SRSD - Notes

## Symmetric Cryptography

Assumes that adversary:

- has access to the ciphertext.
- knows all details about the encryption algorithm, except for the key.
  
Attacks:

- **Cryptanalysis**: the study of analyzing information systems in order to understand hidden aspects of the systems. Gets either the plaintext or the key.
- **Unconditionally secure**: the ciphertext does not reveal any information about the plaintext, even if the adversary has unlimited computational resources. Example: One-time pad.
- **Computationally secure**: the ciphertext does not reveal any information about the plaintext, but only if the adversary has limited computational resources, as either the cost is too high or the time required is impractical.
    Example: AES.
- **Brute-force attack**: the adversary tries all possible keys until the correct one is found. The time required to perform a brute-force attack is proportional to the key length.

**Block Cipher algorithms**:

- transformation of a fixed-length block of plaintext into a fixed-length block of ciphertext using a symmetric key. Examples: AES, DES, 3DES.
- **substitution cipher**: replaces each element of the plaintext with a corresponding element of the ciphertext. Example: AES.
- **transposition cipher**: rearranges the elements of the plaintext to create the ciphertext. Example: DES.
- **product cipher**: combines both substitution and transposition ciphers to create a more secure encryption algorithm. Example: 3DES.
- **Feistel cipher**: a specific type of product cipher that uses a series of rounds to transform the plaintext into ciphertext. Each round consists of a substitution step and a permutation step. Example: DES.

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

---

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

---

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

**Unilateral authentication with public key**:

- database of public keys can be public, but needs to be to protect against changes.
- if user sends:
  - a message encrypted with the other party's public key, the other party can decrypt it, but the adversary can make the other party decrypt arbitrary data encrypted previously with the other party's public key.
  - a challenge, the other party can respond with an encrypted response, but it can be intercepted and personify the other party.

**Mutual authentication**:

- can be a 5, 4 or 3 message protocol if using a public key.
- both parties are authenticated to each other.
  **5 message protocol**:
- they receive a challenge from the other party, and respond with a response that is computed using the shared secret and the challenge, as well as a challenge for the other party to respond to.
- the second party can verify the response from the first party, and respond with a response that is computed using the shared secret and the challenge from the first party.
  **3 message protocol**:
- a party sends the message and the challenge to the other party, and the other party responds with a response that is computed using the shared secret and the challenge, as well as a challenge for the first party to respond to.
- the second party can verify the response from the first party, and respond with a response that is computed using the shared secret and the challenge from the first party.
- vulnerable to reflection attacks. The adversary contacts a party and receives a new challenge and the encrypted previous one. They can create a parallel session with the other party and send the received challenge to the other party, and then respond to the party with the response from the new session. The other party will verify the response and confirm authentication.
- can be avoided by using different keys for the two parties/by deriving a key from the key used to authenticate one of the parties or different challenges with different formats for the two parties.
 **4 message protocol**:
- the party that initiates the protocol should prove its identity first, and then the other party should prove its identity.
- a message is sent, the other party responds with a challenge, and the first party responds with a response that is computed using the shared secret and the challenge, as well as a challenge for the other party to respond to. The other party then responds with a response that is computed using the shared secret and the challenge from the first party.

**Mutual authentication with a timestamp**:

- ASSUMES SYNCHRONIZED CLOCKS
- a party sends a message with an encrypted timestamp to the other party, and the other party responds with a message with an encrypted, incremented, timestamp to the first party. The first party can verify the timestamp from the second party, and the second party can verify the timestamp from the first party.
- personify attack vulnerable if the key is intercepted and immediately replayed to another party. Avoid with encryption of the other party identifier and timestamp.

**Mutual authentication with a public key**:

- public keys need to be obtained from a trusted source.
- private keys need to be obtained from a trusted source and kept secret.
- a solution would be encrypting one party's private key with a key derived from the password and save it with the second party, while encrypting the second party's certificate containing their public key and the first party's private key.

**Mediated authentication**:

- a Key Distribution Center (KDC) is a trusted third party that generates and distributes session keys to the parties that want to communicate securely.
- a party sends a message requesting a session key between them and the other party to the KDC, and the KDC generates a session key and sends it to both parties, encrypted with their respective shared secrets and identifiers. The parties can then use the session key to communicate securely.

- instead of the KDC sending the session key to both parties, it can send the session key to the party that requested it, but CAN be nested encrypted, so that the other party can decrypt it with their shared secret and identifier. The key sent to the other party is called the ticket.

**Key Distribution**:

- generation of a refreshed session key can be based on the previous session key and something related to the long-term shared key. Avoid having the shared key being the encrypted challenge or an incremented version of the challenge.

---

## Authentication handshakes

**Mutual Authentication and Session Key Establishment**:

- after authentication, the messages use the session key + encryption + MAC for confidentiality and integrity (avoids session hijacking) or a sequence number (avoids replay and reording attacks).

**PFS (Perfect Forward Secrecy)**:

- a property of secure communication protocols in which the compromise of long-term keys does not compromise past session keys.
- achieved by generating a new session key for each session based on local information (forgotten after the session terminates), and not deriving the session key from the long-term keys.
- recommended to periodically refresh the temporary key in the same session.
- protects against long-term key compromise, as the adversary cannot use the compromised long-term keys to decrypt past communications (can only listen to the network). Important for escrow systems (third-party hold the keys for decryption).

**Denial of Service Protection**:

- a property of secure communication protocols in which the protocol is designed to prevent or mitigate denial-of-service (DoS) attacks, which are attempts to make a network service unavailable to its intended users.
- uses cookies to verify the identity of the client before allocating resources for the session. The server sends a cookie to the client, which the client must return in subsequent messages to prove its identity.
- can also use puzzles to require the client to perform a computationally expensive operation before allocating resources for the session. The server sends a puzzle to the client, which the client must solve and return in subsequent messages to prove its identity.

**Identity Hiding**:

- a property of secure communication protocols in which the protocol is designed to protect the identity of the parties involved in the communication from both passive (observing the network) and active (intercepting and modifying messages) adversaries.
- anonymous Diffie-Hellman helps with passive attacks but vulnerable to MITM attacks.
- another method works by generating a public DH key, sending to the other party, receiving an OK with the other party's public DH key, and then sending an encrypted message using the calculated shared secret with the identity and encrypted private key of the first party. authenticating itself. The other party responds similarly, authenticating itself.

**Live Partner Reassurance**:

- allow the reuse of DH parameter on B side to improve efficiency and protect against replay attacks.
- a nonce is used when calculating the new shared secret to ensure that the new shared secret is different from the previous one, even if the same DH parameters are used. The nonce is generated by one party and sent to the other party, which uses it in the calculation of the new shared secret.

---

## Password base Network Authentication

Sending password through the network - eavesdropping
Anonymous DH and encrypt password with resulting key - MITM
Save one party's public key locally and then use it to create the secure channel - substitute public key
Create a hash of the password to obtain the key and then use of the symmetric key authentication protocols - dictionary attack

**Lanport Hash**:

- each authentication uses different passwords based on hashed values.
- improved if other fields are used like the password, salt and the other party's identifier.

**SIM swapping**:

- an attack in which an attacker convinces a mobile carrier to transfer the victim's phone number to a SIM card controlled by the attacker. The attacker can then use the victim's phone number to receive authentication codes sent via SMS, allowing them to bypass two-factor authentication and gain access to the victim's accounts.

**2FA (Two-Factor Authentication)**:

- uses HMAC OTP or Time-based OTP to generate a one-time password that is valid for a short period of time. The user must provide both their password and the one-time password to authenticate.

**EKE (Encrypted Key Exchange)**:

- one party sends their identity and an encrypted value, via the hash generated from their password, that is unique to them. The other, knowing the expected hash, chooses the nonce and another value from Diffie-Hellman, and sends it back encrypted with the hash. The first party can then compute the shared secret and send it back encrypted with the new calculated hash and both the old and generated nonces. Lastly, the second party computes the nonces.
- avoids brute-force attacks.
- vulnerable to sophisticated attacks.

**SRP (Secure Remote Password)**:

- a password-authenticated key exchange protocol that allows two parties to establish a shared secret over an insecure network without revealing the password to an eavesdropper.
- uses a combination of public key cryptography and a zero-knowledge proof to authenticate the parties and establish the shared secret.
- The protocol works as follows:
  1. The client generates a random value and computes an ephemeral public value. The password is used later when deriving the shared secret.
  2. The client sends the public value to the server, which computes its ephemeral public value using its random value and the stored password verifier (not the password itself).
  3. The server sends its public value to the client, which computes the shared secret based on its own random value, the server's public value, and the password.
  4. The client sends a proof of knowledge of the shared secret to the server, which verifies it and sends its own proof of knowledge of the shared secret to the client.
  5. Both parties can now use the shared secret for secure communication.

---

## Kerberos

Authentication service for distributed systems that uses symmetric key cryptography and a trusted third party (the Key Distribution Center) to authenticate users and services.
KDC, users, services (offered by servers).

Objectives:

- security: only authorized users can access services.
- scalability: can support a large number of users and services.
- reliability: can handle failures and recover from them.
- transparency: users and services can access the system without being aware of the underlying authentication mechanisms.

**Keys**:

- user-server key is a master key, generated from the user's password and stored in the KDC database.
- server key is a master key, generated from the server's password and stored in the KDC database.
- KDC keeps a local database of all users and service keys and other relevant information.
- KDC has a master key to encrypt and decrypt all keys in the database.
- KDC master key is known only to the administrator.

**Information stored in the KDC database**:

- user ID, master key, and other relevant information for each key.

**Flow**:

1. User sends a request to the KDC for a ticket-granting ticket (TGT) to access a specific service.
2. KDC verifies the user's identity and generates a TGT, which is encrypted with the user's master key and sent back to the user.
3. User decrypts the TGT using their master key and sends it to the KDC along with a request for a service ticket to access the desired service.
4. KDC verifies the TGT and generates a service ticket, which is encrypted with the service's master key and sent back to the user.

Kerberos can require some fields of the initial request to be encrypted with the user's master key, and some fields of the response to be encrypted with the service's master key. This ensures that only the intended recipient can read the information.
Tickets can be used several times, but they have a limited lifetime and can be renewed or refreshed by the KDC. The KDC can also revoke tickets if necessary.

**Delegation of rights**:

- a user can delegate their rights to another user or service by generating a new ticket that includes the delegated rights and sending it to the other user or service. The KDC can verify the delegation and issue a new ticket to the delegated user or service.
- can be proxiable, indicates this TGT can be used to request a service ticket for another user or service. The KDC can verify the delegation and issue a new ticket to the delegated user or service with a proxy flag.
- forwardable, indicates this TGT can be forwarded to another user or service, by allowing the user to request a new TGT for another user or service. The KDC can verify the forwarding and issue a new TGT to the forwarded user or service with a forwardable flag.
- pros: requires explicit requests for right delegation, so auditing is possible.
- cons: performance due to extra messages.

**Realms**:

- each has its own KDC, AS and TGS.
- for a user of realm A to use a service in realm B, the identifier of the service must indicate its from realm B, then the TGS of B must be registered as a service in KDC of realm A. The user asks TGS of realm A for a ticket to TGS of realm B, which is then used to contact the TGS of realm B for a ticket to the service in realm B.

**Ticket lifetime**:

- tickets have a limited lifetime, which is set by the KDC. The lifetime can be specified in the ticket itself, and can be renewed or refreshed by the KDC if necessary.
- tickets can be revoked by the KDC if necessary, for example if a user is no longer authorized to access a service or if a ticket has been compromised. The KDC can maintain a list of revoked tickets and check against it when issuing new tickets.

**Attacks**:

- credential dumping: an attack in which an attacker gains access to the KDC database and extracts sensitive information such as user credentials, service keys, and other relevant information. The attacker can then use this information to impersonate users or services and gain unauthorized access to resources.
- pass-the-ticket: an attack in which an attacker gains access to a valid Kerberos ticket and uses it to authenticate to a service without needing to know the user's password. The attacker can obtain a valid ticket by compromising a user's machine or by intercepting the ticket during transmission. The attacker can then use the ticket to access resources and services that the user is authorized to access, potentially leading to unauthorized access and data breaches.
- silver ticket attack: an attack in which an attacker forges a valid Kerberos service ticket (TGS) for a specific service, allowing them to access that service without needing to authenticate with the KDC. The attacker can create a silver ticket by obtaining the service's secret key (from the KDC database or through other means like brute force) and using it to generate a valid ticket. This allows the attacker to impersonate a legitimate user and gain unauthorized access to the targeted service.
- golden ticket attack: an attack in which an attacker forges a valid Kerberos ticket-granting ticket (TGT), allowing them to impersonate any user and access any service within the Kerberos realm. The attacker can create a golden ticket by obtaining the KDC's secret key (from the KDC database or through other means) and using it to generate a valid TGT. This allows the attacker to gain unrestricted access to resources and services within the Kerberos realm, potentially leading to widespread unauthorized access and data breaches.

---

## TLS (Transport Layer Security)

**Public Key Certificates (X.509)**:

- data structure associating a public key with a user, ensuring key integrity and the correct ownership binding.
- contains: version, serial number, issuer name, subject name, validity period, subject's public key info, optional extensions, and a digital signature from the CA.
- **CA (Certification Authority)**: creates and signs certificates; responsible for their full lifetime including revocation. Users send a request with their public key and identity; the CA validates and signs it.

**TLS Overview**:

- provides a secure channel between two peers — authentication (server always, client optionally), confidentiality, and integrity — over a reliable transport.
- authentication uses asymmetric crypto (RSA, ECDSA, EdDSA) or pre-shared keys (PSK).
- secure even against an attacker with full network control (eavesdropping, tampering, forgery).

**Protocol Architecture**:

- **Record Protocol**: fragments application data into blocks (≤2^14 bytes), protects each record independently using the current traffic keys, and transmits. On receipt: verify, decrypt, reassemble, and pass up.
- **Handshake Protocol**: negotiates protocol version, crypto parameters, authenticates parties, and establishes shared keying material. Runs before any data is sent.
- **Alert Protocol**: sends closure alerts (e.g., `close_notify`, prevents truncation attacks) or error alerts (cause immediate termination). May be encrypted depending on connection state.

**TLS 1.3 Record Protocol**:

- Plain text record format: content type (handshake / application_data / alert), legacy version (ignored), length, fragment.
- Cipher text record format: opaque type always set to 23 (`application_data`), legacy version (always 0x0303, irrelevant since real version is in ClientHello/ServerHello), length, and AEAD-encrypted fragment containing the real content type + optional padding (zero bytes, to defeat traffic analysis).
- **AEAD (Authenticated Encryption with Associated Data)**: unified encryption + authentication. `AEAD(key, nonce, additional_data, plaintext)` where nonce = sequence_number XOR iv (iv is static per direction; sequence number is 64-bit initialized to 0 on key change), and additional_data = the record header (type, version, length). The receiver derives the nonce the same way.

**TLS 1.3 Handshake — Key Exchange Modes**:

- **(EC)DHE**: ephemeral Diffie-Hellman over finite fields or elliptic curves. Provides forward secrecy.
- **PSK-only**: symmetric key from a prior connection (session ticket) or out-of-band setup.
- **PSK with (EC)DHE**: combines both, ensuring forward secrecy even when PSK is used.

**Phase 1 — Key Exchange**:

- **ClientHello**: supported TLS versions, client random nonce (32 bytes, anti-replay), supported cipher suites (AEAD algorithm + hash for HKDF), key material (ephemeral DH public key shares for various groups, and/or PSK labels), and extensions.
- **ServerHello**: selected version, server random nonce, selected cipher suite, and chosen key material (DH key share for (EC)DHE, PSK label, or both). After the two Hello messages, both sides can derive the shared keys. Everything from here is encrypted.

**Phase 2 — Server Parameters** (encrypted):

- **EncryptedExtensions**: extensions not affecting crypto parameters and not tied to certificates (e.g., heartbeat, cookie, padding).
- **CertificateRequest** (optional): if the server wants client certificate authentication. Contains acceptable signature algorithms and CAs.

**Phase 3 — Authentication** (encrypted):

- **Certificate** (server then optionally client): peer's X.509 certificate chain. Omitted if using PSK-only auth, or if client was not requested to authenticate.
- **CertificateVerify**: signature over all prior handshake messages using the sender's private key.
  `signature = Sign(private_key, transcript-hash(Handshake Context || Certificate))`
  The inclusion of random nonces in the Hello messages prevents replay.
- **Finished**: MAC over the entire handshake, computed with a key derived from the selected shared secret. Provides key confirmation, handshake integrity, and identity binding. In PSK mode, also authenticates the handshake as a side effect.
  `MAC = MAC(MAC_key, transcript-hash(Handshake Context || Certificate || CertificateVerify))`

**Session Resumption (NewSessionTicket)**:

- After the handshake, the server sends a `NewSessionTicket` with a PSK identity and a unique `ticket_nonce`. The PSK is derived: `PSK = HKDF(resumption_master_secret, "resumption", ticket_nonce, key_size)`.
- The client includes the PSK label in a future ClientHello to resume without a full handshake (optionally adding (EC)DHE for forward secrecy).
- Maximum ticket lifetime: one week.

**0-RTT Data (Early Data)**:

- With a shared PSK, the client can send encrypted application data on the first flight, before the handshake completes.
- **Not forward secret**: key is derived from the PSK alone.
- **No replay protection between connections**: no fresh random values are used in the key for early data.

---

## IPsec

**Overview**:

- provides integrity, confidentiality, and authenticity at the network layer, transparent to applications and end users.
- implemented at border firewalls/routers or individual hosts; supports IPv4 and IPv6.
- attacks it addresses: IP spoofing, packet sniffing, replay attacks.
- extension headers: **ESP** (Encapsulating Security Payload) and **AH** (Authentication Header). AH should not be used since ESP already provides authentication and AH can create security problems.

**Security Associations (SA)**:

- one-way logical connection for secure data. Bidirectional traffic requires two SAs.
- a SA uses AH or ESP, not both.
- identified by: **SPI** (Security Parameter Index, 32-bit, local to receiver), destination IP address, and security protocol (AH or ESP).
- **SAD** (Security Association Database): stores per-SA parameters — sequence number counter, algorithms and keys, key lifetimes, SA lifetime or max bytes, and protocol mode (transport/tunnel/wildcard).

**Security Policy Database (SPD)**:

- configured by the user or admin; determines which SA (or set of SAs) to apply to each outgoing packet.
- selectors: destination/source IP, transport protocol, username, source/destination ports.

**Transport Mode vs. Tunnel Mode**:

- **Transport mode**: protects the payload above IP (used end-to-end between hosts).
  - AH: authenticates IP payload + selected (immutable) IP header fields.
  - ESP: encrypts IP payload; ESP with auth also authenticates the encrypted payload (not the outer header).
- **Tunnel mode**: wraps the entire inner IP packet inside a new outer IP packet (used gateway-to-gateway).
  - AH: authenticates the inner IP packet + selected fields of the outer IP header.
  - ESP: encrypts the inner IP packet; ESP with auth also authenticates it.

**ESP Header**:

- fields: SPI (identifies SA), sequence number (for replay detection), payload data, padding, next header (identifies the encapsulated protocol, e.g., TCP), and ICV (Integrity Check Value — optional MAC over encrypted ESP minus ICV).
- authentication is performed after encryption.
- Traffic Flow Confidentiality (TFC) padding may be added in tunnel mode to obscure packet sizes.

**Replay Attack Detection**:

- sender: sequence counter starts at 0 when the SA is created; incremented per packet.
- receiver: maintains a sliding window of size W. Accepts a packet only if: (1) sequence number > N-W, (2) not already received, (3) authentication is valid.
- SA must be re-initialized before the counter reaches 2^32-1.

**AH Header**:

- provides a MAC over immutable IP header fields + the full payload. Does not provide confidentiality.
- uses HMAC-MD5-96 or HMAC-SHA-1-96 (mutable fields set to zero during computation).

**Combining SAs**:

- **Transport adjacency**: apply more than one SA (without tunneling), typically ESP then AH.
- **Iterated tunneling**: apply more than one tunnel with potentially different endpoints.
- To get auth + confidentiality: (1) ESP with auth (simplest, but doesn't protect IP header), (2) transport adjacency (ESP + AH, also protects IP header fields), (3) transport+tunnel bundle (AH in transport, ESP in tunnel).

**Key Management (IKEv2)**:

- two types: manual (admin configures keys) or automated (IKEv2).
- four keys typically needed between each pair of nodes.
- IKEv2 uses DH for key exchange + authentication (digital signatures, public key encryption, or pre-shared keys).
- **DoS protection**: cookies — each peer sends a hash (e.g., `hash(IP_s, Port_s, IP_r, Port_r, local_secret)`) in its first message; the secret key is only computed after receiving the cookie back. Prevents spoofed DH parameter floods.
- **MIM prevention**: messages are authenticated after the DH exchange with digital signatures, public key encryption, or symmetric pre-shared key.
- **Logjam attack**: NSA-scale precomputation of DH-1024 (Number Field Sieve) against the small set of standardized IKE groups is plausible (~45M core-years, reducible with custom ASICs). Mitigated by using larger groups (2048+ bits) or elliptic curve DH.

**IKEv2 Exchanges**:

- all communications are request/response pairs.
- **IKE_SA_INIT**: negotiate crypto parameters, send nonces and DH values. `I→R: SAi1, KEi, Ni` / `R→I: SAr1, KEr, Nr, [Certreq]`. No authentication yet; ends with an IKE SA.
- **IKE_AUTH**: exchange identities (ID), certificates (Cert), and authenticate via Auth payload (HMAC or digital signature over the messages + SPI + identity + other party's nonce), encrypted with keys derived from DH. Establishes the first Child SA.
- **CREATE_CHILD_SA**: creates additional Child SAs. Optional new DH parameter for forward secrecy. Messages encrypted with IKE SA keys.
- **INFORMATIONAL**: deletes a SA or reports errors/conditions.
- SAs have no fixed lifetime but should be rekeyed periodically. Rekeying sends fresh nonces and optionally new DH parameters; the SA continues with new keys.

---

## WiFi (IEEE 802.11)

**Security Objectives**: confidentiality, integrity, availability, access control.

**Threats**: eavesdropping, MIM via rogue AP, masquerading, message modification/replay, DoS, traffic analysis. Directional antennas can extend range beyond the standard; weak default configurations are common.

**Security Mechanism Overview**:

- **Pre-Robust Security Networks** (legacy): WEP — no longer secure.
- **Robust Security Networks (RSN)**: WPA, WPA2 (802.11i), WPA3.

**IEEE 802.11i / WPA2**:

- defines an RSN (Robust Security Network) with four phases: discovery, authentication, key management, data protection.
- **Authentication**: either via **IEEE 802.1X + EAP** (using an Authentication Server and RADIUS protocol) for enterprise, or **PSK** for personal use.
  - EAP exchange: STA ↔ AP via EAPOL; AP ↔ AS via RADIUS. AS generates MSK (Master Session Key / AAA Key) and transmits it to the AP.
  - With PSK: authentication is implicit (both sides know the PSK); no AS needed.
  - "Control port" blocks access to other hosts until temporal keys are installed.
- **Key Hierarchy**:
  - **PMK** (Pairwise Master Key): derived from MSK (EAP) or directly from PSK.
  - **PTK** (Pairwise Transient Key): derived from PMK, AP nonce (Anonce), STA nonce (Snonce), and both MAC addresses via a PRF. Splits into: KCK (Key Confirmation Key, for MIC in handshake), KEK (Key Encryption Key, encrypts GTK), TK (Temporal Key, for actual traffic).
  - **GTK** (Group Temporal Key): generated by the AP for broadcast/multicast, distributed encrypted with KEK.

**4-Way Handshake**:

- Confirms PMK existence, verifies cipher suite choice, derives fresh PTK, and distributes GTK.
- AP → STA: Anonce
- STA → AP: Snonce + MIC (using KCK, confirming STA derived PTK)
- AP → STA: encrypted GTK (with KEK) + MIC
- STA → AP: ACK + MIC (confirming receipt)

**Cipher Suites**:

- **TKIP**: temporary AES-incompatible hardware workaround using RC4 + Michael MIC. Includes per-frame key derivation (to defeat Fluhrer-Mantin-Shamir), sequence counters (anti-replay), and countermeasures on MIC failures (lock out for 60s after 2 failures). Not fully secure.
- **CCMP**: full AES-based solution. Uses CCM mode (CTR for confidentiality + CBC-MAC for authentication/integrity). Single 128-bit key for both. Provides confidentiality for payload and integrity for header + payload.

**WPA3**:

- **WPA3-Personal**: replaces PSK exchange with **SAE** (Simultaneous Authentication of Equals), protecting against offline dictionary attacks.
- **WPA3-Enterprise**: optional 192-bit suite (AES-256-GCM + HMAC-SHA-384 + ECC). Requires management frame protection (IEEE 802.11w).
- **Wi-Fi Enhanced Open**: encrypts traffic on open networks to prevent passive eavesdropping (OWE — Opportunistic Wireless Encryption).

**SAE (Simultaneous Authentication of Equals)**:

- Based on the Dragonfly protocol (RFC 7664), which uses Diffie-Hellman.
- The DH generator `a` (called PWE — PassWord Element) is derived deterministically from the password and MAC addresses. `p` comes from standard groups.
- **Commit phase**: both parties send DH values `(s, Z)` where `s = (X + m) mod q` and `Z = a^{-m} mod p`, blinding the private exponent `X`. Each side computes `K = a^{XA*XB} mod p`, then derives PMK.
- **Confirm phase**: exchange hashes proving possession of the DH key.
- Brute-forcing the password requires a new online interaction per guess — no offline attacks possible.
- After SAE, a standard 4-way handshake derives the PTK and GTK.

**WEP (legacy, for reference)**:

- uses RC4 with a 24-bit IV + 40/104-bit key; same key for all stations.
- vulnerabilities: **Fluhrer-Mantin-Shamir attack** (recover key from IV statistics), IV reuse (decrypt second message if plaintext of first is known), non-cryptographic CRC-32 checksum (vulnerable to bit-flip under XOR encryption), no replay protection, unilateral authentication only, recovery of keystream from shared-key authentication challenge/response.

---

## Bluetooth

**Overview**:

- short-range radio for WPANs; low power, 1–100m (class 1/2/3). No line-of-sight needed.
- master/slave topology; up to 7 active slaves in a piconet; piconets connect into scatternets.
- security defined at the link layer; applications can add more.
- physical security (frequency hopping spread spectrum) is ineffective against determined attackers with appropriate hardware.

**Security Model**:

- threats: eavesdropping, MITM, tracking/privacy, message modification/replay, resource misappropriation, DoS.
- services: authentication (device identity via address), confidentiality, integrity, authorization, pairing/bonding.

**BR/EDR Security Modes**:

- Mode 1: no security.
- Mode 2: service-level security enforced after physical link, before logical channel (service discovery possible before auth+encryption).
- Mode 3: link-level security; all connections require auth+encryption before service discovery.
- Mode 4: service-level security using link keys from Secure Simple Pairing.
- Devices use the most secure mode available but may downgrade for compatibility — **downgrade attacks are relevant**.

**Secure Simple Pairing (SSP, v2.1+)**:

- goals: protect against passive eavesdropping (via ECDH) and MITM (via user verification), achieving security equivalent to a 16-character alphanumeric PIN (≥95 bits entropy).
- uses ECDH (P-192 or P-256) to produce a shared DH key → link key. DH key pair can be reused across sessions.
- **Association models**:
  - **Numeric Comparison**: both devices display a 6-digit value derived via `g(PKa, PKb, Na, Nb)`; user confirms they match. MITM probability ≤ 1 in 10^6. Attacker cannot engineer matching values without knowing both nonces (commitment scheme prevents this).
  - **Just Works**: same as Numeric Comparison but user cannot verify — protects only against passive attacks. MITM is fully possible.
  - **Out of Band (OOB)**: exchange crypto parameters over a separate channel (e.g., NFC). One-way OOB protects against MITM on the OOB side only; two-way OOB gives full mutual auth.
  - **Passkey Entry**: one device displays 6 digits; user enters them on the other. The passkey is committed bit-by-bit (k rounds for k-bit secret), preventing forgery.
- Authentication Stage 1: commitments (f1) then nonces then verification (for Numeric Comparison/Just Works) or commitment + OOB data + nonce verification.
- Authentication Stage 2: derive link key (f2) and check values (f3) from DH key, nonces, and randoms. Confirms prior steps completed correctly.

**PIN/Legacy Pairing (BR/EDR modes 2 & 3)**:

- derives Kinit from PIN + BD_ADDR + a random value.
- **Unit key** (KA): generated by one device only; reused for all its connections — allows any device with the key to impersonate or eavesdrop.
- **Combination key** (KAB): both devices contribute random values (XOR'd with Kinit for exchange); different per device pair — more secure.
- vulnerable to **offline brute-force of PIN**: attacker captures auth exchange → precomputes Kinit for all PINs → tries each.

**Authentication**:

- **Legacy (pre-4.1)**: uses E1 (SAFER+-based); unilateral by default (claimant proves identity to verifier). Requires second round for mutual auth.
- **Secure (4.1+)**: HMAC-SHA-256 (h4/h5); both master and slave act as claimant and verifier — inherently mutual.

**Encryption**:

- three modes: no encryption, individually addressed traffic encrypted (with individual link keys), all traffic encrypted.
- key size: 1–16 bytes, negotiated between master and slave. A minimum key size parameter prevents downgrade to short keys.
- **Pre-4.1**: E0 (LFSRs) — considered insecure.
- **4.1+**: AES-CCM.

**Bluetooth Low Energy (BLE)**:

- designed for very constrained devices; different pairing and key hierarchy from BR/EDR.
- **LE Legacy Pairing (v4.0–4.1)**: LTK shared via key transport (not DH agreement). TK derived via OOB, Passkey, or Just Works (all-zero TK = insecure). LTK, IRK, and CSRK distributed encrypted with STK. Considered insecure.
- **LE Secure Connections (v4.2+)**: ECDH (P-256) key agreement similar to SSP. Supports same four association models. LTK is derived from the DH key (not transported). IRK and CSRK distributed encrypted with LTK.
- **Data protection**: AES-CCM for encryption/authentication/integrity, or CSRK-based data signing (integrity only, no confidentiality).
- **Privacy**: Resolvable Private Addresses (RPA) periodically change the Bluetooth address using the IRK, preventing device tracking.
- **Security Mode 1** (encryption): 4 levels (none → unauthenticated pairing → authenticated pairing → LE Secure Connections). **Security Mode 2** (data signing): 2 levels.

---

## RFID

**Overview**:

- automatic identification via radio. A reader broadcasts a request; the tag interprets and responds.
- cryptographic protection scales with tag capability and application requirements.

**Tag Types**:

- **Passive**: no battery; powered by reader's electromagnetic field (Near Field). Range: cm to a few meters. Small and cheap. Response stored in EEPROM.
- **Active**: own power source; can actively transmit at much greater range. Larger and more expensive. Can include sensors and larger memory.
- **Battery-Assisted Passive (Semi-passive)**: battery powers chip; radio still powered by reader. Requires 100× less reader power than passive, longer range (1 order of magnitude), lower error rates, and longer battery life than active.

**Radio Bands**: Low (30–300 kHz), High (13.56 MHz), UHF (860–930 MHz). Higher frequency → greater range. Standardized distances cannot be trusted for security: high-powered directional antennas can extend range beyond spec.

**Applications and Security Issues**:

- **Product Identification (stores/warehouses)**:
  - advantages: faster checkout, inventory management, theft detection.
  - **privacy problems**: tags remain active after purchase. A reader at an entrance can match tags to payment card info (P1), profile a person's clothing value (P2), or a thief can scan for targets (P3).
  - mitigations: disable tag at checkout (ensure full wipe, not partial); encrypt tag (but static ciphertext still tracks).
  - read-write tags: allow repricing attacks (overwrite tag with cheaper item ID), supply chain disruption (zero out tags), or inventory manipulation.
  - fix: authenticate readers with shared secrets (zero-knowledge auth protocol using SSDK + RSK + increasing nonce DT).

- **Passports (e-Passports)**:
  - passive 13.56 MHz tags with 64KB (ISO 14443); stores same data as physical passport + optional biometrics.
  - **threats**: skimming (reading passport from a distance), tracking nationals by country.
  - **Basic Access Control (BAC)**: session key derived from OCR data on the passport page (passport number, DoB, expiry). Protects against random reads. Vulnerable to brute-force if key is guessable (predictable fields).
  - **Passive Authentication (PA)** [mandatory]: chip stores hashes of all data files (SOD) + a digital signature from the document signing key (country-signed). Detects data alterations.
  - **Active Authentication (AA)** [optional]: chip has a non-extractable private key; proves its authenticity by signing a terminal challenge. Prevents chip cloning.
  - **Extended Access Control (EAC)** [optional/mandatory in EU]: run after BAC; validates both chip and terminal using country signing key + card-verifiable certificate (CVC). Protects sensitive data (e.g., fingerprint).

- **Physical Access Control**:
  - RFID cards communicate with door readers connected to a backend database. Supports audit trails and fine-grained access control.
  - **MIM attack (Scenario 1 — no auth)**: adversary reads the card ID directly and clones it.
  - **MIM attack (Scenario 2 — with auth)**: adversary + accomplice relay the challenge from the reader to the victim's card and the response back — circumvents authentication entirely.
  - mitigations: real-time audit log anomaly detection (unexpected hours, double entry without exit), metallic card shield, supplementary PIN, distance-bounding authentication protocols.

- **Contactless Payment (e.g., SpeedPass)**:
  - 40-bit key + 24-bit ID embedded at manufacture; challenge-response authentication.
  - broken via: reverse-engineering the proprietary algorithm + FPGA brute-force of 40-bit key (~1 hour with 16 boards, 32 parallel operations each).

---

## Secure Email

**Email Architecture**:

- **MUA** (Mail User Agent): user-facing client for composing/reading email.
- **MTA** (Mail Transfer Agent): store-and-forward relay using SMTP (port 25). Queues undeliverable mail and retries up to 3–5 days.
- **MSA** (Mail Submission Agent): accepts from MUAs and initiates the relay chain; may be combined with MTA.
- **MDA** (Mail Delivery Agent): receives from inbound MTA and deposits into recipient's mailbox.

**Security Goals**: confidentiality, message flow confidentiality (hide sender/receiver relationship), authentication, integrity, non-repudiation, proof of submission/delivery, anonymity, audit.

**Achieving Key Properties**:

- **Confidentiality**: encrypt content with a symmetric session key; encrypt the session key with the receiver's public key. One encryption of the message regardless of receiver count (efficiency). For distribution lists: local exploder → multiple encrypted session keys; remote exploder → maintainer re-encrypts (requires trusting the maintainer).
- **Authentication of sender**: public key — hash encrypted with sender's private key (signature); or symmetric — MAC with shared secret.
- **Non-repudiation**: public key signatures are sufficient. With symmetric keys, a Notary is required: Alice sends hash to Notary; Notary creates a seal; Bob verifies with Notary. Without a Notary, the receiver cannot prove to a third party who signed.
- **Authentication without Non-repudiation (plausible deniability)**: Alice generates session key S, encrypts S with Bob's public key, signs the encrypted S with her private key, and computes a MAC of the message with S. Bob can verify identity, but cannot prove the message content to a third party (he could have generated any MAC once he got S).
- **Proof of delivery**: requires receiver cooperation. Receiver may refuse to ACK, or sign before reading (and claim crash), or sign after reading (and refuse). Hard to guarantee non-cooperatively.
- **Anonymity / message flow confidentiality**: use an intermediary that receives from many senders; or periodically send encrypted dummy messages through intermediaries with random delays (Mix Networks).

**SMTP Protocol**:

- text-based; commands are 4-letter ASCII words; responses are numeric codes.
- flow: connect → HELO → MAIL FROM → RCPT TO → DATA → QUIT.
- if server unavailable, queue and retry (initial timeout 30 min; total 3–5 days; return to sender on timeout).

**MIME**:

- extends RFC 5322 for rich content (multimedia, non-ASCII).
- adds `Content-Type` and `Content-Transfer-Encoding` headers (e.g., base64).
- S/MIME adds types: `application/pkcs7-mime`, `application/pkcs7-signature`, `multipart/signed`.

**SPF (Sender Policy Framework)**:

- goal: prevent unauthorized MTAs from sending mail as a domain.
- domain publishes authorized sender IPs in a DNS TXT record (`v=spf1 ...`).
- receiver's MTA checks the connecting MTA's IP against the SPF record as soon as `MAIL FROM:` arrives.
- qualifiers: `+` pass (default), `-` fail, `~` soft-fail (accept but mark), `?` neutral.
- tags: `ip4/ip6` (IP ranges), `mx`, `a`, `include` (reference another domain's record), `all`.
- does not authenticate message content or the visible From: header — only the envelope sender.

**DKIM (DomainKeys Identified Mail)**:

- goal: let a domain take responsibility for email by signing it.
- the signing domain publishes its public key in DNS: `selector._domainkey.domain IN TXT "v=DKIM1; k=rsa; p=<base64>"`.
- signature covers message body + selected headers; placed in the `DKIM-Signature` header.
- receiver queries DNS for the public key and verifies the signature.
- any modification to the body or signed headers breaks the signature (mailing list footers can cause DKIM failures).

**DMARC (Domain-based Message Authentication, Reporting and Conformance)**:

- builds on SPF and DKIM; publishes a policy in DNS (`_dmarc.domain IN TXT "v=DMARC1; p=..."`) specifying how to handle failures.
- policies: `none` (monitor only), `quarantine` (treat as suspicious), `reject` (discard).
- **Identifier Alignment**: checks that the message-From: domain aligns with the domain verified by SPF or DKIM (strict = exact match; relaxed = organizational domain match).
- sends aggregate reports to the domain owner so they can monitor the effectiveness of their SPF/DKIM policies.

**STARTTLS**:

- SMTP extension to upgrade a connection to TLS mid-session.
- the server advertises STARTTLS support; client issues the `STARTTLS` command; TLS handshake follows.
- **limitations**: optional (hops may skip it); vulnerable to downgrade attacks (attacker strips the STARTTLS advertisement); certificate validation failures usually default to unprotected delivery.
- **REQUIRETLS**: variant where the sender asserts TLS must be used at every hop; email is not forwarded if TLS is unavailable.
- Similar mechanisms for POP and IMAP.

**DANE (DNS-based Authentication of Named Entities)**:

- domain owner publishes a TLSA DNS record specifying a specific certificate, public key, or CA to trust for TLS on that domain.
- client receiving a TLS certificate matches it against the TLSA record, bypassing or complementing the normal CA trust chain.

**S/MIME (Secure MIME)**:

- extends MIME with encryption and digital signatures.
- **Enveloped data**: session key encrypted with each receiver's public key; content encrypted symmetrically. Multiple receivers: one encrypted session key block per receiver.
- **Signed data**: hash of content signed with sender's private key; both signature and data encoded in base64.
- **Clear-signed data**: data left in plain text; only the signature is base64-encoded (readable by non-S/MIME agents).
- **Signed and enveloped**: both operations combined.
- public key obtained from certificate in the message or from DANE.
- algorithm selection: sender uses previously received `SMIMECapabilities` attribute (list of receiver's supported algorithms in preference order).

**Overall Layering**:

- SPF/DKIM/DMARC authenticate at the domain/MTA level (envelope and header).
- S/MIME/OpenPGP authenticate at the individual user level (message body).
- DKIM signature is in the email header; S/MIME signature is a MIME body part — they are complementary and do not interfere.
- DKIM signature is added after the message leaves the MUA; S/MIME signature is added before.

---

## Electronic Payments

**Card-Based Systems (EMV)**:

- EMV (Europay-Mastercard-Visa) uses smart cards (CPU + tamper-resistant memory) to store secrets and execute crypto operations.
- four entities: client, merchant (acquiring bank), issuing bank; Visa/Mastercard provide clearance/settlement infrastructure.
- **Three phases per transaction**:

**Phase 1 — Card Authentication** (verify card data not altered):

- terminal selects the card application and checks resident card data.
- **SDA (Static Data Authentication)**: terminal uses CA public key → verifies issuer certificate → uses issuer public key → verifies static application data (SAD) signature. Detects data alteration but not card cloning.
  - **"Yes Card" vulnerability**: attacker copies the CA certificate and SAD to a new card; the cloned card responds "yes" to any PIN. Only exploitable offline (online terminals verify MAC with issuer).
- **DDA (Dynamic Data Authentication)**: same as SDA, plus terminal sends a nonce that the card must sign with its own private key (SIC). Prevents cloning.
- **CDA (Combined Data Authentication)**: DDA plus a signature over application-dependent data including the ARQC and terminal challenge. Stronger than DDA.

**Phase 2 — Cardholder Verification** (user is the owner):

- CVM list in the card specifies the preference order (PIN, signature, nothing).
- **Offline PIN**: PIN typed by user is sent to the card for local comparison. Response is not protected.
- **Online PIN**: PIN encrypted by terminal; sent to issuer bank for verification.

**Phase 3 — Transaction Authorization** (issuer bank approves):

- card generates **ARQC** (Authorization ReQuest Cryptogram) = MAC(transaction data) using a key shared with the issuer, plus **ATC** (Application Transaction Counter, acts as nonce to prevent replay).
- terminal → acquirer → payment network → issuer: transmits ARQC + transaction details.
- issuer verifies ARQC, checks funds, returns **ARPC** = MAC(ARQC ⊕ ARC) and ARC (Authorization Response Code).
- card is notified of the result; terminal finalizes the transaction.
- **Note**: the terminal identifier is NOT included in the ARQC — enabling the pre-play attack.

**Pre-Play Attack (on EMV)**:

- exploits the ATM's predictable Unpredictable Number (UN, used as nonce in the protocol).
- **Variant 1 — guessable UN**: attacker runs a few transactions to predict future UNs, pre-computes valid ARQCs for those UNs, and uses them with a cloned card later (valid for 1–2 days).
- **Variant 2 — UN manipulation**: terminal generates UN1 but doesn't protect the transaction message with a MAC. Attacker intercepts and substitutes UN1 with a known UN for which they have a valid ARQC from a prior real transaction. Issuer accepts because it validates the ARQC, and the terminal doesn't validate the UN in the IAD.

---

**Bitcoin**:

- decentralized peer-to-peer system; coins are a chain of transactions. No central authority.
- ownership: current owner has a public-private key pair; transferring a coin = signing hash(previous transaction) + next owner's public key.
- **Double-spending prevention**: public blockchain — earliest announced transaction wins. All nodes can verify prior transactions.
- **Blockchain**: each block contains a set of transactions + Merkle root + hash of previous block + nonce. A valid block requires proof-of-work: find a nonce such that `hash(block)` starts with N zero bits (~10 minutes of work). Checking is O(1).
- **Security**: changing a past block requires redoing all subsequent blocks' proof-of-work. Secure as long as honest nodes control > 50% of CPU power.
- **Mining reward**: started at 50 BTC/block; halves every 4 years (3.125 BTC in 2025–2028). Also transaction fees.
- **Forks**: two nodes broadcasting competing next blocks simultaneously; resolved when the next block extends one branch (all nodes switch to the longest chain).
- **Merkle Tree**: transactions stored in a Merkle tree; only the root goes in the block header. Old transactions can be pruned while preserving block validity.
- **Privacy**: public keys are anonymous addresses. New key pairs per transaction improve privacy. Multi-input transactions can link ownership; if one key is de-anonymized, linked transactions are too.

**E-Cash (DigiCash)**:

- centralized anonymous electronic cash. Bank signs coins; verifies against a double-spending database.
- **Blind Signatures** (core anonymity mechanism): client blinds the coin's hash before the bank signs it so the bank cannot link the coin to the withdrawal later.
  1. Client picks random blinding factor `r`; computes `Blinded_H = H(serial#) · r^e mod m`.
  2. Bank signs: `Sign(Blinded_H) = (H(serial#) · r^e)^d mod m = H(serial#)^d · r mod m`.
  3. Client removes blinding: divide by `r` → gets `H(serial#)^d mod m` = valid RSA signature on the hash. Bank never saw `H(serial#)` unblinded.
- **Coin structure**: `{serial#, keyversion, {H(serial#)}SIG_KR_Bank_coin}`. Keyversion encodes denomination, currency, and expiry.
- Different signing keys per denomination: prevents a client from escalating a coin's value.
- Bank signs `H(serial#)` not `serial#` directly: prevents RSA-based forgery (forging requires inverting the hash function).
- **Payment**: client sends exact amount (no change — receiving change breaks anonymity since the bank can correlate withdrawals). Coins encrypted with the bank's public key in transit. `Hash(payment_info)` detects tampering. `Hash(description)` proves to vendor that client accepted the transaction terms without revealing it to the bank.
- **Double-spending prevention**: bank stores all seen serial numbers per signing key; purges entries when the key expires.
- **Recovery of lost coins**: client sends last 16 withdrawal messages (with blinding factors) to bank → bank removes blinding factors → returns unspent coins.