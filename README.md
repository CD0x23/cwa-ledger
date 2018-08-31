# Sample Signature App for Ledger Blue & Ledger Nano S

This application demonstrates a more complex user interface, the Secure Element
proxy logic, cryptographic APIs and flash storage.

Before compiling, verify that the following environment variables are set:

  - BOLOS_SDK : must point to [secure_sdk_dev](https://github.com/LedgerHQ/blue-secure-sdk/tree/master) that  has been cloned from this repository
  - BOLOS_ENV : must point to the location where the [toolchain](https://github.com/LedgerHQ/blue-devenv/tree/master) has been built

Run `make load` to build and load the application onto the device. After
installing and running the application, you can run `demo.py` to test a
signature over USB.

Note that in order to run `demo.py`, you must install the `secp256k1` Python
package:

```
pip install secp256k1
```

See [Ledger's documentation](http://ledger.readthedocs.io) to get started.
