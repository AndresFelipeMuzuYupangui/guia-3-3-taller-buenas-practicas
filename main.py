from controller.order_controller import OrderController
from model.discounts import VIPDiscount

# Asumiendo que crearon estas clases base en model/implementations.py
from model.implementations import CardPayment, MySQLRepository, TextReport
from model.order import Order
from view.console_view import ConsoleView


def main():
    """Función principal de ejecución del sistema."""

    # 1. Instanciar dependencias (Modelo y Vista)
    view = ConsoleView()
    payment_processor = CardPayment()
    repository = MySQLRepository()
    report_generator = TextReport()

    # 2. Inyectar dependencias al Controlador (DIP)
    controller = OrderController(view, payment_processor, repository, report_generator)

    # 3. Crear los datos del pedido inicial para validación
    items = [10000, 25000, 5000]
    order_id = "ORD-001"

    # Usamos VIPDiscount para garantizar el total esperado de 38080
    order = Order(items, VIPDiscount())

    # 4. Ejecutar el sistema
    controller.process_order(order, order_id)


if __name__ == "__main__":
    main()
