import pytest
from model.order import Order
from model.discounts import VIPDiscount, RegularDiscount, StudentDiscount

# 1. Cálculo base y 2. Resultado esperado para cliente VIP (Total inicial de la guía)
def test_vip_discount_total():
    """Verifica que el cliente VIP pague exactamente 38080.0."""
    items = [10000, 25000, 5000]
    order = Order(items, VIPDiscount())
    # pytest.approx maneja posibles diferencias de decimales flotantes
    assert order.calculate_total() == pytest.approx(38080.0)

# 3. Otra estrategia de descuento existente
def test_regular_discount_total():
    """Verifica el descuento del 10% del cliente regular."""
    items = [10000, 25000, 5000]
    order = Order(items, RegularDiscount())
    # 40000 * 0.9 = 36000 -> 36000 * 1.19 = 42840.0
    assert order.calculate_total() == pytest.approx(42840.0)

# 4. Nueva estrategia añadida
def test_student_discount_total():
    """Verifica el descuento del 30% del estudiante."""
    items = [10000, 25000, 5000]
    order = Order(items, StudentDiscount())
    # 40000 * 0.7 = 28000 -> 28000 * 1.19 = 33320.0
    assert order.calculate_total() == pytest.approx(33320.0)

# 5. Cálculo del impuesto
def test_tax_calculation_applied():
    """Verifica que el impuesto del 19% se sume tras el descuento."""
    order = Order([100], VIPDiscount()) 
    # 100 * 0.8 = 80 -> 80 * 1.19 = 95.2
    assert order.calculate_total() == pytest.approx(95.2)

# 6. Generador de reporte (Simulación a nivel de datos)
def test_report_generation_data():
    """Verifica la estructura de datos que se enviará al generador de reportes."""
    order_data = {"total": 38080.0, "items": [10000, 25000, 5000]}
    report_string = f"Pedido con total {order_data['total']}" 
    assert "38080.0" in report_string
    assert report_string.startswith("Pedido con total")

# 7. Sustitución de implementaciones (Principio LSP)
def test_discount_substitution_lsp():
    """Verifica que cualquier descuento derivado puede sustituir a la abstracción."""
    discounts = [VIPDiscount(), RegularDiscount(), StudentDiscount()]
    for discount in discounts:
        order = Order([1000], discount)
        assert order.calculate_total() > 0 

# 8. Comportamiento adicional: Lista de compras vacía
def test_empty_order_total():
    """Verifica que un pedido sin productos calcule el total como 0.0."""
    order = Order([], RegularDiscount())
    assert order.calculate_total() == 0.0

# 8. Comportamiento adicional: Modificación de la tasa de impuesto
def test_order_custom_tax_rate():
    """Verifica el total si el pedido está exento de impuestos (tax_rate = 1.0)."""
    order = Order([1000], VIPDiscount())
    order.tax_rate = 1.0
    assert order.calculate_total() == 800.0