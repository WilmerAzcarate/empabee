# Generated by Django 4.2.6 on 2023-10-10 20:43

from django.db import migrations

def pais_inserts(apps, schema_editor):
    with open('./sql/paises.sql', 'r',encoding='utf-8') as sql_file:
        sql_query = sql_file.read()
    
    # Ejecuta la consulta SQL
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(sql_query)
        
def departamento_inserts(apps, schema_editor):
    with open('./sql/departamentos.sql', 'r',encoding='utf-8') as sql_file:
        sql_query = sql_file.read()
    
    # Ejecuta la consulta SQL
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(sql_query)
        
def ciudad_inserts(apps, schema_editor):
    with open('./sql/ciudades.sql', 'r',encoding='utf-8') as sql_file:
        sql_query = sql_file.read()
    
    # Ejecuta la consulta SQL
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(sql_query)
class Migration(migrations.Migration):

    dependencies = [
        ('empabee_auth', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(pais_inserts),
        migrations.RunPython(departamento_inserts),
        migrations.RunPython(ciudad_inserts),
    ]