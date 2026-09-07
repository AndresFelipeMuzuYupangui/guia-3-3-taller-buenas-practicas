Taller 3: Refactorización MVC, Principios SOLID y Pruebas Unitarias
Este proyecto consiste en la refactorización de un sistema monolítico de gestión de pedidos en Python hacia una arquitectura limpia utilizando el patrón Modelo-Vista-Controlador (MVC), aplicando los Principios SOLID y garantizando la calidad del software mediante Pruebas Unitarias (pytest) y linters (ruff).

Integrantes
Andrés Muzu - Propietario del Repositorio

Diana Franco - Colaborador/a

Docente: Jonathan R. Torres C.

Arquitectura del Proyecto (MVC)
El sistema ha sido estructurado en tres capas independientes para lograr una clara separación de responsabilidades:

Modelo (model/): Contiene la lógica de negocio, entidades de dominio, estrategias de descuento e interfaces para persistencia, pagos y reportes.

Vista (view/): Encargada exclusivamente de la interacción de salida por consola con el usuario.

Controlador (controller/): Recibe las interacciones del usuario, invoca las operaciones en el modelo y delega la representación de datos a la vista.

 Aplicación de Principios SOLID
Single Responsibility Principle (SRP):

ConsoleView se limita a formatear e imprimir salidas.

Order solo gestiona los datos e impuestos del pedido.

OrderController coordina la ejecución sin contener lógica de negocio ni salidas directas por pantalla.

Open/Closed Principle (OCP):

El sistema está abierto a la extensión pero cerrado a la modificación. Se añadió la nueva funcionalidad StudentDiscount creando una nueva clase sin modificar el código interno de Order.

Liskov Substitution Principle (LSP):

Todas las estrategias de descuento (VIPDiscount, RegularDiscount, StudentDiscount) derivan de DiscountStrategy y pueden ser utilizadas indistintamente sin romper el cálculo.

Interface Segregation Principle (ISP):

Se crearon abstracciones independientes y enfocadas (DiscountStrategy, PaymentProcessor, OrderRepository, ReportGenerator) en lugar de una interfaz pesada y monolítica.

Dependency Inversion Principle (DIP):

OrderController e Order dependen de abstracciones (interfaces de model/interfaces.py) y no de implementaciones concretas, las cuales son inyectadas en el punto de entrada (main.py).

 Estructura del Proyecto
Plaintext
.
├── controller/
│   └── order_controller.py      # Coordinación del flujo MVC
├── model/
│   ├── discounts.py             # Estrategias de descuento (incluye StudentDiscount)
│   ├── implementations.py       # Implementaciones concretas de interfaces
│   ├── interfaces.py            # Contratos/Abstracciones (ABC)
│   └── order.py                 # Entidad principal de Order
├── tests/
│   └── test_order.py            # Pruebas unitarias con pytest
├── view/
│   └── console_view.py          # Salida en consola
├── .gitignore                   # Archivos ignorados por Git
├── main.py                      # Punto de entrada de la aplicación
├── README.md                    # Documentación del proyecto
└── requirements.txt             # Dependencias del proyecto
 Instalación y Configuración
Clonar el repositorio:

Bash
git clone <https://github.com/AndresFelipeMuzuYupangui/guia-3-3-taller-buenas-practicas.git>
Crear y activar un entorno virtual:

Bash
python -m venv .venv
# En Windows:
.venv\Scripts\activate
# En Linux/Mac:
source .venv/bin/activate
Instalar dependencias de desarrollo:

Bash
pip install pytest ruff
⚙️ Ejecución del Sistema
Para ejecutar el flujo principal y verificar el correcto funcionamiento del sistema:

Bash
python main.py
Salida esperada por consola
El cálculo de referencia mantiene el valor exacto esperado de $38080.0 para un cliente VIP con productos de [10000, 25000, 5000]:

Plaintext
Total calculado: 38080.0
Procesando pago de $38080.00 con tarjeta...
Pedido 'ORD-001' guardado exitosamente en la base de datos MySQL.
Reporte:
=== REPORTE DE COMPRA ===
Productos: [10000, 25000, 5000]
Total a pagar: $38080.00
=========================
🧪 Ejecución de Pruebas Unitarias y Calidad de Código
Pruebas con pytest
Ejecutar la suite de pruebas unitarias para validar los cálculos, estrategias de descuento y la nueva funcionalidad:

Bash
pytest -v
Verificación de Estilo y Linting con ruff
Garantizar que el código cumple con los estándares PEP 8:

Bash
ruff check .
Si hay errores de formato automáticos, se pueden corregir ejecutando:

Bash
ruff check --fix
