# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django import forms


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    empresa = models.CharField(max_length=128)
    nit = models.IntegerField(blank=True, null=True)
    representante1 = models.CharField(max_length=100, blank=True, null=True)
    representante2 = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    celular1 = models.CharField(max_length=100, blank=True, null=True)
    celular2 = models.CharField(max_length=100, blank=True, null=True)
    correo1 = models.CharField(max_length=100, blank=True, null=True)
    correo2 = models.CharField(max_length=100, blank=True, null=True)
    direccion1 = models.CharField(max_length=100, blank=True, null=True)
    direccion2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'
    def __unicode__(self):
		return self.empresa
        
    def get_absolute_url(self):
        return reverse('empresa-list')



class Pasarela(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa', verbose_name="empresa",blank=True, null=True)
    mac = models.CharField(db_column='MAC', max_length=256, blank=True, null=True)  # Field name made lowercase.
    referencia = models.CharField(max_length=256, blank=True, null=True)
    ubicacion = models.CharField(max_length=256, blank=True, null=True)
    ip_pasarela = models.CharField(db_column='IP_pasarela', max_length=256, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(max_length=100, blank=True, null=True)
    version_firmware = models.CharField(max_length=100, blank=True, null=True)
    fecha_entrada_operacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pasarela'

    def __unicode__(self):
		return self.marca
    
    def get_absolute_url(self):
        return reverse('pasarela-list')

class Medidor(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_pasarela = models.ForeignKey(Pasarela, models.DO_NOTHING, db_column='id_pasarela',verbose_name="pasarela", blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    id_modbus = models.IntegerField(blank=True, null=True)
    ubicacion = models.CharField(max_length=256, blank=True, null=True)
    nombre_punto = models.CharField(max_length=256, blank=True, null=True)
    tipo_medidor = models.CharField(max_length=256, blank=True, null=True)
    ip_medidor = models.CharField(db_column='IP_medidor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(max_length=100, blank=True, null=True)
    version_firmware = models.CharField(max_length=100, blank=True, null=True)
    fecha_entrada_operacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medidor'

    def __unicode__(self):
		return self.medidor
    
    def get_absolute_url(self):
        return reverse('medidor-list')

class SysDiagrams(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_principal = models.BigIntegerField()
    id_diagram = models.BigIntegerField()
    version = models.IntegerField(blank=True, null=True)
    definicion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_diagrams'


class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    perfil = models.CharField(max_length=100)
    estado = models.IntegerField(blank=True, null=True)
    correo_electronico = models.CharField(max_length=200, blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

    def __unicode__(self):
		return self.usuario


class Variable(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_medidor = models.ForeignKey(Medidor, models.DO_NOTHING, db_column='id_medidor', blank=True, null=True)
    id_pasarela = models.ForeignKey(Pasarela, models.DO_NOTHING, db_column='id_pasarela', blank=True, null=True)
    vl1_n = models.FloatField(db_column='VL1_n', blank=True, null=True)  # Field name made lowercase.
    vl2_n = models.FloatField(db_column='VL2_n', blank=True, null=True)  # Field name made lowercase.
    vl3_n = models.FloatField(db_column='VL3_n', blank=True, null=True)  # Field name made lowercase.
    vl1_l2 = models.FloatField(db_column='VL1_L2', blank=True, null=True)  # Field name made lowercase.
    vl2_l3 = models.FloatField(db_column='VL2_L3', blank=True, null=True)  # Field name made lowercase.
    vl3_l1 = models.FloatField(db_column='VL3_L1', blank=True, null=True)  # Field name made lowercase.
    il1 = models.FloatField(db_column='IL1', blank=True, null=True)  # Field name made lowercase.
    il2 = models.FloatField(db_column='IL2', blank=True, null=True)  # Field name made lowercase.
    il3 = models.FloatField(db_column='IL3', blank=True, null=True)  # Field name made lowercase.
    f = models.FloatField(db_column='F', blank=True, null=True)  # Field name made lowercase.
    fp = models.FloatField(db_column='FP', blank=True, null=True)  # Field name made lowercase.
    pa = models.FloatField(db_column='PA', blank=True, null=True)  # Field name made lowercase.
    pq = models.FloatField(db_column='PQ', blank=True, null=True)  # Field name made lowercase.
    ps = models.FloatField(db_column='PS', blank=True, null=True)  # Field name made lowercase.
    ea = models.FloatField(db_column='EA', blank=True, null=True)  # Field name made lowercase.
    eq = models.FloatField(db_column='EQ', blank=True, null=True)  # Field name made lowercase.
    es = models.FloatField(db_column='ES', blank=True, null=True)  # Field name made lowercase.
    disparo = models.TextField(blank=True, null=True)  # This field type is a guess.
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    tiempo = models.DateTimeField(blank=True, null=True)
    pal1 = models.FloatField(db_column='PAL1', blank=True, null=True)  # Field name made lowercase.
    pal2 = models.FloatField(db_column='PAL2', blank=True, null=True)  # Field name made lowercase.
    pal3 = models.FloatField(db_column='PAL3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variable'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __unicode__(self):
		return self.username
    
    def get_absolute_url(self):
        return reverse('user-list')


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class RegistrationRegistrationprofile(models.Model):
    activation_key = models.CharField(max_length=40)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)
    activated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registration_registrationprofile'


class RegistrationSupervisedregistrationprofile(models.Model):
    registrationprofile_ptr = models.ForeignKey(RegistrationRegistrationprofile, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'registration_supervisedregistrationprofile'
