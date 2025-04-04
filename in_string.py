def check_vowels():
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
    name = input ("Ingresa su nombre").lower()
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"
    print("Contiene a:") 
    print (a in name)
    print("Contiene e:") 
    print(e in name)
    print("Contiene i:") 
    print(i in name)
    print("Contiene o:") 
    print(o in name)
    print("Contiene u:") 
    print(u in name)

check_vowels()
