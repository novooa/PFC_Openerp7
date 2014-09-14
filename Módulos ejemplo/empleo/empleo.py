# -*- coding: utf-8 -*-
from osv import osv, fields
from openerp import netsvc
from openerp.tools.translate import _
from datetime import datetime

class empleo_paginas(osv.osv):
  _name = 'empleo.paginas'
  _description = 'Paginas'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'name': fields.char('Nombre', size=200, required=True),
    'web': fields.char('Web', size=200, required=False),
    'usuario': fields.char('Usuario', size=200, required=False),
    'contrasena': fields.char('Contraseña', size=200, required=False),
    'boletin_id': fields.one2many('empleo.boletin','name_id','Boletín'),
    'notas': fields.text('Notas', required=False),
  }
  
empleo_paginas()

class empleo_boletin(osv.osv):
  _name = 'empleo.boletin'
  _description = 'Boletin'
  _columns = {
    'name_id': fields.many2one('empleo.paginas','Nombre', ),
    'fecha': fields.date('Fecha', required=False),
    'archivo': fields.binary("Archivo", help="Archivo a cargar"),
    'abrir': fields.char("Abrir con", size=400, required=False),
  }
  
empleo_boletin()

class empleo_becas(osv.osv):
  _name = 'empleo.becas'
  _description = 'Becas'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'name': fields.char('Nombre', size=200, required=True),
    'institucion': fields.char("Institución", size=400, required=False),
    'fecha': fields.date('Fecha', required=False),
    'pagalaempresa': fields.boolean('Paga la empresa', required=False),
    'pagalabeca': fields.boolean('Paga la beca', required=False),
    'cuantia': fields.char('Cuantía', size=200, required=False),
    'ficha': fields.binary("Ficha", help="Ficha adjunta"),
    'abrir': fields.char("Abrir con", size=400, required=False),
    'web': fields.char('Web', size=200, required=False),
    'contacto': fields.char('Contacto', size=200, required=False),
    'informacion': fields.text('Presentación', required=False),
    'notas': fields.text('Notas', required=False),
  }
  
empleo_becas()

class empleo_multinacionales(osv.osv):
  _name = 'empleo.multinacionales'
  _description = 'Multinacionales'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'name': fields.char('Nombre', size=200, required=True),
    'ambito': fields.char('ambito', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'web': fields.char('Web', size=200, required=False),
    'contacto': fields.char('Contacto', size=200, required=False),
    'formulario': fields.boolean('Formulario', required=False),
    'enviadoonline': fields.boolean('Enviado online', required=False),
    'enviadomail': fields.boolean('Enviado mail', required=False),
    'enviadopersona': fields.boolean('Enviado en persona', required=False),
    'enviadoporalguien': fields.boolean('Enviado por alguien', required=False),
    'entrevista': fields.boolean('Entrevista', required=False),
    'fecha': fields.date('Fecha', required=False),
    'informacion': fields.text('Información', required=False),
    'cartapresentacion': fields.text('Carta presentación', required=False),
    'respuestas': fields.text('Respuestas', required=False),
    'notas': fields.text('Notas', required=False),
  }
  
empleo_multinacionales()

class empleo_mineria(osv.osv):
  _name = 'empleo.mineria'
  _description = 'Mineria'
  _columns = {
    'nombre': fields.char('Nombre', size=200, required=True),
    'ambito': fields.char('ambito', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'web': fields.char('Web', size=200, required=False),
    'contacto': fields.char('Contacto', size=200, required=False),
    'formulario': fields.boolean('Formulario', required=False),
    'enviadoonline': fields.boolean('Enviado online', required=False),
    'enviadomail': fields.boolean('Enviado mail', required=False),
    'enviadopersona': fields.boolean('Enviado en persona', required=False),
    'enviadoporalguien': fields.boolean('Enviado por alguien', required=False),
    'entrevista': fields.boolean('Entrevista', required=False),
    'fecha': fields.date('Fecha', required=False),
    'informacion': fields.text('Información', required=False),
    'cartapresentacion': fields.text('Carta presentación', required=False),
    'respuestas': fields.text('Respuestas', required=False),
    'notas': fields.text('Notas', required=False),
  }
  
empleo_mineria()

class empleo_erp(osv.osv):
  _name = 'empleo.erp'
  _description = 'ERP'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'name': fields.char('Nombre', size=200, required=True),
    'erp': fields.char('ERP', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'web': fields.char('Web', size=200, required=False),
    'contacto': fields.char('Contacto', size=200, required=False),
    'formulario': fields.boolean('Formulario', required=False),
    'enviadoonline': fields.boolean('Enviado online', required=False),
    'enviadomail': fields.boolean('Enviado mail', required=False),
    'enviadopersona': fields.boolean('Enviado en persona', required=False),
    'enviadoporalguien': fields.boolean('Enviado por alguien', required=False),
    'entrevista': fields.boolean('Entrevista', required=False),
    'fecha': fields.date('Fecha', required=False),
    'informacion': fields.text('Información', required=False),
    'cartapresentacion': fields.text('Carta presentación', required=False),
    'respuestas': fields.text('Respuestas', required=False),
    'notas': fields.text('Notas', required=False),
  }
  
empleo_erp()

class empleo_otras(osv.osv):
  _name = 'empleo.otras'
  _description = 'Otras'
  _columns = {
    'nombre': fields.char('Nombre', size=200, required=True),
    'ambito': fields.char('ambito', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'web': fields.char('Web', size=200, required=False),
    'contacto': fields.char('Contacto', size=200, required=False),
    'formulario': fields.boolean('Formulario', required=False),
    'enviadoonline': fields.boolean('Enviado online', required=False),
    'enviadomail': fields.boolean('Enviado mail', required=False),
    'enviadopersona': fields.boolean('Enviado en persona', required=False),
    'enviadoporalguien': fields.boolean('Enviado por alguien', required=False),
    'entrevista': fields.boolean('Entrevista', required=False),
    'fecha': fields.date('Fecha', required=False),
    'informacion': fields.text('Información', required=False),
    'cartapresentacion': fields.text('Carta presentación', required=False),
    'respuestas': fields.text('Respuestas', required=False),
    'notas': fields.text('Notas', required=False),
  }
  
empleo_otras()

class empleo_masters(osv.osv):
  _name = 'empleo.masters'
  _description = 'Masters'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'name': fields.char('Nombre', size=200, required=True),
    'universidad': fields.char('Universidad', size=200, required=False),
    'modalidad': fields.char('Modalidad', size=200, required=False),
    'web': fields.char('Web', size=200, required=False),
    'contacto': fields.char('Contacto', size=200, required=False),
    'fechainicio': fields.date('Fecha inicio', required=False),
    'fechafin': fields.date('Fecha fin', required=False),
    'informacion': fields.text('Información', required=False),
    'notas': fields.text('Notas', required=False),
  }
  
empleo_masters()