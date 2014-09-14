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

class legislacion_galicia(osv.osv):
  _name = 'legislacion.galicia'
  _description = 'Galicia'
  _columns = {
    'directiva': fields.char('Directiva', size=400, required=True),
    'modificada': fields.boolean('Modificada', required=False),
    'nuevadirectiva': fields.char('Nueva', size=400, required=False),
    'derogada': fields.boolean('Derogada', required=False),
    'fuente': fields.char('Fuente', size=200, required=False),
    'resumen': fields.text('Resumen', required=False),
    'contenido': fields.text('Contenido', required=False),
  }
  
legislacion_galicia()

class legislacion_comunidadautonoma(osv.osv):
  _name = 'legislacion.comunidadautonoma'
  _description = 'Comunidad autonoma'
  _columns = {
    'image': fields.binary("Bandera", help="Seleccionar imagen aqui"),
    'comunidad': fields.char('Comunidad', size=200, required=True),
    'directiva': fields.char('Directiva', size=400, required=True),
    'modificada': fields.boolean('Modificada', required=False),
    'nuevadirectiva': fields.char('Nueva', size=400, required=False),
    'derogada': fields.boolean('Derogada', required=False),
    'fuente': fields.char('Fuente', size=200, required=False),
    'resumen': fields.text('Resumen', required=False),
    'contenido': fields.text('Contenido', required=False),
  }
  
legislacion_comunidadautonoma()

class legislacion_estado(osv.osv):
  _name = 'legislacion.estado'
  _description = 'Estado'
  _columns = {
    'directiva': fields.char('Directiva', size=400, required=True),
    'modificada': fields.boolean('Modificada', required=False),
    'nuevadirectiva': fields.char('Nueva', size=400, required=False),
    'derogada': fields.boolean('Derogada', required=False),
    'fuente': fields.char('Fuente', size=200, required=False),
    'resumen': fields.text('Resumen', required=False),
    'contenido': fields.text('Contenido', required=False),
  }
  
legislacion_estado()

class legislacion_unioneuropea(osv.osv):
  _name = 'legislacion.unioneuropea'
  _description = 'Union Europea'
  _columns = {
    'directiva': fields.char('Directiva', size=400, required=True),
    'modificada': fields.boolean('Modificada', required=False),
    'nuevadirectiva': fields.char('Nueva', size=400, required=False),
    'derogada': fields.boolean('Derogada', required=False),
    'fuente': fields.char('Fuente', size=200, required=False),
    'resumen': fields.text('Resumen', required=False),
    'contenido': fields.text('Contenido', required=False),
  }
  
legislacion_unioneuropea()

class legislacion_galiciaer(osv.osv):
  _name = 'legislacion.galiciaer'
  _description = 'Galicia'
  _columns = {
    'directiva': fields.char('Directiva', size=400, required=True),
    'modificada': fields.boolean('Modificada', required=False),
    'nuevadirectiva': fields.char('Nueva', size=400, required=False),
    'derogada': fields.boolean('Derogada', required=False),
    'fuente': fields.char('Fuente', size=200, required=False),
    'resumen': fields.text('Resumen', required=False),
    'contenido': fields.text('Contenido', required=False),
  }
  
legislacion_galiciaer()

class legislacion_comunidadautonomaer(osv.osv):
  _name = 'legislacion.comunidadautonomaer'
  _description = 'Comunidad autonomaer'
  _columns = {
    'image': fields.binary("Bandera", help="Seleccionar imagen aqui"),
    'comunidad': fields.char('Comunidad', size=200, required=True),
    'directiva': fields.char('Directiva', size=400, required=True),
    'modificada': fields.boolean('Modificada', required=False),
    'nuevadirectiva': fields.char('Nueva', size=400, required=False),
    'derogada': fields.boolean('Derogada', required=False),
    'fuente': fields.char('Fuente', size=200, required=False),
    'resumen': fields.text('Resumen', required=False),
    'contenido': fields.text('Contenido', required=False),
  }
  
