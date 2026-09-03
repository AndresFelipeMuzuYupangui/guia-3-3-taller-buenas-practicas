from model.interfaces import DiscountStrategy

class Order:
    """Representa un pedido y su lógica de cálculo base."""

    def __init__(self, items: list[float], discount_strategy: DiscountStrategy):
        """Inicializa el pedido con sus ítems y estrategia de descuento.

        Args:
            items (list[float]): Lista de precios de los productos.
            discount_strategy (DiscountStrategy): Estrategia de descuento a aplicar.
        """
        self.items = items
        self.discount_strategy = discount_strategy
        self.tax_rate = 1.19

    def calculate_total(self) -> float:
        """Calcula el valor total de un pedido.

        Aplica primero el descuento correspondiente según la estrategia definida 
        y posteriormente suma el impuesto definido en tax_rate.

        Returns:
            float: valor total calculado.
        """
        subtotal = sum(self.items)
        discounted_total = self.discount_strategy.apply_discount(subtotal)
        return discounted_total * self.tax_rate