from Api import obtener_informacion
from UI import seleccion_usuario, mostrar_propiedades_cultivo

def main():
    print("Bievenido al programa Análisis de Laboratorio Suelos en Colombia ")
    departamento, municipio, cultivo, limiteRegistros = seleccion_usuario()

    informacionDf = obtener_informacion(limiteRegistros)

   
    filtro = (informacionDf['departamento'] == departamento) & \
             (informacionDf['municipio'] == municipio) & \
             (informacionDf['cultivo'] == cultivo)

    propiedades_cultivo = informacionDf[filtro]

    mostrar_propiedades_cultivo(propiedades_cultivo)

if __name__ == "__main__":
    main()
