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

class asociados_juntadirectiva(osv.osv):
  _name = 'asociados.juntadirectiva'
  _description = 'Junta directiva'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'cargo': fields.char('Cargo', size=200, required=True),
    'nombre': fields.char('Nombre', size=200, required=True),
    'empresa': fields.char('Empresa', size=100, required=False),
    'telefonoempresa': fields.char('Telf empresa', size=200, required=False),
    'movil': fields.char('Móvil', size=200, required=False),
    'email': fields.char('EMail', size=200, required=False),
    'informacion': fields.text('Informacion', required=False),

  }
  
asociados_juntadirectiva()

class asociados_grupos(osv.osv):
  _name = 'asociados.grupos'
  _description = 'Grupos de trabajo'
  _rac_name='name'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'name': fields.char('Nombre grupo', size=200, required=True),
    'coordinador': fields.char('coordinador/a', size=200, required=False),
    'telefono': fields.char('Teléfono', size=64, required=False),
    'correo': fields.char('Correo', size=200, required=False),
    'miembrosdelgrupo_id': fields.one2many('asociados.miembrosgt','name_id','Miembros del grupo'),
    'informacion': fields.text('Información', required=False),

  }
  
asociados_grupos()

class asociados_miembrosgt(osv.osv):
  _name = 'asociados.miembrosgt'
  _description = 'Miembros gt'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'name_id': fields.many2one('asociados.grupos','Grupo', ),
    'nombre': fields.char('Nombre', size=150, required=False),
    'empresa': fields.char('Empresa', size=200, required=False),
    'telefonoempresa': fields.char('Telf empresa', size=20, required=False),
    'movil': fields.char('Móvil', size=20, required=False),
    'email': fields.char('EMail', size=100, required=False),
    'informacion': fields.text('Información', required=False),

  }
  
asociados_miembrosgt()

