from django.db import models

tramites = [
    ('Matricula','Matricula'),
    ('Traspaso','Traspaso'),
    ('Traslado_matricula','Traslado_matricula'),
    ('Radicado_matricula','Radicado_matricula'),
    ('Cambio_coor','Cambio_coor'),
    ('Cambio_servicio','Cambio_servicio'),
    ('Regresar_motor','Regresar_motor'),
    ('Regresar_chasis','Regresar_chasis'),
    ('Transformacion','Transformacion'),
    ('Duplicado_matricula','Duplicado_matricula'),
    ('Inscripcion','Inscripcion'),
    ('Levantaprenda','Levantaprenda'),
    ('Cancelacion_matricula','Cancelacion_matricula'),
    ('Cambio_placas','Cambio_placas'),
    ('Duplicado_placas','Duplicado_placas'),
    ('Rematricula','Rematricula'),
    ('Cambio_carroceria','Cambio_carroceria'),
    ('Otros','Otros')
]
vehiculo = [
    ('Automovil','Automovil'),
    ('Bus','Bus'),
    ('Buseta','Buseta'),
    ('Camion','Camion'),
    ('Camioneta','Camioneta'),
    ('Campero','Campero'),
    ('Microbus','Microbus'),
    ('Tractocamion','Tractocamion'),
    ('Motocicleta','Motocicleta'),
    ('Motocarro','Motocarro'),
    ('Mototriciclo','Mototriciclo'),
    ('Cuatrimoto','Cuatrimoto'),
    ('Volqueta','Volqueta'),
    ('Otro','Otro'),
]

combustible = [
    ('Gasolina','Gasolina'),
    ('Diesel','Diesel'),
    ('Gas','Gas'),
    ('Mixto','Mixto'),
    ('Electrico','Electrico'),
    ('Hidrogen','Hidrogen'),
    ('Etanol','Etanol'),
    ('Biodiese','Biodiese'),
]

imp_rem = [
    ('Manif','Manif'),
    ('Dec','Dec'),
    ('Acta','Acta'),
    ('Entidad','Entidad'),
    ('Lugar','Lugar'),
    ('Codigo','Codigo'),
]

servicio = [
    ('particular','particular'),
    ('publico','publico'),
    ('diplomatico','diplomatico'),
    ('oficial','oficial'),
    ('especial','especial'),
    ('otros','otros'),
]

alerta = [
    ('hurto','hurto'),
    ('lim','lim'),
    ('embargo','embargo'),
    ('otro','otro'),
    ('A_favor','A_favor'),
]

id = [
    ('c','C.C'),
    ('n','NIT'),
    ('x','N.N'),
    ('p','Pasaporte'),
    ('e','C.extranjero'),
    ('t','T.identidad'),
    ('u','NUIP'),
    ('d','C.diplomatico'),
]

class formulario(models.Model):
    placa = models.CharField(max_length=6,unique=True,primary_key=True,null=False)
    tramite = models.CharField(null=False,blank=False,choices=tramites,max_length=21)
    clase_de_vehiculo = models.CharField(null=False,blank=False,choices=vehiculo,max_length=14)
    marca = models.CharField(max_length=30,null=False)
    linea = models.CharField(max_length=50,null=False)
    combustible = models.CharField(null=False,blank=False,choices=combustible,max_length=14)
    color = models.CharField(max_length=30,null=False)
    modelo = models.CharField(max_length=30,null=False)
    cilindraje = models.CharField(max_length=30,null=False)
    capacidad  = models.CharField(max_length=4,null=False)
    blindaje = models.BooleanField()
    desmonteblind = models.BooleanField()
    potencia = models.IntegerField()
    codigo_carroceria = models.CharField(max_length=30,null=False)
    tipo_carroceria = models.CharField(max_length=15,null=False)
    No_motor = models.CharField(max_length=30,null=False)
    No_chasis = models.CharField(max_length=30,null=False)
    No_serie = models.CharField(max_length=30,null=False)
    Vin = models.IntegerField()
    imp_o_rem = models.CharField(null=False,blank=False,choices=imp_rem,max_length=14)
    documento = models.IntegerField()
    fecha = models.DateField()
    tipo_servicio = models.CharField(null=False,blank=False,choices=servicio,max_length=14)
    nombre_empresa = models.CharField(max_length=30,null=False)
    NIT = models.IntegerField()
    datos_alerta = models.CharField(null=False,blank=False,choices=alerta,max_length=14)
    nombres_vendedor = models.CharField(max_length=30,null=False)
    apellido1_vendedor = models.CharField(max_length=30,null=False)
    apellido2_vendedor = models.CharField(max_length=30,null=False)
    id_vendedor = models.CharField(null=False,blank=False,choices=id,max_length=14)
    documento_vendedor = models.IntegerField()
    direccion_vendedor = models.CharField(max_length=100,null=False)
    ciudad_vendedor = models.CharField(max_length=30,null=False)
    telefono_vendedor = models.CharField(max_length=10,null=False)
    firma_vendedor = models.CharField(max_length=30,null=False)
    nombres_comprador = models.CharField(max_length=30,null=False)
    apellido1_comprador = models.CharField(max_length=30,null=False)
    apellido2_comprador = models.CharField(max_length=30,null=False)
    id_comprador = models.CharField(null=False,blank=False,choices=id,max_length=14)
    documento_comprador = models.IntegerField()
    direccion_comprador = models.CharField(max_length=100,null=False)
    ciudad_comprador = models.CharField(max_length=30,null=False)
    telefono_comprador = models.CharField(max_length=10,null=False)
    firma_comprador = models.CharField(max_length=30,null=False)
    
    
    
    
    
    
    
