

usuarioGuardado = "1234"
passGuardado = "4321"
captcha1 = 234
captcha2 = int(((4-1)*2)/2)       #3 apartir de operaciones de 1, 2, 4
captchaGuardado = captcha1 + captcha2

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

usuarioExterno = input("Ingrese usuario: ")

if True: #usuarioExterno == usuarioGuardado:
    passExterno = input("Ingese Contraseña")
    if True: #passExterno == passGuardado:
        captchaExterno = int(input(f"{captcha1} + {captcha2}="))
        if True:#captchaExterno == captchaGuardado:
            print("Sesión iniciada")
        else:
            print("Error")
    else:
        print("Error")
    
else:
    print("Error")