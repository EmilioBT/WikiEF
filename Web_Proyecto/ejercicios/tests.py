from django.test import TestCase
from ejercicios.models import Ejercicio
from django.urls import reverse

class EjercicioModelTest(TestCase):
    def test_crear_ejercicio(self):
        ejercicio = Ejercicio.objects.create(
            title="Ejercicio de Prueba",
            description="Descripción del ejercicio de prueba",
        )
        self.assertEqual(ejercicio.title, "Ejercicio de Prueba")
        self.assertEqual(str(ejercicio), "Ejercicio de Prueba")
        self.assertIsNotNone(ejercicio.created)
