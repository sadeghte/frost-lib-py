from frost_lib import ed25519 as frost

keypair = frost.keypair_new()
print(keypair.model_dump_json(indent=4))

tweeked = frost.pubkey_tweak(keypair.verifying_key, b"1")
print("tweeked: ", tweeked)
