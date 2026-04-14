
## Clase HotelService

### Decisión de diseño

La clase `HotelService` se implementó como una `dataclass`, ya que su propósito es representar una entidad de datos simple dentro del sistema de gestión hotelera.

No contiene lógica compleja ni comportamiento que afecte directamente el flujo del sistema, por lo que no requiere una implementación como clase normal.

---

### Responsabilidad de la clase

La clase `HotelService` tiene una única responsabilidad:

- Representar un servicio ofrecido por el hotel asociado a una reserva (por ejemplo: spa, lavandería, room service, transporte).

Esto sigue el principio de responsabilidad única (SRP), ya que la clase no gestiona reservas ni habitaciones.

---

### Atributos

- `name (str)`: nombre del servicio.
- `price (float)`: costo del servicio.
- `description (str)`: descripción opcional del servicio.
- `date_used (date | None)`: fecha en la que se utilizó el servicio (opcional).

---

### Integración con el modelo

La clase `HotelService` se integra con el sistema a través de la clase `Reservation`.

Se añade un atributo `services: list[HotelService]` en `Reservation`, lo que permite asociar múltiples servicios a una misma reserva.

Esto garantiza que:

- Los servicios estén correctamente agrupados dentro de una reserva.
- La relación entre reserva y servicios sea coherente.
- Se mantenga la estructura del modelo sin acoplar servicios directamente al hotel o a las habitaciones.

---

### Principios aplicados

- **SRP (Single Responsibility Principle)**: la clase tiene una única responsabilidad.
- **Encapsulación**: los servicios se gestionan dentro de la reserva.
- **Bajo acoplamiento**: `HotelService` no depende de otras clases del sistema.
- **Alta cohesión**: todos los atributos pertenecen al concepto de “servicio del hotel”.

---

### Justificación final

El diseño de `HotelService` permite extender fácilmente el sistema en el futuro (por ejemplo, agregar tipos de servicios, facturación o historial de uso) sin modificar la estructura principal del modelo.