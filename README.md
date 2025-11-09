# 🔬 Linear Nonce Detector — quick reference (code-block style)

This small snippet tests whether two ECDSA signatures imply a **linear relation** between their nonces and — if so — computes the implied nonce `k`.  
It is a lightweight detector: compute `Δs = s1 − s2` and `Δz = z1 − z2`; if `Δs` is invertible modulo the curve order `n`, then

delta_s = (s1 − s2) mod n
delta_z = (z1 − z2) mod n

- If `delta_s ≠ 0`, computes:


k = delta_z * inverse_mod(delta_s, n) (mod n)

and prints `k` (hex).  
- If `delta_s == 0` it reports no linear relation found.

---

## Why this works (math summary)

From ECDSA signing:


s ≡ k⁻¹ (z + r·d) (mod n)
⇒ s*k ≡ z + r·d

Subtract two signatures:


(s1 − s2) * k ≡ (z1 − z2) (mod n)
⇒ k ≡ (z1 − z2) * (s1 − s2)⁻¹ (mod n)

So when `(s1 − s2)` is invertible mod `n`, you can directly compute `k`. Once `k` is known, `d` can be recovered from a single signature (if desired).

---

## ASCII flow (visual)



Input: r1, s1, z1 r2, s2, z2
↓ ↓
compute delta_s = (s1-s2) mod n
compute delta_z = (z1-z2) mod n
↓
if delta_s != 0:
k = delta_z * (delta_s)^-1 mod n → print k
else:
print "no linear relation"


---

## When to use

- Quick pre-check for **linear nonce relationships** between two signatures.  
- Use before attempting full algebraic key recovery or brute-force refinement.  
- Useful in research/forensics when testing whether two signatures leak nonce info.

---

## Limitations & caveats

- **Only valid** if the two signatures are related as assumed. For arbitrary unrelated signatures the computed `k` will be meaningless.  
- Requires `(s1 − s2)` to be invertible modulo the curve order `n` (i.e., not zero mod `n`).  
- Does **not** compute the private key `d` itself — it only finds `k`. (You can compute `d` afterward using `d = (s1*k - z1) * r1⁻¹ mod n`.)  
- Numerical correctness depends on using the correct curve order `n` (here `secp256k1`).

---

## Example output (successful)


✅ Wykryto liniową zależność k! k = 0x1a2b3c...


---

## Ethical reminder

Use this code **only** on data you own or when you have explicit permission to analyze. Recovering or using private keys without authorization is illegal and unethical. This snippet is provided for research, auditing, and educational use only.

© 2025 — Author: [ethicbrudhack]

BTC donation address: bc1q4nyq7kr4nwq6zw35pg0zl0k9jmdmtmadlfvqhr
