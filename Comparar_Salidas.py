┌──(kali㉿kali)-[~/Simulacion]
└─$ cat comparar_salidas2.py                     
import xml.etree.ElementTree as ET

def analizar_tripinfo(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    total_duracion = 0
    total_espera = 0
    total_distancia = 0
    total_vehiculos = 0

    for trip in root.findall("tripinfo"):
        total_vehiculos += 1
        total_duracion += float(trip.attrib["duration"])
        total_espera += float(trip.attrib["waitingTime"])
        total_distancia += float(trip.attrib["routeLength"])

    if total_vehiculos == 0:
        return None

    return {
        "vehiculos": total_vehiculos,
        "duracion": total_duracion / total_vehiculos,
        "espera": total_espera / total_vehiculos,
        "distancia": total_distancia / total_vehiculos
    }

# Analizar ambos archivos
antes = analizar_tripinfo("tripinfo_sin_algoritmo.xml")
despues = analizar_tripinfo("tripinfo_con_algoritmo.xml")

# Mostrar resultados
print("📊 Comparativa de Resultados")
print("─────────────────────────────")
print(f"🚗 Vehículos totales: {antes['vehiculos']}")

print("\n⏱ Tiempo de viaje promedio:")
print(f"  Antes : {antes['duracion']:.2f} s")
print(f"  Después : {despues['duracion']:.2f} s")

print("\n⏳ Tiempo de espera promedio:")
print(f"  Antes : {antes['espera']:.2f} s")
print(f"  Después : {despues['espera']:.2f} s")

print("\n📏 Longitud promedio de ruta:")
print(f"  Antes : {antes['distancia']:.2f} m")
print(f"  Después : {despues['distancia']:.2f} m")

# Evaluación simple
mejora_viaje = antes["duracion"] - despues["duracion"]
mejora_espera = antes["espera"] - despues["espera"]

print("\n📝 Conclusión:")
if mejora_viaje > 0 and mejora_espera > 0:
    print("✅ El algoritmo balanceado mejoró los tiempos de viaje y de espera.")
elif mejora_espera > 0:
    print("🟡 El tiempo de espera mejoró, pero el de viaje no cambió significativamente.")
elif mejora_viaje > 0:
    print("🟡 El tiempo de viaje mejoró, pero el de espera no.")
else:
    print("❌ No se observaron mejoras significativas en los tiempos.")

