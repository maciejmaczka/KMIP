#keysecure


import ssl

from kmip import client
from kmip.pie import objects
from kmip.pie.client import ProxyKmipClient
from kmip.core import enums


print("Config")

client = client.ProxyKmipClient(
hostname='192.168.10.249',
port=5696,
ca='E:\KMIP\ca.pem',
key='E:\KMIP\key.pem',
cert='E:\KMIP\client.pem',
username='kmip',
password='Clico123!'

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
        enums.CryptographicUsageMask.DECRYPT
    ],
    "KeyFromKMIPAgent"
)
print("OK")


print("Register")
#client.register(symmetric_key)
print("OK")



print("Get Key:")
key = client.get("55f9244e809fd16241337f8d4ea5c493cd2312b980b2854bcf58644a1aaf4f6c")
print(key)

print("Close")
client.close()
print("OK")