legislacion_comunidadautonomaer()

class legislacion_estadoer(osv.osv):
  _name = 'legislacion.estadoer'
  _description = 'Estado'
  _columns = {
    'directiva': fields.char('Directiva', size=400, required=True),
    'modificada': fields.boolean('Modificada', required=False),
    'nuevadirectiva': fields.char('Nueva', size=400, required=False),
    'derogada': fields.boolean('Derogada', required=False),
    'fuente': fields.char('Fuente', size=200, required=False),
    'resumen': fields.text('Resumen', required=False),
    'contenido': fields.text('Contenido', required=False),
  }
  
legislacion_estadoer()

class legislacion_unioneuropeaer(osv.osv):
  _name = 'legislacion.unioneuropeaer'
  _description = 'Union Europea'
  _columns = {
    'directiva': fields.char('Directiva', size=400, required=True),
    'modificada': fields.boolean('Modificada', required=False),
    'nuevadirectiva': fields.char('Nueva', size=400, required=False),
    'derogada': fields.boolean('Derogada', required=False),
    'fuente': fields.char('Fuente', size=200, required=False),
    'resumen': fields.text('Resumen', required=False),
    'contenido': fields.text('Contenido', required=False),
  }
  
legislacion_unioneuropeaer()

class legislacion_galiciaot(osv.osv):
  _name = 'legislacion.galiciaot'
  _description = 'Galicia'
  _columns = {
    'directiva': fields.char('Directiva', size=400, required=True),
    'modificada': fields.boolean('Modificada', required=False),
    'nuevadirectiva': fields.char('Nueva', size=400, required=False),
    'derogada': fields.boolean('Derogada', required=False),
    'fuente': fields.char('Fuente', size=200, required=False),
    'resumen': fields.text('Resumen', required=False),
    'contenido': fields.text('Contenido', required=False),
  }
  
legislacion_galiciaot()

class legislacion_comunidadautonomaot(osv.osv):
  _name = 'legislacion.comunidadautonomaot'
  _description = 'Comunidad autonoma'
  _columns = {
    'image': fields.binary("Bandera", help="Seleccionar imagen aqui"),
    'comunidad': fields.char('Comunidad', size=200, required=True),
    'directiva': fields.char('Directiva', size=400, required=True),
    'modificada': fields.boolean('Modificada', required=False),
    'nuevadirectiva': fields.char('Nueva', size=400, required=False),
    'derogada': fields.boolean('Derogada', required=False),
    'fuente': fields.char('Fuente', size=200, required=False),
    'resumen': fields.text('Resumen', required=False),
    'contenido': fields.text('Contenido', required=False),
  }
  
legislacion_comunidadautonomaot()

class legislacion_estadoot(osv.osv):
  _name = 'legislacion.estadoot'
  _description = 'Estado'
  _columns = {
    'directiva': fields.char('Directiva', size=400, required=True),
    'modificada': fields.boolean('Modificada', required=False),
    'nuevadirectiva': fields.char('Nueva', size=400, required=False),
    'derogada': fields.boolean('Derogada', required=False),
    'fuente': fields.char('Fuente', size=200, required=False),
    'resumen': fields.text('Resumen', required=False),
    'contenido': fields.text('Contenido', required=False),
  }
  
legislacion_estadoot()

class legislacion_unioneuropeaot(osv.osv):
  _name = 'legislacion.unioneuropeaot'
  _description = 'Union Europea'
  _columns = {
    'directiva': fields.char('Directiva', size=400, required=True),
    'modificada': fields.boolean('Modificada', required=False),
    'nuevadirectiva': fields.char('Nueva', size=400, required=False),
    'derogada': fields.boolean('Derogada', required=False),
    'fuente': fields.char('Fuente', size=200, required=False),
    'resumen': fields.text('Resumen', required=False),
    'contenido': fields.text('Contenido', required=False),
  }
  
legislacion_unioneuropeaot()