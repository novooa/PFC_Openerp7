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

class curso_ficha(osv.osv):
  _name = 'curso.ficha'
  _description = 'Ficha'
  _columns = {
    'nombre': fields.char('Nombre', size=200, required=True),
    'tipo': fields.char('Tipo', size=200, required=False),
    'codigo': fields.char('Código', size=64, required=False),
    'modalidad': fields.char('Modalidad', size=200, required=False),
    'objetivo': fields.char('Objetivo', size=200, required=False),
    'entidadesorganizadoras': fields.char('Entidades organizadoras', size=200, required=False),
    'coordinadores': fields.char('Coordinadores', size=200, required=False),
    'destinatarios': fields.char('destinatarios', size=200, required=False),
    'extension': fields.char('Extensión', size=200, required=False),
    'plazas': fields.char('Plazas', size=200, required=False),
    'ficha': fields.binary("Ficha del curso", help="Ficha adjunta"),
    'abrir': fields.char("Abrir con", size=400, required=False),
    'creditos': fields.text('Créditos', required=False),
    'programa': fields.text('Programa', required=False),
    'condicionesacceso': fields.text('Condiciones', required=False),
    'sistemaevaluacion': fields.text('Evaluación', required=False),
    'materiales': fields.text('Materiales', required=False),
    'metododepago': fields.text('Pago', required=False),
    'metodologia': fields.text('Metodología', required=False),
    'observaciones': fields.text('Observaciones', required=False),
  }
  
curso_ficha()


class curso_periododematricula(osv.osv):
  _name = 'curso.periododematricula'
  _description = 'Periodo de matricula'
  _columns = {
    'desde': fields.datetime('Desde', required=True),
    'hasta': fields.datetime('Hasta', required=True),
    'observaciones': fields.text('Observaciones', size=300, required=False),

  }
  
curso_periododematricula()

class curso_periododedocencia(osv.osv):
  _name = 'curso.periododedocencia'
  _description = 'Periodo de docencia'
  _columns = {
    'desde': fields.datetime('Desde', required=True),
    'hasta': fields.datetime('Hasta', required=True),
    'observaciones': fields.text('Observaciones', size=300, required=False),
  }
  
curso_periododedocencia()

class curso_listapreinscritos(osv.osv):
  _name = 'curso.listapreinscritos'
  _description = 'Lista preinscritos'
  _columns = {
    'nombre': fields.char('Nombre', size=200, required=True),
    'dni': fields.char('DNI', size=20, required=False),
    'email': fields.char('EMAIL', size=64, required=False),
    'direccioncompleta': fields.char('Dirección completa', size=250, required=False),
    'provincia': fields.char('Provincia', size=20, required=False),
    'pais': fields.char('País', size=20, required=False),
    'tlf': fields.char('Teléfono', size=20, required=False),
    'colectivo': fields.char('Colectivo', size=200, required=False),
    'empresa': fields.char('Empresa', size=200, required=False),
    'cif': fields.char('C.I.F.', size=20, required=False),
    'ntrabajadores': fields.char('Nº Trabajadores', size=50, required=False),
    'acluxega': fields.boolean('Acluxega', required=False),
    'bonificada': fields.boolean('Bonificada', required=False),
    'etiquetas': fields.boolean('Etiquetas', required=False),
    'pago': fields.char('Pago', size=200, required=False),
  }
  
curso_listapreinscritos()

