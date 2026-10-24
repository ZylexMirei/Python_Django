import json
from django.test import SimpleTestCase
from django.urls import reverse
from saludo.application.services.saludar_service import SaludarService
from saludo.domain.persona import Persona

class ServicioSaludoTests(SimpleTestCase):
    def test_saludo_sin_django(self):
        self.assertEqual(SaludarService().ejecutar(Persona("Natalia")), "Hola Natalia")

    def test_api_nombre(self):
        respuesta = self.client.post(reverse("saludar"), data=json.dumps({"nombre": "Natalia"}), content_type="application/json")
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json(), {"mensaje": "Hola Natalia"})

    def test_api_nombre_vacio(self):
        respuesta = self.client.post(reverse("saludar"), data=json.dumps({"nombre": " "}), content_type="application/json")
        self.assertEqual(respuesta.status_code, 400)

    def test_api_json_invalido(self):
        respuesta = self.client.post(reverse("saludar"), data="{mal json", content_type="application/json")
        self.assertEqual(respuesta.status_code, 400)

    def test_api_metodo_get_no_permitido(self):
        self.assertEqual(self.client.get(reverse("saludar")).status_code, 405)
