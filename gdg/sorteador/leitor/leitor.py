from abc import ABC, abstractmethod
from Participante import Participante
from typing import List

class Leitor(ABC):
    @abstractmethod
    def ler(self, caminho: str, ingressosParaIgnorar: List[str], apenasComCheckin: bool) -> List[Participante]:
        pass