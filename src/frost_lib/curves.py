from frost_core import ed25519 as ed25519_r  # type: ignore
from frost_core import secp256k1 as secp256k1_r  # type: ignore
from frost_core import secp256k1_evm as secp256k1_evm_r  # type: ignore
from frost_core import secp256k1_tr as secp256k1_tr_r  # type: ignore

from .abstracts import BaseCurveWithNonceAddress, BaseCurveWithTweakedPubkey, BaseCurveWithTweakedSign


class Ed25519(BaseCurveWithTweakedPubkey):
    def _get_curve(self):
        return ed25519_r

    @property
    def name(self):
        return "ed25519"


class Secp256k1(BaseCurveWithTweakedPubkey):
    def _get_curve(self):
        return secp256k1_r

    @property
    def name(self):
        return "secp256k1"


class Secp256k1Tr(BaseCurveWithTweakedSign):
    def _get_curve(self):
        return secp256k1_tr_r

    @property
    def name(self):
        return "secp256k1_tr"


class Secp256k1EVM(BaseCurveWithNonceAddress):
    def _get_curve(self):
        return secp256k1_evm_r

    @property
    def name(self):
        return "secp256k1_evm"


ed25519 = Ed25519()
secp256k1 = Secp256k1()
secp256k1_tr = Secp256k1Tr()
secp256k1_evm = Secp256k1EVM()
