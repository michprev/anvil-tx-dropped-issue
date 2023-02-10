
import woke.testing.core
from woke.utils import get_package_version

if get_package_version("woke") != "2.0.0":
    raise RuntimeError("Pytypes generated for a different version of woke. Please regenerate.")

woke.testing.core.errors = {b'\x08\xc3y\xa0': {'': ('woke.testing.internal', ('Error',))}, b'NH{q': {'': ('woke.testing.internal', ('Panic',))}}
woke.testing.core.events = {}
woke.testing.core.contracts_by_fqn = {'contracts/Counter.sol:Counter': ('pytypes.contracts.Counter', ('Counter',))}
woke.testing.core.contracts_by_metadata = {b'\xa2dipfsX"\x12 \xb5%\xbeuz\x95NCD\xd2Y\x1f\xe3\x906<(\xa9\x11\xe4\xb8\x7f\x86\x90fM\xcc\x1c:\xcb\x935dsolcC\x00\x08\x12\x003': 'contracts/Counter.sol:Counter'}
woke.testing.core.contracts_inheritance = {'contracts/Counter.sol:Counter': ('contracts/Counter.sol:Counter',)}
woke.testing.core.contracts_revert_index = {}
woke.testing.core.deployment_code_index = [(((612, b'\xa2\x15$En]\xa2|\x07 ]\xd7\x9c\xdf\xf6\xf5\xe2\x94\ne7\xb6\xb3\xc0\xb4nW\xcd\xe0\xb8\xbcL'),), 'contracts/Counter.sol:Counter')]
