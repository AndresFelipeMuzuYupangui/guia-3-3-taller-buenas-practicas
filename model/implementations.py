from model.interfaces import OrderRepository, PaymentProcessor, ReportGenerator


class CardPayment(PaymentProcessor):
    """Implementación concreta para procesar pagos con tarjeta."""

    def process(self, amount: float) -> str:
        """
        Procesa un pago dada una cantidad.

        Args:
            amount (float): Monto a procesar.

        Returns:
            str: Mensaje de confirmación del pago.
        """
        return f"Procesando pago de ${amount:.2f} con tarjeta..."


class MySQLRepository(OrderRepository):
    """Implementación concreta para simular la persistencia en MySQL."""

    def save(self, order_id: str, order_data: dict) -> str:
        """
        Simula el guardado de un pedido en la base de datos.

        Args:
            order_id (str): Identificador único del pedido.
            order_data (dict): Información del pedido.

        Returns:
            str: Mensaje de estado de la persistencia.
        """
        return f"Pedido '{order_id}' guardado exitosamente en la base de datos MySQL."


class TextReport(ReportGenerator):
    """Implementación concreta para generar reportes en texto plano."""

    def generate(self, order_data: dict) -> str:
        """
        Genera un reporte formateado en consola.

        Args:
            order_data (dict): Información del pedido.

        Returns:
            str: Reporte formateado en texto.
        """
        items_str = ", ".join(str(item) for item in order_data.get("items", []))
        total = order_data.get("total", 0.0)
        return (
            f"=== REPORTE DE COMPRA ===\n"
            f"Productos: [{items_str}]\n"
            f"Total a pagar: ${total:.2f}\n"
            f"========================="
        )
