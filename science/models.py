# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


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


class Caracteristicas22(models.Model):
    field_store = models.IntegerField(db_column='\ufeffStore', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    temperature = models.FloatField(db_column='Temperature', blank=True, null=True)  # Field name made lowercase.
    fuel_price = models.FloatField(db_column='Fuel_Price', blank=True, null=True)  # Field name made lowercase.
    markdown1 = models.TextField(db_column='MarkDown1', blank=True, null=True)  # Field name made lowercase.
    markdown2 = models.TextField(db_column='MarkDown2', blank=True, null=True)  # Field name made lowercase.
    markdown3 = models.TextField(db_column='MarkDown3', blank=True, null=True)  # Field name made lowercase.
    markdown4 = models.TextField(db_column='MarkDown4', blank=True, null=True)  # Field name made lowercase.
    markdown5 = models.TextField(db_column='MarkDown5', blank=True, null=True)  # Field name made lowercase.
    cpi = models.FloatField(db_column='CPI', blank=True, null=True)  # Field name made lowercase.
    unemployment = models.FloatField(db_column='Unemployment', blank=True, null=True)  # Field name made lowercase.
    isholiday = models.TextField(db_column='IsHoliday', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caracteristicas22'


class DataCaracteristicas(models.Model):
    date = models.TextField()
    temperature = models.FloatField()
    fuel_price = models.FloatField()
    md1 = models.CharField(max_length=50)
    md2 = models.CharField(max_length=50)
    md3 = models.CharField(max_length=50)
    md4 = models.CharField(max_length=50)
    md5 = models.CharField(max_length=50)
    cpi = models.DecimalField(max_digits=20, decimal_places=2)
    unenemplyment = models.DecimalField(max_digits=20, decimal_places=2)
    is_holiday = models.CharField(max_length=50)
    id_tienda_c = models.ForeignKey('DataTiendas', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_caracteristicas'


class DataTiendas(models.Model):
    store = models.CharField(primary_key=True, max_length=50)
    types = models.CharField(max_length=1)
    size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'data_tiendas'


class DataVentas(models.Model):
    dept = models.CharField(max_length=100)
    date = models.TextField()
    weekly_sales = models.DecimalField(max_digits=20, decimal_places=2)
    id_tienda_v = models.ForeignKey(DataTiendas, models.DO_NOTHING)
    isholiday = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'data_ventas'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
