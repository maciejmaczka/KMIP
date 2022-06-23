#keysecure


import ssl

from kmip import client
from kmip.pie import objects
from kmip.pie.client import ProxyKmipClient
from kmip.core import enums


print("Config")

client = client.ProxyKmipClient(
hostname='192.168.10.251',
port=5696,
ca='E:\KMIP\Vormetric\ca.pem',
key='E:\KMIP\Vormetric\key.pem',
cert='E:\KMIP\Vormetric\cert.crt',


)
print("OK")


print("KMIP Connection")
client.open()
print("OK")



print("New Key")
symmetric_key = objects.SymmetricKey(
    enums.CryptographicAlgorithm.AES,
    128,
    (
        b'\x00\x01\x02\x03\x04\x05\x06\x07'
        b'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
    ),
    [
        enums.CryptographicUsageMask.ENCRYPT,
        enums.CryptographicUsageMask.DECRYPT,
        enums.CryptographicUsageMask.EXPORT
    ],
    "KeyFromKMIPAgent"
)
print("OK")


print("Register")
#client.register(symmetric_key)
print("OK")



print("Get Key:")
key = client.get("59f07c3f-80e1-4a66-8b48-e87cbcc0eb80")
print(key)

print("Close")
client.close()
print("OK")
