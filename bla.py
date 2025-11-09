from ecdsa.numbertheory import inverse_mod
from ecdsa.ecdsa import generator_secp256k1

# Dane z transakcji
r1 = int("d8e2d92d3fca2a3293ed2e57c80a8db40069da2229225756b77de2f967baa1fb", 16)
r2 = int("5ebecec888b158797ded9ebc1421b4797d4077c2e16945f45361ac33f6abf41b", 16)
s1 = int("6f2dc5ce39475b4c98ae27285a36939aadf19e38b3845c57400ef08326d24d23", 16)
s2 = int("340050758fd9de606d45383f63f1b236a7a47318c595e99c910f4b943a88a364", 16)
z1 = int("cc5260cf9f0c439f2847dae4560a63f62da6fb6682ed77df872076f0f0aafd34", 16)
z2 = int("5429e50aa800fe787d59bc03594476c704c86ce7b58060025ffe9ee6c2658273", 16)

n = generator_secp256k1.order()

# Obliczamy różnicę `s`
delta_s = (s1 - s2) % n

# Obliczamy różnicę `z`
delta_z = (z1 - z2) % n

# Jeśli `delta_s` i `delta_z` są stałe, `k` jest zależne liniowo!
if delta_s != 0:
    k = (delta_z * inverse_mod(delta_s, n)) % n
    print(f"✅ Wykryto liniową zależność k! k = {hex(k)}")
else:
    print("❌ Brak zależności liniowej w k")
