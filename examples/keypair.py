import json

from frost_lib import secp256k1_tr as frost

keypair = frost.keypair_new()
print("keypair: ", json.dumps(keypair, indent=4))

pubkey = frost.get_pubkey(keypair.signing_key)
print("verifying_key: ", pubkey)

msg = b"sample message to sign"

signature = frost.single_sign(keypair.signing_key, msg)
print("signature: ", signature)

verified = frost.single_verify(signature, msg, keypair.verifying_key)
print("correct message verified: ", verified)

verified = frost.single_verify(signature, b"wrong message", keypair.verifying_key)
print("wrong message verified: ", verified)
