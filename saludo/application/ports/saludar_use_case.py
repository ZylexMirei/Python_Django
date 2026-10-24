from abc import ABC, abstractmethod
from saludo.domain.persona import Persona

class SaludarUseCase(ABC):
    @abstractmethod
    def ejecutar(self, persona: Persona) -> str:
        raise NotImplementedError
