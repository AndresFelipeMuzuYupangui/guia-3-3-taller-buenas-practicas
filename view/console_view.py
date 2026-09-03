class ConsoleView:
    """Maneja la presentación de información al usuario por consola."""

    def display_total(self, total: float) -> None:
        """
        Muestra el total calculado.
        
        Args:
            total (float): Valor total del pedido.
        """
        print(f"Total calculado: {total}")

    def display_message(self, message: str) -> None:
        """
        Muestra un mensaje genérico de estado.
        
        Args:
            message (str): Mensaje a mostrar.
        """
        print(message)

    def display_report(self, report: str) -> None:
        """
        Muestra el reporte generado.
        
        Args:
            report (str): Contenido del reporte.
        """
        print("Reporte:")
        print(report)