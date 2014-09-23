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

class modulo_master_ficha(osv.osv):
  _name = 'modulo_master.ficha'
  _description = 'Ficha'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'apellidosyn': fields.char('Apellidos y Nombre', size=400, required=True),
    'fecha': fields.date('Fecha', required=False),
    'email': fields.char('Correo electrónico', size=200, required=False),
    'telf': fields.integer('Telf Móvil',size=9, required=False),
    'telffijo': fields.integer('Telf Fijo',size=9, required=False),
    'direccion': fields.char('Dirección', size=400, required=False),
    'titulo': fields.text('Título', required=False),
    'becario': fields.text('Becario', required=False),
    'idiomas': fields.text('Idiomas', required=False),
  }
  
modulo_master_ficha()















