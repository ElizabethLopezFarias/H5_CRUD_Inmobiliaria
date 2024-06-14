from django.db import models

class Tipo_inmueble(models.Model):
    id_tipo_inmueble = models.AutoField(primary_key=True)
    CHOICES = [
        ('Departamento', 'Departamento'),
        ('Casa', 'Casa'),
        ('Parcela', 'Parcela'),
    ]
    tipo = models.TextField(choices=CHOICES)
    
    def __str__(self):
        return self.tipo


class Tipo_usuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    CHOICES = [
        ('Arrendador', 'Arrendador'),
        ('Arrendatario', 'Arrendatario')
    ]

    tipo = models.CharField(choices=CHOICES)
    
    def __str__(self):
        return self.tipo


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=50, blank=False, null=False)
    nombre_comuna = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f"{self.nombre_comuna}, {self.nombre_region}"


class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50, blank=False, null=False)
    numero = models.CharField(max_length=10, blank=False, null=False)
    depto = models.CharField(max_length=10, blank=True, null=True)
    id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.depto if self.depto else ''}, {self.id_ubicacion}"


class Usuarios(models.Model):
    usuario = models.OneToOneField('auth.User',on_delete=models.CASCADE, default=1)
    tipo_usuario = models.ForeignKey('Tipo_usuario', on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    correo = models.EmailField()

    def __str__(self):
        return self.usuario.username
        #return f"{self.nombre} {self.apellido} {self.usuario}


class Inmuebles(models.Model):
    id_inmueble = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField()
    m2_construidos = models.IntegerField(default=0)
    m2_terreno = models.IntegerField(default=0)
    n_estacionamientos = models.IntegerField()
    n_banos = models.IntegerField()
    n_habitaciones = models.IntegerField()
    tipo_inmueble = models.ForeignKey(Tipo_inmueble, on_delete=models.CASCADE)
    precio_mensual = models.IntegerField(default=0)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    CHOICES = [
        ('Disponible', 'Disponible'),
        ('Arrendado', 'Arrendado')
    ]

    estado = models.CharField(choices=CHOICES)

    def __str__(self):
        return self.nombre
