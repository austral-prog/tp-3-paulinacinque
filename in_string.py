def check_vowels():
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
    name = input ("Matias").lower()
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"
    print("Contiene a:") 
    print (a in "Matias")
    print("Contiene e:") 
    print(e in "Matias")
    print("Contiene i:") 
    print(i in "Matias")
    print("Contiene o:") 
    print(o in "Matias")
    print("Contiene u:") 
    print(u in "Matias")

check_vowels()
