# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from osv import osv, fields

class congreso_ficha(osv.osv):
  _name = 'congreso.ficha'
  _description = 'Ficha'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'nombre': fields.char('Nombre', size=200, required=True),
    'subtitulo': fields.char('Subtitulo', size=200, required=False),
    'fechauno': fields.date('Desde', required=False),
    'fechados': fields.date('Hasta', required=False),
    'sede': fields.char('Sede', size=200, required=False),
    'secretariatecnica': fields.char('Secretaría técnica', size=200, required=False),
    'ficha': fields.binary("Ficha del congreso", help="Ficha adjunta"),
    'abrir': fields.char("Abrir con", size=400, required=False),
    'presentacion': fields.text('Presentación', required=False),
    'objetivos': fields.text('Objetivos', required=False),
    'comites': fields.text('Comités', required=False),
    'inscripciones': fields.text('Inscripciones', required=False),
    'creditos': fields.text('Créditos', required=False),
    'exposicion': fields.text('Exposición', required=False),
    'patrocinadores': fields.text('Patrocinadores', required=False),
    'programa': fields.text('Programa', required=False),
    'observaciones': fields.text('Observaciones', required=False),

  }
  
congreso_ficha()

class congreso_programa(osv.osv):
  _name = 'congreso.programa'
  _description = 'programa'
  _columns = {
    'desde': fields.float('Desde'),
    'hasta': fields.float('Hasta'),
    'actividad': fields.char('Actividad', size=200, required=True),
    'ponente': fields.char('Ponente', size=450, required=False),

  }
  
congreso_programa()

class congreso_organizadores(osv.osv):
  _name = 'congreso.organizadores'
  _description = 'Organizadores'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'nombre': fields.char('Nombre', size=200, required=False),
    'contacto': fields.char('Persona contacto', size=200, required=False),
    'direccion': fields.char('Direccion', size=200, required=False),
    'cif': fields.char('C.I.F.', size=50, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'email': fields.char('Email', size=200, required=False),
    'web': fields.char('Web', size=300, required=False),
    'informacion': fields.text('Información', required=False),

  }
  
congreso_organizadores()

class congreso_entidadescolaboradoras(osv.osv):
  _name = 'congreso.entidadescolaboradoras'
  _description = 'Entidades colaboradoras'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'nombre': fields.char('Nombre', size=200, required=False),
    'contacto': fields.char('Persona contacto', size=200, required=False),
    'direccion': fields.char('Direccion', size=200, required=False),
    'cif': fields.char('C.I.F.', size=50, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'email': fields.char('Email', size=200, required=False),
    'web': fields.char('Web', size=300, required=False),
    'informacion': fields.char('Información', size=600,required=False),

  }
  
congreso_entidadescolaboradoras()

class congreso_patrocinadores(osv.osv):
  _name = 'congreso.patrocinadores'
  _description = 'Patrocinadores'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'nombre': fields.char('Nombre', size=200, required=False),
    'contacto': fields.char('Persona contacto', size=200, required=False),
    'direccion': fields.char('Direccion', size=200, required=False),
    'cif': fields.char('C.I.F.', size=50, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'email': fields.char('Email', size=200, required=False),
    'web': fields.char('Web', size=300, required=False),
    'informacion': fields.char('Información', size=600, required=False),

  }
  
congreso_patrocinadores()

class congreso_presentador(osv.osv):
  _name = 'congreso.presentador'
  _description = 'Presentador'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'nombre': fields.char('Nombre', size=200, required=False),
    'empresa': fields.char('Empresa', size=200, required=False),
    'direccion': fields.char('Direccion', size=200, required=False),
    'cif': fields.char('C.I.F.', size=50, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'email': fields.char('Email', size=200, required=False),
    'web': fields.char('Web', size=300, required=False),
    'informacion': fields.text('Información', required=False),

  }
  
congreso_presentador()

class congreso_ponentes(osv.osv):
  _name = 'congreso.ponentes'
  _description = 'Ponentes'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'nombre': fields.char('Nombre', size=200, required=False),
    'empresa': fields.char('Empresa', size=200, required=False),
    'direccion': fields.char('Direccion', size=200, required=False),
    'cif': fields.char('C.I.F.', size=50, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'email': fields.char('Email', size=200, required=False),
    'web': fields.char('Web', size=300, required=False),
    'informacion': fields.text('Información', required=False),

  }
  
congreso_ponentes()

class congreso_expositores(osv.osv):
  _name = 'congreso.expositores'
  _description = 'Expositores'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'nombre': fields.char('Nombre', size=200, required=False),
    'contacto': fields.char('Persona contacto', size=200, required=False),
    'direccion': fields.char('Direccion', size=200, required=False),
    'cif': fields.char('C.I.F.', size=50, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'email': fields.char('Email', size=200, required=False),
    'web': fields.char('Web', size=300, required=False),
    'informacion': fields.text('Información', required=False),

  }
  
