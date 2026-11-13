#!/usr/bin/env python3
"""Pruebas de ia/verificar.py. Correr: python3 -m unittest discover -s ia -p 'test_*.py'"""
import re
import unittest

import verificar as v


class Secretos(unittest.TestCase):
    def detecta(self, texto: str) -> bool:
        return any(re.search(p, texto) for p in v.SECRETOS)

    def test_detecta(self):
        # Las muestras se arman al vuelo para que este archivo no dispare el propio escaneo.
        for texto in ("-----BEGIN RSA " + "PRIVATE KEY-----", "sk" + "-" + "a" * 30, "gh" + "p_" + "A1" * 18,
                      "li" + "_at=" + "AQED" * 6, "GAME" + "900101" + "HDFRRL09"):
            self.assertTrue(self.detecta(texto), texto)

    def test_no_marca_texto_normal(self):
        for texto in ("La cookie de sesión nunca se guarda aquí.", "https://www.linkedin.com/in/emiliano-milla",
                      "https://www.linkedin.com/help/linkedin/answer/a528176", "password: nunca se guarda aquí"):
            self.assertFalse(self.detecta(texto), texto)


class Certeza(unittest.TestCase):
    def test_marca_lo_que_falta(self):
        texto = ("# T\n\n- Afirmación con fuente [oficial](https://x)\n- Afirmación sin nada\n"
                 "| Regla | Certeza |\n|---|---|\n| algo | [terceros] |\n| otra cosa | ninguna |\n"
                 "```\n- dentro de código no cuenta\n```\n")
        malas = v.afirmaciones_sin_certeza(texto)
        self.assertEqual(len(malas), 2, malas)

    def test_fuentes_legibles(self):
        texto, dias = v.edad_fuentes()
        self.assertIsInstance(dias, int, texto)


if __name__ == "__main__":
    unittest.main()
