# Sample applications for Ledger Blue 

This directory includes sample applications

  - [Hello World](https://github.com/LedgerHQ/blue-sample-apps/tree/master/blue-app-helloworld) : a simple application showing the UI and USB logic

  - [Sample Signature](https://github.com/LedgerHQ/blue-sample-apps/tree/master/blue-app-samplesign) : an application storing a secp256k1 private key, giving the public key to the user and signing messages after getting an on screen user confirmation

  - [BIP 39 Performance Evaluation](https://github.com/LedgerHQ/blue-sample-apps/tree/master/blue-app-bip39perf) : an application demonstrating the flexibility of re-implementing your own cryptographic primitives when necessary 

Before compiling those applications, verify that the following environment variables are set

  - BOLOS_SDK : must point to [secure_sdk_dev](https://github.com/LedgerHQ/blue-secure-sdk/tree/master) that  has been cloned from this repository
  - BOLOS_ENV : must point to the location where the [toolchain](https://github.com/LedgerHQ/blue-devenv/tree/master) has been built
 
