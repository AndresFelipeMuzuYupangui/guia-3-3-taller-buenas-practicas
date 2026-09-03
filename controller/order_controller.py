from view.console_view import ConsoleView
from model.order import Order
from model.interfaces import PaymentProcessor, OrderRepository, ReportGenerator

class OrderController:
    """Coordina el flujo del programa utilizando los modelos y la vista."""

    def __init__(self, view: ConsoleView, payment_processor: PaymentProcessor,
                 repository: OrderRepository, report_generator: ReportGenerator):
        """Inicializa el controlador inyectando sus dependencias."""
        self.view = view
        self.payment_processor = payment_processor
        self.repository = repository
        self.report_generator = report_generator

    def process_order(self, order: Order, order_id: str) -> None:
        """
        Ejecuta el flujo completo de un pedido.
        
        Args:
            order (Order): Entidad del pedido.
            order_id (str): Identificador único del pedido.
        """
        total = order.calculate_total()
        self.view.display_total(total)

        payment_msg = self.payment_processor.process(total)
        self.view.display_message(payment_msg)

        order_data = {"total": total, "items": order.items}
        save_msg = self.repository.save(order_id, order_data)
        self.view.display_message(save_msg)

        report = self.report_generator.generate(order_data)
        self.view.display_report(report)