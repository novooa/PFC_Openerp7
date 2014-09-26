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
  _rac_name='name'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'name': fields.char('Apellidos y Nombre', size=400, required=True),
    'fecha': fields.date('Fecha', required=False),
    'email': fields.char('Correo electrónico', size=200, required=False),
    'telf': fields.integer('Telf Móvil',size=9, required=False),
    'telffijo': fields.integer('Telf Fijo',size=9, required=False),
    'direccion': fields.char('Dirección', size=400, required=False),
    'empresa_id': fields.many2one('modulo_master.empresas','Empresa TFM'),
    'titulo': fields.text('Título', required=False),
    'becario': fields.text('Becario', required=False),
    'idiomas': fields.text('Idiomas', required=False),
  }
  
modulo_master_ficha()

class modulo_master_empresas(osv.osv):
  _name = 'modulo_master.empresas'
  _description = 'Empresas'
  _rac_name='name'
  _columns = {
    'name': fields.char('Nombre de la empresa', size=400, required=True),
    'email': fields.char('Correo electrónico', size=200, required=False),
    'telffijo': fields.integer('Telf Fijo',size=9, required=False),
    'direccion': fields.char('Dirección', size=400, required=False),
    'informacion': fields.text('Información', required=False),
  }
  
modulo_master_empresas()


class modulo_master_asignaturas(osv.osv):
  _name = 'modulo_master.asignaturas'
  _description = 'Asignaturas'
  _columns = {
    'nombre': fields.char('nombre de la asignatura', size=400, required=True),
    'profesor': fields.char('Profesor', required=False),
    'creditos': fields.char('Créditos', size=200, required=False),
    'notas_ids': fields.one2many('modulo_master.calificaciones','name_id','Notas'),
  }
  
modulo_master_asignaturas()

class modulo_master_calificaciones(osv.osv):
  _name = 'modulo_master.calificaciones'
  _description = 'Calificaciones'
  _columns = {
    'name_id': fields.many2one('modulo_master.asignaturas','Many2one obligado',help="obligado por one2many, no necesario aparezca en vista"),
    'nombre': fields.many2one('modulo_master.ficha','Nombre alumno'),
    'nota': fields.char('nota', required=False),
  }
  
modulo_master_calificaciones()








