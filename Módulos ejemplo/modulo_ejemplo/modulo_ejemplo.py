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

class modulo_ejemplo_objeto(osv.osv):
  _name = 'modulo_ejemplo.objeto'
  _description = 'Objeto'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'cadena': fields.char('Campo char', size=200, required=True),
    'boleano': fields.boolean('Campo boleano', required=False),
    'numerico': fields.integer('Campo integer/número entero', required=False),
    'float': fields.float('Campo float, número con decimales', required=False),
    'fecha': fields.date('Fecha', required=False),
    'fechayhora': fields.datetime('Fecha y hora', required=False),
    'seleccion': fields.selection((('uno','UNO'),('dos','DOS')),'Campo selección', required=False),
    'relacion_id': fields.many2one('modulo_ejemplo.objetorelacion','Campo relación'),
    'archivo': fields.binary("Archivo o documento", help="Permite insertar un archivo"),
    'relacionlista_ids': fields.one2many('modulo_ejemplo.objetorelacionlista','name_id','Ejemplo de one2many',help="Se obliga a crear many2one"),
    'textouno': fields.text('Campo texto uno', required=False),
    'textodos': fields.text('campo de texto dos', required=False),
    'texto3': fields.text('Campo de texto 3', required=False),
    'cadenados': fields.char('Campo char', size=200, required=False),
    'texto4': fields.text('Campo de texto 4', required=False),

  }
  
modulo_ejemplo_objeto()

class modulo_ejemplo_objetorelacion(osv.osv):
  _name = 'modulo_ejemplo.objetorelacion'
  _description = 'Objeto relacion'
  _rac_name='name'
  _columns = {
    'name': fields.char('Campo que se va a ver ',size=200, required=True),
    'otro': fields.char('Otro campo',size=200, required=False),
    'otrocampomas': fields.text('Otro campo distinto', required=False),

  }
  
modulo_ejemplo_objetorelacion()

class modulo_ejemplo_objetorelacionlista(osv.osv):
  _name = 'modulo_ejemplo.objetorelacionlista'
  _description = 'Objeto one2many'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'name_id': fields.many2one('modulo_ejemplo.objeto','Many2one obligado',help="obligado por one2many, no necesario aparezca en vista"),
    'campouno': fields.char('Campo 1',size=200, required=False),
    'campodos': fields.char('Campo 2',size=200, required=False),
    'campotres': fields.char('Campo 3',size=200, required=False),
    'campocuatro': fields.char('Campo 4',size=200, required=False),
    'otrocampomas': fields.text('Otro campo distinto', required=False),

  }
  
modulo_ejemplo_objetorelacionlista()














