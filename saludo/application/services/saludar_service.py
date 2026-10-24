from saludo.application.ports.saludar_use_case import SaludarUseCase
from saludo.domain.persona import Persona

class SaludarService(SaludarUseCase):
    def ejecutar(self, persona: Persona) -> str:
        return f"Hola {persona.nombre}"
