from datetime import datetime
def validar_fecha(fecha_):
    formato = "%d/%m/%Y"  # Formato esperado: día/mes/año
    try:
        # Intenta convertir la cadena de texto a un objeto datetime
        fecha = datetime.strptime(fecha, formato)
        val=True
        return val
    except ValueError:
        # Si ocurre un ValueError, la fecha no es válida
        val=False
        return val