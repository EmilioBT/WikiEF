from django.test import TestCase
from django.urls import reverse
from .models import Herramienta
from django.utils.text import slugify


class HerramientaListViewTest(TestCase):
    def setUp(self):
        self.herramienta1 = Herramienta.objects.create(
            title="Herramienta 1", 
            description="Descripción de prueba 1"
        )
        self.herramienta2 = Herramienta.objects.create(
            title="Herramienta 2", 
            description="Descripción de prueba 2"
        )
    
    def test_herramientas_list_view(self):
        response = self.client.get(reverse('herramientas:herramientas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Herramienta 1")
        self.assertContains(response, "Herramienta 2")

class HerramientaDetailViewTest(TestCase):
    def setUp(self):
        self.herramienta = Herramienta.objects.create(
            title="Herramienta 1", 
            description="Descripción de prueba"
        )
        self.page_slug = slugify(self.herramienta.title)
    
    def test_herramienta_detail_view(self):
        response = self.client.get(reverse('herramientas:herramientas', args=[self.herramienta.id, self.page_slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Herramienta 1")
        self.assertContains(response, "Descripción de prueba")