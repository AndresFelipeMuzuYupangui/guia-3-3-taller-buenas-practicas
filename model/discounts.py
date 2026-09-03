from model.interfaces import DiscountStrategy

class VIPDiscount(DiscountStrategy):
    """Estrategia de descuento del 20% exclusiva para clientes VIP."""
    
    def apply_discount(self, total: float) -> float:
        """Aplica un 20% de descuento al total dado.

        Args:
            total (float): Valor original sin descuento.

        Returns:
            float: Valor con el 20% descontado.
        """
        return total * 0.8

class RegularDiscount(DiscountStrategy):
    """Estrategia de descuento del 10% para clientes regulares."""
    
    def apply_discount(self, total: float) -> float:
        """Aplica un 10% de descuento al total dado.

        Args:
            total (float): Valor original sin descuento.

        Returns:
            float: Valor con el 10% descontado.
        """
        return total * 0.9

class StudentDiscount(DiscountStrategy):
    """Estrategia de descuento del 30% para estudiantes universitarios.
    Nueva funcionalidad agregada.
    """
    
    def apply_discount(self, total: float) -> float:
        """Aplica un 30% de descuento al total dado.

        Args:
            total (float): Valor original sin descuento.

        Returns:
            float: Valor con el 30% descontado.
        """
        return total * 0.7