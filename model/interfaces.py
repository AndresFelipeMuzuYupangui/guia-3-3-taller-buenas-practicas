from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    """Define el contrato para las estrategias de descuento aplicables."""
    
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        """Aplica el descuento correspondiente al total parcial.

        Args:
            total (float): Valor sumado de los productos sin impuestos.

        Returns:
            float: Valor total con el descuento restado.
        """
        pass

class PaymentProcessor(ABC):
    """Define el contrato para procesar transacciones de pago."""
    
    @abstractmethod
    def process(self, amount: float) -> str:
        """Procesa el pago por el monto especificado.

        Args:
            amount (float): Cantidad final a cobrar.

        Returns:
            str: Mensaje de confirmación del proceso de pago.
        """
        pass

class OrderRepository(ABC):
    """Define el contrato para la persistencia de pedidos en base de datos."""
    
    @abstractmethod
    def save(self, order_id: str, order_data: dict) -> str:
        """Guarda la información del pedido en el almacenamiento.

        Args:
            order_id (str): Identificador del pedido.
            order_data (dict): Diccionario con los datos del pedido a guardar.

        Returns:
            str: Mensaje de confirmación de guardado.
        """
        pass

class ReportGenerator(ABC):
    """Define el contrato para generar reportes en distintos formatos."""
    
    @abstractmethod
    def generate(self, order_data: dict) -> str:
        """Genera una representación del pedido.

        Args:
            order_data (dict): Diccionario con los datos del pedido.

        Returns:
            str: Reporte formateado como cadena de texto.
        """
        pass