class curso_listamatriculados(osv.osv):
  _name = 'curso.listamatriculados'
  _description = 'Lista matriculados'
  _rac_name='name'
  _columns = {
    'name': fields.char('Nombre', size=200, required=True),
    'dni': fields.char('DNI', size=10, required=False),
    'email': fields.char('EMAIL', size=64, required=False),
    'direccioncompleta': fields.char('Dirección completa', size=200, required=False),
    'cp': fields.char('C.P.', size=12, required=False),
    'ciudad': fields.char('Ciudad', size=200, required=False),
    'provincia': fields.char('Provincia', size=50, required=False),
    'pais': fields.char('País', size=50, required=False),
    'tlf': fields.char('Teléfono', size=20, required=False),
    'colectivo': fields.char('Colectivo', size=200, required=False),
    'empresa': fields.char('Empresa', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'ntrabajadores': fields.char('Nº Trabajadores', size=200, required=False),
    'acluxega': fields.boolean('Acluxega', required=False),
    'bonificada': fields.boolean('Bonificada', required=False),
    'etiquetas': fields.boolean('Etiquetas', required=False),
    'pago': fields.char('Pago', size=200, required=False),
    'entregadomanual': fields.boolean('¿Entregado manual?', required=False),
    'asistencia_id': fields.one2many('curso.asistencia','name_id','Asistencia al curso'),
    'evaluacion_id': fields.one2many('curso.evaluacion','name_id','Evaluación'),
    'total': fields.char('Evaluación total', size=200, required=False),
  }
  
curso_listamatriculados()

class curso_asistencia(osv.osv):
  _name = 'curso.asistencia'
  _description = 'Asistencia'
  _columns = {
    'name_id': fields.many2one('curso.listamatriculados','Nombre', ),
    'jornada': fields.char('Jornada', size=100, required=False),
    'asistio': fields.boolean('Asistió', required=False),
  }
  
curso_asistencia()

class curso_evaluacion(osv.osv):
  _name = 'curso.evaluacion'
  _description = 'Evaluacion'
  _columns = {
    'name_id': fields.many2one('curso.listamatriculados','Nombre', ),
    'tema': fields.char('Tema', size=100, required=False),
    'nota': fields.char('Nota', size=20, required=False),
  }
  
curso_evaluacion()

class curso_listabajas(osv.osv):
  _name = 'curso.listabajas'
  _description = 'Lista bajas'
  _columns = {
    'nombre': fields.char('Nombre', size=200, required=True),
    'dni': fields.char('DNI', size=15, required=False),
    'email': fields.char('EMAIL', size=64, required=False),
    'direccioncompleta': fields.char('Dirección completa', size=200, required=False),
    'cp': fields.char('C.P.', size=10, required=False),
    'ciudad': fields.char('Ciudad', size=50, required=False),
    'provincia': fields.char('Provincia', size=50, required=False),
    'pais': fields.char('País', size=15, required=False),
    'tlf': fields.char('Teléfono', size=20, required=False),
    'colectivo': fields.char('Colectivo', size=200, required=False),
    'empresa': fields.char('Empresa', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'ntrabajadores': fields.char('Nº Trabajadores', size=20, required=False),
    'acluxega': fields.boolean('Acluxega', required=False),
    'bonificada': fields.boolean('Bonificada', required=False),
    'etiquetas': fields.boolean('Etiquetas', size=200, required=False),
    'pago': fields.char('Pago', size=200, required=False),
  }
  
curso_listabajas()


class curso_fichaalumnos(osv.osv):
  _name = 'curso.fichaalumnos'
  _description = 'Ficha alumnos'
  _columns = {
    'nombre': fields.char('Nombre', size=200, required=True),
    'dni': fields.char('DNI', size=20, required=False),
    'email': fields.char('EMAIL', size=64, required=False),
    'direccioncompleta': fields.char('Dirección completa', size=200, required=False),
    'cp': fields.char('C.P.', size=10, required=False),
    'ciudad': fields.char('Ciudad', size=50, required=False),
    'provincia': fields.char('Provincia', size=20, required=False),
    'pais': fields.char('País', size=200, required=False),
    'tlf': fields.char('Teléfono', size=200, required=False),
    'colectivo': fields.char('Colectivo', size=200, required=False),
    'empresa': fields.char('Empresa', size=200, required=False),
    'cif': fields.char('C.I.F.', size=20, required=False),
    'ntrabajadores': fields.char('Nº Trabajadores', size=10, required=False),
    'etiquetas': fields.boolean('Etiquetas', required=False),
    'pago': fields.char('Pago', size=200, required=False),
    'entregadomanual': fields.boolean('¿Entregado manual?', required=False),
  }
  
curso_fichaalumnos()

class curso_tutores(osv.osv):
  _name = 'curso.tutores'
  _description = 'Tutores'
  _columns = {
    'nombre': fields.char('Nombre', size=200, required=True),
    'dni': fields.char('DNI', size=200, required=False),
    'email': fields.char('EMAIL', size=64, required=False),
    'tlf': fields.char('Teléfono', size=200, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'modulo': fields.char('Módulo', size=200, required=False),
    'disponibilidaddiayhoras': fields.text('Días y horas', required=False),
    'tutoriasdiayhoras': fields.text('Días y horas', required=False),
    'horasclasediayhoras': fields.text('Días y horas', required=False),
  }
  
curso_tutores()















