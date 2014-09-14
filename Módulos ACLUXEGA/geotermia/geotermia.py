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

class geotermia_preguntasyrespuestas(osv.osv):
  _name = 'geotermia.preguntasyrespuestas'
  _description = 'Preguntas y respuestas'
  _columns = {
    'fecha': fields.date('Fecha', required=False),
    'autorpreg': fields.char('Autor pregunta', size=300, required=False),
    'autorresp': fields.char('Autor respuesta', size=300, required=False),
    'pregunta': fields.text('Pregunta', required=False),
    'respuesta': fields.text('Respuesta', required=False),

  }
  
geotermia_preguntasyrespuestas()

class geotermia_medios(osv.osv):
  _name = 'geotermia.medios'
  _description = 'Medios'
  _rac_name='medio'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'medio': fields.char('Medio', size=200, required=True),
    'web': fields.char('Web', size=300, required=False),
    'galicia': fields.boolean('Galicia', required=False),
    'estatal': fields.boolean('Estatal', required=False),
    'estranjero': fields.boolean('Estranjero', required=False),
    'especializados': fields.boolean('especializados', required=False),
    'online': fields.boolean('online', required=False),
    'contacto': fields.many2one('geotermia.contactos','Contacto'),
    'informacion': fields.text('Información', required=False),

  }
  
geotermia_medios()

class geotermia_contactos(osv.osv):
  _name = 'geotermia.contactos'
  _description = 'Contactos'
  _rac_name='name'
  _columns = {
    'name': fields.char('Nombre', size=200, required=True),
    'medio': fields.many2one('geotermia.medios','Medio'),
    'email': fields.char('EMAIL', size=100, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),

  }
  
geotermia_contactos()

class geotermia_webpropia(osv.osv):
  _name = 'geotermia.webpropia'
  _description = 'Web propia'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'titulo': fields.char('Título', size=200, required=True),
    'enlace': fields.char('Enlace', size=300, required=False),
    'informacion': fields.text('Información', required=False),

  }
  
geotermia_webpropia()

class geotermia_publicidad(osv.osv):
  _name = 'geotermia.publicidad'
  _description = 'Publicidad'
  _columns = {
    'fecha': fields.date('Fecha'),
    'medio': fields.many2one('geotermia.medios','Medio'),
    'enlace': fields.char('Enlace', size=200, required=False),
    'image1': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image2': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image3': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'presupuesto': fields.text('Presupuesto', required=False),
    'informacion': fields.text('Información', required=False),

  }
  
geotermia_publicidad()

class geotermia_noticiasgen(osv.osv):
  _name = 'geotermia.noticiasgen'
  _description = 'Noticias generadas'
  _columns = {
    'fecha': fields.date('Fecha'),
    'medio': fields.many2one('geotermia.medios','Medio'),
    'enlace': fields.char('Enlace', size=200, required=False),
    'image1': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image2': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'image3': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'informacion': fields.text('Información', required=False),

  }
  
geotermia_noticiasgen()

class geotermia_imagenes(osv.osv):
  _name = 'geotermia.imagenes'
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
  
geotermia_imagenes()

class geotermia_alertas(osv.osv):
  _name = 'geotermia.alertas'
  _description = 'Alertas'
  _columns = {
    'image': fields.binary("Bandera", help="Seleccionar imagen aqui"),
    'comunidad': fields.char('Comunidad', size=200, required=True),
    'permite': fields.boolean('Permite suscripción', required=False),
    'permitealertas': fields.boolean('Permite alertas', required=False),
    'llegan': fields.boolean('¿Llegan?', required=False),
    'alertasempleadas': fields.text('Alertas empleadas', required=False),

  }
  
geotermia_alertas()

class geotermia_alertasenviadas(osv.osv):
  _name = 'geotermia.alertasenviadas'
  _description = 'Alertas enviadas'
  _columns = {
    'tipo': fields.char('Tipo', size=100, required=False),
    'ficha': fields.binary("Ficha/documento", help="Ficha adjunta"),
    'abrir': fields.char("Abrir con", size=400, required=False),
    'titulo': fields.char('Título', size=400, required=False),
    'informacion': fields.text('Información', required=False),

  }
  
geotermia_alertasenviadas()