congreso_expositores()

class congreso_listapreinscritos(osv.osv):
  _name = 'congreso.listapreinscritos'
  _description = 'Lista preinscritos'
  _columns = {
    'nombre': fields.char('Nombre', size=200, required=True),
    'dni': fields.char('DNI', size=200, required=False),
    'email': fields.char('EMAIL', size=64, required=False),
    'direccioncompleta': fields.char('Dirección completa', size=250, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'pais': fields.char('País', size=200, required=False),
    'tlf': fields.char('Teléfono', size=200, required=False),
    'colectivo': fields.char('Colectivo', size=200, required=False),
    'empresa': fields.char('Empresa', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'ntrabajadores': fields.char('Nº Trabajadores', size=200, required=False),
    'acluxega': fields.boolean('Acluxega', required=False),
    'estudiante': fields.boolean('Estudiante', required=False),
    'entidad': fields.boolean('Entidad/empresa', required=False),
    'pago': fields.boolean('pago', required=False),
    'cantidad': fields.char('Cantidad', size=200, required=False),
    'informacion': fields.char('Información', size=500, required=False),

  }
  
congreso_listapreinscritos()

class congreso_listamatriculados(osv.osv):
  _name = 'congreso.listamatriculados'
  _description = 'Lista matriculados'
  _columns = {
    'nombre': fields.char('Nombre', size=200, required=True),
    'dni': fields.char('DNI', size=200, required=False),
    'email': fields.char('EMAIL', size=100, required=False),
    'direccioncompleta': fields.char('Dirección completa', size=250, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'pais': fields.char('País', size=200, required=False),
    'tlf': fields.char('Teléfono', size=200, required=False),
    'colectivo': fields.char('Colectivo', size=200, required=False),
    'empresa': fields.char('Empresa', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'ntrabajadores': fields.char('Nº Trabajadores', size=200, required=False),
    'acluxega': fields.boolean('Acluxega', required=False),
    'estudiante': fields.boolean('Estudiante', required=False),
    'entidad': fields.boolean('Entidad/empresa', required=False),
    'pago': fields.boolean('pago', required=False),
    'cantidad': fields.char('Cantidad', size=200, required=False),
    'informacion': fields.char('Información', size=500, required=False),

  }
  
congreso_listamatriculados()

class congreso_medios(osv.osv):
  _name = 'congreso.medios'
  _description = 'Medios'
  _rac_name='name'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'name': fields.char('Medio', size=200, required=True),
    'web': fields.char('Web', size=300, required=False),
    'galicia': fields.boolean('Galicia', required=False),
    'estatal': fields.boolean('Estatal', required=False),
    'estranjero': fields.boolean('Extranjero', required=False),
    'especializados': fields.boolean('especializados', required=False),
    'online': fields.boolean('online', required=False),
    'contacto': fields.many2one('congreso.contactos','Contacto'),
    'informacion': fields.text('Información', required=False),

  }
  
congreso_medios()

class congreso_contactos(osv.osv):
  _name = 'congreso.contactos'
  _description = 'Contactos'
  _rac_name='name'
  _columns = {
    'name': fields.char('Nombre', size=200, required=True),
    'medio': fields.many2one('congreso.medios','Medio'),
    'email': fields.char('EMAIL', size=100, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),

  }
  
congreso_contactos()

class congreso_webpropia(osv.osv):
  _name = 'congreso.webpropia'
  _description = 'Web propia'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'titulo': fields.char('Título', size=200, required=True),
    'enlace': fields.char('Enlace', size=300, required=False),
    'informacion': fields.text('Información', required=False),

  }
  
congreso_webpropia()

class congreso_publicidad(osv.osv):
  _name = 'congreso.publicidad'
  _description = 'Publicidad'
  _columns = {
    'fecha': fields.date('Fecha'),
    'medio': fields.many2one('congreso.medios','Medio'),
    'enlace': fields.char('Enlace', size=200, required=False),
    'image1': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image2': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image3': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'presupuesto': fields.text('Presupuesto', required=False),
    'informacion': fields.text('Información', required=False),

  }
  
congreso_publicidad()

class congreso_noticiasgen(osv.osv):
  _name = 'congreso.noticiasgen'
  _description = 'Noticias generadas'
  _columns = {
    'fecha': fields.date('Fecha'),
    'medio': fields.many2one('congreso.medios','Medio'),
    'enlace': fields.char('Enlace', size=200, required=False),
    'image1': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image2': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image3': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'informacion': fields.text('Información', required=False),

  }
  
congreso_noticiasgen()

class congreso_imagenes(osv.osv):
  _name = 'congreso.imagenes'
  _description = 'Imagenes'
  _columns = {
    'evento': fields.char('Enlace', size=200, required=False),
    'fecha': fields.date('Fecha'),
    'informacion': fields.text('Información', required=False),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),

  }
  
congreso_imagenes()