class asociados_lista(osv.osv):
  _name = 'asociados.lista'
  _description = 'Lista asociados'
  _columns = {
    'image': fields.binary("Logo", help="Seleccionar imagen aqui"),
    'nombrecliente': fields.char('Nombre', size=200, required=True),
    'codigo': fields.char('Código', size=200, required=False),
    'numero': fields.char('Número', size=64, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'cp': fields.char('C.P.', size=200, required=False),
    'poblacion': fields.char('Población', size=200, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'fax': fields.char('FAX', size=200, required=False),
    'email': fields.char('EMAIL', size=200, required=False),
    'contacto': fields.char('Contacto', size=200, required=False),
    'web': fields.char('WEB', size=200, required=False),
    'altaensello_id': fields.many2one('asociados.altaensello','Alta en sello', help='Alta en sello calidad instaladoras'),
    'concesionsello_id': fields.many2one('asociados.concesionsello','Concesión sello', help='Sello concedido o no'),
    'denegadas_id': fields.many2one('asociados.denegadas','Denegado', help='Sello denegado y motivos'),
    'altaenselloper_id': fields.many2one('asociados.altaenselloper','Alta en sello', help='Alta en sello calidad perforación'),
    'concesionselloper_id': fields.many2one('asociados.concesionselloper','Concesión sello', help='Sello concedido o no'),
    'denegadasper_id': fields.many2one('asociados.denegadasper','Denegado', help='Sello denegado y motivos'),
  }
  
asociados_lista()

class asociados_clasificacion(osv.osv):
  _name = 'asociados.clasificacion'
  _description = 'Clasificacion empresas'
  _columns = {
    'nombre': fields.char('Nombre',size=200, required=True),
    'distribuidora': fields.boolean('Distribuidora', required=False),
    'ingenieria': fields.boolean('Ingeniería', required=False),
    'instaladora': fields.boolean('Instaladora', required=False),
    'sondeos': fields.boolean('Sondeos', required=False),
    'institucionales': fields.boolean('Institucionales', required=False),
    'arquitectura': fields.boolean('Arquitectura', required=False),
    'otrasactividades': fields.text('Otras actividades', required=False),
  
  }
  
asociados_clasificacion()

class asociados_altas(osv.osv):
  _name = 'asociados.altas'
  _description = 'Altas'
  _columns = {
    'nombrecliente': fields.char('Nombre', size=200, required=True),
    'codigo': fields.char('Código', size=200, required=False),
    'numero': fields.char('Número', size=64, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'cp': fields.char('C.P.', size=200, required=False),
    'poblacion': fields.char('Población', size=200, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'fax': fields.char('FAX', size=200, required=False),
    'email': fields.char('EMAIL', size=200, required=False),
    'contacto': fields.char('Contacto', size=200, required=False),
    'web': fields.char('WEB', size=200, required=False),
  }
  
asociados_altas()

class asociados_bajas(osv.osv):
  _name = 'asociados.bajas'
  _description = 'Bajas'
  _columns = {
    'nombrecliente': fields.char('Nombre', size=200, required=True),
    'codigo': fields.char('Código', size=200, required=False),
    'numero': fields.char('Número', size=64, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'cp': fields.char('C.P.', size=200, required=False),
    'poblacion': fields.char('Población', size=200, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'fax': fields.char('FAX', size=200, required=False),
    'email': fields.char('EMAIL', size=200, required=False),
    'contacto': fields.char('Contacto', size=200, required=False),
    'web': fields.char('WEB', size=200, required=False),
  }
  
asociados_bajas()

class asociados_variaciones(osv.osv):
  _name = 'asociados.variaciones'
  _description = 'Variaciones'
  _columns = {
    'nombrecliente': fields.char('Nombre', size=200, required=True),
    'codigo': fields.char('Código', size=200, required=False),
    'numero': fields.char('Número', size=64, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'cp': fields.char('C.P.', size=200, required=False),
    'poblacion': fields.char('Población', size=200, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'fax': fields.char('FAX', size=200, required=False),
    'email': fields.char('EMAIL', size=200, required=False),
    'contacto': fields.char('Contacto', size=200, required=False),
    'web': fields.char('WEB', size=200, required=False),
  }
  
asociados_variaciones()

class asociados_otros(osv.osv):
  _name = 'asociados.otros'
  _description = 'Otros'
  _columns = {
    'nombrecliente': fields.char('Nombre', size=200, required=True),
    'codigo': fields.char('Código', size=200, required=False),
    'numero': fields.char('Número', size=64, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'cp': fields.char('C.P.', size=200, required=False),
    'poblacion': fields.char('Población', size=200, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'fax': fields.char('FAX', size=200, required=False),
    'email': fields.char('EMAIL', size=200, required=False),
    'contacto': fields.char('Contacto', size=200, required=False),
    'web': fields.char('WEB', size=200, required=False),
  }
  
asociados_otros()

class asociados_ingenierias(osv.osv):
  _name = 'asociados.ingenierias'
  _description = 'Ingenierias'
  _columns = {
    'email': fields.char('E-mail', size=200, required=True),
    'fuente': fields.char('Fuente', size=200, required=False),
    'empresa': fields.char('Empresa', size=64, required=False),
    'poblacion': fields.char('Población', size=200, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'cp': fields.char('C.P.', size=11, required=False),
  }
  
asociados_ingenierias()

class asociados_instaladoras(osv.osv):
  _name = 'asociados.instaladoras'
  _description = 'Instaladoras'
  _columns = {
    'email': fields.char('E-mail', size=200, required=True),
    'fuente': fields.char('Fuente', size=200, required=False),
    'empresa': fields.char('Empresa', size=64, required=False),
    'poblacion': fields.char('Población', size=200, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'cp': fields.char('C.P.', size=11, required=False),
  }
  
asociados_instaladoras()

class asociados_sondeos(osv.osv):
  _name = 'asociados.sondeos'
  _description = 'Sondeos'
  _columns = {
    'email': fields.char('E-mail', size=200, required=True),
    'fuente': fields.char('Fuente', size=200, required=False),
    'empresa': fields.char('Empresa', size=64, required=False),
    'poblacion': fields.char('Población', size=200, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'cp': fields.char('C.P.', size=11, required=False),
  }
  
asociados_sondeos()

class asociados_distribuidoras(osv.osv):
  _name = 'asociados.distribuidoras'
  _description = 'Distribuidoras'
  _columns = {
    'email': fields.char('E-mail', size=200, required=True),
    'fuente': fields.char('Fuente', size=200, required=False),
    'empresa': fields.char('Empresa', size=64, required=False),
    'poblacion': fields.char('Población', size=200, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'cp': fields.char('C.P.', size=11, required=False),
  }
  
asociados_distribuidoras()

class asociados_institucionales(osv.osv):
  _name = 'asociados.institucionales'
  _description = 'Institucionales'
  _columns = {
    'email': fields.char('E-mail', size=200, required=True),
    'fuente': fields.char('Fuente', size=200, required=False),
    'empresa': fields.char('Empresa', size=64, required=False),
    'poblacion': fields.char('Población', size=200, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'cp': fields.char('C.P.', size=11, required=False),
  }
  
asociados_institucionales()

class asociados_arquitectura(osv.osv):
  _name = 'asociados.arquitectura'
  _description = 'Arquitectura'
  _columns = {
    'email': fields.char('E-mail', size=200, required=True),
    'fuente': fields.char('Fuente', size=200, required=False),
    'empresa': fields.char('Empresa', size=64, required=False),
    'poblacion': fields.char('Población', size=200, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'cp': fields.char('C.P.', size=11, required=False),
  }
  
asociados_arquitectura()

class asociados_otras(osv.osv):
  _name = 'asociados.otras'
  _description = 'Otras'
  _columns = {
    'email': fields.char('E-mail', size=200, required=True),
    'fuente': fields.char('Fuente', size=200, required=False),
    'empresa': fields.char('Empresa', size=64, required=False),
    'poblacion': fields.char('Población', size=200, required=False),
    'provincia': fields.char('Provincia', size=200, required=False),
    'telefono': fields.char('Teléfono', size=200, required=False),
    'cif': fields.char('C.I.F.', size=200, required=False),
    'direccion': fields.char('Dirección', size=200, required=False),
    'cp': fields.char('C.P.', size=11, required=False),
  }
  
asociados_otras()

class asociados_altaensello(osv.osv):
  _name = 'asociados.altaensello'
  _description = 'Alta en sello'
  _rac_name='name'
  _columns = {
    'name': fields.char('Nº entrada', size=200, required=True),
    'fechaentrada': fields.date('Fecha entrada', required=False),
    'empresa': fields.char('Empresa', size=200, required=False),
    'lugarauditoria': fields.char('Lugar auditoría', size=200, required=False),
    'fechaauditoria': fields.datetime('Fecha auditoría', required=False),
    'aprobada': fields.boolean('¿Aprobada?', required=False),
    'observaciones': fields.text('observaciones', required=False),
  }
  
asociados_altaensello()

class asociados_concesionsello(osv.osv):
  _name = 'asociados.concesionsello'
  _description = 'Concesion sello'
  _rac_name='name'
  _columns = {
    'name': fields.char('Nº registro', size=200, required=True),
    'empresa': fields.char('Empresa', size=200, required=False),
    'fecha': fields.date('Fecha concesión', required=False),
    'observaciones': fields.text('Observaciones', required=False),
  }
  
asociados_concesionsello()

class asociados_denegadas(osv.osv):
  _name = 'asociados.denegadas'
  _description = 'Denegadas'
  _rac_name='name'
  _columns = {
    'name': fields.char('Nº entrada', size=200, required=True),
    'empresa': fields.char('Empresa', size=200, required=False),
    'pendienterevision': fields.boolean('¿Pendiente revisión?', required=False),
    'plazo': fields.char('Plazo de revisión', size=200, required=False),
    'observaciones': fields.text('Observaciones', required=False),
  }
  
asociados_denegadas()

class asociados_altaenselloper(osv.osv):
  _name = 'asociados.altaenselloper'
  _description = 'Alta en sello'
  _rac_name='name'
  _columns = {
    'name': fields.char('Nº entrada', size=200, required=True),
    'fechaentrada': fields.date('Fecha entrada', required=False),
    'empresa': fields.char('Empresa', size=200, required=False),
    'lugarauditoria': fields.char('Lugar auditoría', size=200, required=False),
    'fechaauditoria': fields.datetime('Fecha auditoría', required=False),
    'aprobada': fields.boolean('¿Aprobada?', required=False),
    'observaciones': fields.text('observaciones', required=False),
  }
  
asociados_altaenselloper()

class asociados_concesionselloper(osv.osv):
  _name = 'asociados.concesionselloper'
  _description = 'Concesion sello'
  _rac_name='name'
  _columns = {
    'name': fields.char('Nº registro', size=200, required=True),
    'empresa': fields.char('Empresa', size=200, required=False),
    'fecha': fields.date('Fecha concesión', required=False),
    'observaciones': fields.text('Observaciones', required=False),
  }
  
asociados_concesionselloper()

class asociados_denegadasper(osv.osv):
  _name = 'asociados.denegadasper'
  _description = 'Denegadas'
  _rac_name='name'
  _columns = {
    'name': fields.char('Nº entrada', size=200, required=True),
    'empresa': fields.char('Empresa', size=200, required=False),
    'pendienterevision': fields.boolean('¿Pendiente revisión?', required=False),
    'plazo': fields.char('Plazo de revisión', size=200, required=False),
    'observaciones': fields.text('Observaciones', required=False),
  }
  
asociados_denegadasper()