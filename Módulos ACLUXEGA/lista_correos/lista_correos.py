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

class lista_correos_listageneral(osv.osv):
  _name = 'lista_correos.listageneral'
  _description = 'Lista general'
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
    'actividad': fields.char('Acitvidad', size=200, required=False),
  }
  
lista_correos_listageneral()

class lista_correos_bajas(osv.osv):
  _name = 'lista_correos.bajas'
  _description = 'Bajas'
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
    'actividad': fields.char('Acitvidad', size=200, required=False),
  }
  
lista_correos_bajas()

class lista_correos_ingenierias(osv.osv):
  _name = 'lista_correos.ingenierias'
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
  
lista_correos_ingenierias()

class lista_correos_instaladoras(osv.osv):
  _name = 'lista_correos.instaladoras'
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
  
lista_correos_instaladoras()

class lista_correos_sondeos(osv.osv):
  _name = 'lista_correos.sondeos'
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
  
lista_correos_sondeos()

class lista_correos_distribuidoras(osv.osv):
  _name = 'lista_correos.distribuidoras'
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
  
lista_correos_distribuidoras()

class lista_correos_arquitectura(osv.osv):
  _name = 'lista_correos.arquitectura'
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
  
lista_correos_arquitectura()

class lista_correos_sudamerica(osv.osv):
  _name = 'lista_correos.sudamerica'
  _description = 'Sudamerica'
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
  
lista_correos_sudamerica()

class lista_correos_otras(osv.osv):
  _name = 'lista_correos.otras'
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
  
lista_correos_otras()

class lista_correos_agenciasenergia(osv.osv):
  _name = 'lista_correos.agenciasenergia'
  _description = 'Agencias de energia'
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
  
lista_correos_agenciasenergia()

class lista_correos_asociaciones(osv.osv):
  _name = 'lista_correos.asociaciones'
  _description = 'Asociaciones'
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
  
lista_correos_asociaciones()

class lista_correos_colegiosprofesionales(osv.osv):
  _name = 'lista_correos.colegiosprofesionales'
  _description = 'Colegios profesionales'
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
  
lista_correos_colegiosprofesionales()

class lista_correos_universidad(osv.osv):
  _name = 'lista_correos.universidad'
  _description = 'Universidad'
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
  
class lista_correos_otrosa(osv.osv):
  _name = 'lista_correos.otrosa'
  _description = 'Otra'
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
  
lista_correos_otrosa()

class lista_correos_galicia(osv.osv):
  _name = 'lista_correos.galicia'
  _description = 'Galicia'
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
  
lista_correos_galicia()

class lista_correos_estatal(osv.osv):
  _name = 'lista_correos.estatal'
  _description = 'Estatal'
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
  
lista_correos_estatal()

class lista_correos_extranjero(osv.osv):
  _name = 'lista_correos.extranjero'
  _description = 'Extranjero'
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
  
lista_correos_extranjero()

class lista_correos_especializados(osv.osv):
  _name = 'lista_correos.especializados'
  _description = 'Especializados'
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
  
lista_correos_especializados()
 
class lista_correos_online(osv.osv):
  _name = 'lista_correos.online'
  _description = 'Online'
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
  
lista_correos_online()

class lista_correos_otross(osv.osv):
  _name = 'lista_correos.otross'
  _description = 'Otro'
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
  
lista_correos_otross()

class lista_correos_personas(osv.osv):
  _name = 'lista_correos.personas'
  _description = 'Personas'
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
  
lista_correos_personas()

class lista_correos_otros(osv.osv):
  _name = 'lista_correos.otros'
  _description = 'Otros'
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
  
lista_correos_otros()