# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cuenta(models.Model):
    idcuenta = models.CharField(primary_key=True, max_length=45)
    foto_perfil = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'


class Solicitud(models.Model):
    emisor = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='emisor')
    receptor = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='receptor', related_name='solicitud_receptor_set')

    class Meta:
        managed = False
        db_table = 'solicitud'


class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido_paterno = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(unique=True, max_length=45)
    contraseña = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    genero = models.IntegerField()
    es_admin = models.IntegerField()
    idcuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='idcuenta')

    class Meta:
        managed = False
        db_table = 'usuario'