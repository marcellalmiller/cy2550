# Part 1
### 1.1
- -pbkdf2 derives a cryptographic key from the passphrase using the PBKDF2 algorithm.
- It is required to derive a secure fixed-length key from the arbitrarily long passphrase.
### 1.2
- The checksums are different because the first block of each encryption has a different
  pseudo-random initialization vector whose randomness carries into each subsequent block.
- Deterministic encryption algorithms make it much easier for adversaries to obtain the
  cryptographic key using chosen plaintext attacks.
### 1.3
1. CBC produced 37 distinct blocks with none repeated. ECB produced 3 distinct blocks, and 
  the most common block repeated 24 times.
2. ECB leaked how many times the plaintext repeated the same data (in this case letters). 
  Attackers could break the encryption with frequency analysis, or in the case of larger
  blocks, by finding patterns. 
3. I would ask if the encryption algorithm is non-deterministic.

# Part 2
1. My colleague isn't protected because they can't verify whether the file came from me.
  A matching message and hash is no guarantee because the attacker controls the channel
  and could change both, and presumably knows the hashing algorithm I used.
2. Using an HMAC hashes my file with a shared secret key. My colleague can be certain the 
  file came from me if hashing its contents with the shared secret gives the same hash
  as the one I sent.
3. With SHA-256, the attacker can edit the message and impersonate me. With HMAC, they
  can edit the message, but if they do, my colleague will know, so they cannot impersonate
  me.

# Part 3
1. The verification link proves that someone with access is purposefully trying to create
  a key connected to the email. It does not prove that their identity matches the name they
  entered, or even that they are the owner of the email.
2. Assuming the attacker doesn't have access to my classmate's Northeastern email, I could 
  look up the key associated with their email using OpenPGP. If their key is publicly linked
  to that address, they must have verified it. So if the downloaded key matches the key I 
  find on OpenPGP, I can safely conclude it actually belongs to my classmate, and was not
  just created by the attacker using their email. 

# Part 4
### 4.2
1. The first packet with a few thousand bits contains the encrypted private key (the private
  key encrypted with the receiver's public RSA key). The second packet contains the encrypted 
  message itself. 
2.The entire message is not encrypted using RSA because its algorithm was designed to produce
  keys of a fixed-length output, not encrypt a message of an arbitrary length.
3. This construction is called hybrid cryptosystem. 
### 4.3
1. The sender's private key is used for signing.
2. The sender's public key is used for verifying their signature.
3. The receiver's public key is used for encryption.
4. The receiver's private key is used for decryption.
5. Signing provides authentication.

# Part 5
- The RSA-4096 key was created by multiplying large primes together and the Ed25519 key was
  created using logarithms and elliptical curves, which do not grow in size as quickly as 
  multiplication.
- So even though RSA is much larger, it would take around the same amount of computation to
  break them.

# Part 6

# Part 7
### 7.1
- I used ChatGPT and used the prompt "Write me a Python function that encrypts a file with AES."

### 7.2
- The code does not authenticate the sender. An attacker could pose as the sender and the
  receiver wouldn't know. This violates the authenticity of the encryption.
- The code does not prevent an attacker from modifying the file without the receiver knowing
  because it isn't signed. This violates the integrity of the encryption.
- The code does not prevent the author from claiming they sent the file. This violates the
  non-repudiation of the encryption.
