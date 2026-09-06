import time,random,qrcode


print("aguarde...")
time.sleep(1)
print("pronto")

aleatory=random.randint(1,100)
print(aleatory)

img=qrcode.make("https://github.com/nathan-cabral")
img.save("qr_perfil_Nathan.png")
