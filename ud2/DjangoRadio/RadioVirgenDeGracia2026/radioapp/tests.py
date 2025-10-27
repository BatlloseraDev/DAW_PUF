from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class UsuarioApiTest(TestCase):

    #Lo ejecuto con: python manage.py test radioapp.tests
    def test_crear_usuario(self):

        url = reverse('add_usuario')
        data ={
            "nombre": "Persona n 2",
            "apellido": "apellido n 2",
            "nick": "persona nick 3",
            "fecha_nacimiento": "2025-10-25",
            "telefono": "655555555",
            "email": "anonimo@email.com"
        }
        r = self.client.post(url,data=data, content_type='application/json')
        self.assertEqual(r.status_code, 201)