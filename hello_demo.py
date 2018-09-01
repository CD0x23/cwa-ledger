#!/usr/bin/env python
#*******************************************************************************
#*   Ledger Blue
#*   (c) 2016 Ledger
#*
#*  Licensed under the Apache License, Version 2.0 (the "License");
#*  you may not use this file except in compliance with the License.
#*  You may obtain a copy of the License at
#*
#*      http://www.apache.org/licenses/LICENSE-2.0
#*
#*  Unless required by applicable law or agreed to in writing, software
#*  distributed under the License is distributed on an "AS IS" BASIS,
#*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#*  See the License for the specific language governing permissions and
#*  limitations under the License.
#********************************************************************************
from ledgerblue.comm import getDongle
from ledgerblue.commException import CommException
from secp256k1 import PublicKey

INS_SIGN            = "02"
INS_SET_TRANSFER_ID = "11"
INS_SET_DATE        = "12"
INS_SET_CURRENCY    = "13"
INS_SET_AMOUNT      = "14"
INS_SET_COLD_WALLET = "15"
INS_SET_HOT_WALLET  = "16"


def send_to_ledger(instruction_code, data):
    offset = 0
    response = ""
    while offset <> len(data):
        if (len(data) - offset) > 255:
            chunk = data[offset : offset + 255] 
        else:
            chunk = data[offset:]
        if (offset + len(chunk)) == len(data):
            p1 = 0x80
        else:
            p1 = 0x00
        apdu = bytes(("80" + instruction_code).decode('hex')) + chr(p1) + chr(0x00) + chr(len(chunk)) + bytes(chunk)
        response = dongle.exchange(apdu)
        offset += len(chunk)
    return response      


textToSign = "textToSign87ry923y7r7h9dj0ke"

dongle = getDongle(True)
publicKey = dongle.exchange(bytes("8004000000".decode('hex')))
print "publicKey " + str(publicKey).encode('hex')
try:
    send_to_ledger(INS_SET_TRANSFER_ID, "t234567189512")
    send_to_ledger(INS_SET_DATE, "26 Agustos 2018 15:38")
    send_to_ledger(INS_SET_CURRENCY, "BTC")
    send_to_ledger(INS_SET_AMOUNT, "631.5132")
    send_to_ledger(INS_SET_COLD_WALLET, "3B4oStNceDPrQBEyeKbG7yEwmPgBKMwbBd")
    send_to_ledger(INS_SET_HOT_WALLET, "1Hzh3CEJT8ZA1Yw5JdpyoDdnLmyJomBhNf")
    signature = send_to_ledger(INS_SIGN, textToSign)
    print "signature " + str(signature).encode('hex')
    publicKey = PublicKey(bytes(publicKey), raw=True)
    signature = publicKey.ecdsa_deserialize(bytes(signature))
    print "verified " + str(publicKey.ecdsa_verify(bytes(textToSign), signature))
except CommException as comm:
    if comm.sw == 0x6985:
        print "Aborted by user"
    else:
        print "Invalid status " + comm.sw 
