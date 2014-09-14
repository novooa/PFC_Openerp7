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

class subvenciones_geotermia(osv.osv):
  _name = 'subvenciones.geotermia'
  _description = 'Geotermia'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_geotermia()

class subvenciones_renovables(osv.osv):
  _name = 'subvenciones.renovables'
  _description = 'Renovables'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_renovables()

class subvenciones_energia(osv.osv):
  _name = 'subvenciones.energia'
  _description = 'Energia'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_energia()

class subvenciones_otras(osv.osv):
  _name = 'subvenciones.otras'
  _description = 'Otras'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_otras()

class subvenciones_unioneuropea(osv.osv):
  _name = 'subvenciones.unioneuropea'
  _description = 'Union europea'
  _columns = {
    'tipo': fields.char('Tipo', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_unioneuropea()

class subvenciones_otra(osv.osv):
  _name = 'subvenciones.otra'
  _description = 'Otras'
  _columns = {
    'tipo': fields.char('Tipo', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('', size=400, required=False),
    'nombredos': fields.char('', size=400, required=False),
    'beneficiarios': fields.text('', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('', required=False),
  }
  
subvenciones_otra()

class subvenciones_cursos(osv.osv):
  _name = 'subvenciones.cursos'
  _description = 'Cursos'
  _columns = {
    'tipo': fields.char('Tipo', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_cursos()

class subvenciones_congresos(osv.osv):
  _name = 'subvenciones.congresos'
  _description = 'Congresos'
  _columns = {
    'tipo': fields.char('Tipo', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_congresos()

class subvenciones_material(osv.osv):
  _name = 'subvenciones.material'
  _description = 'Material'
  _columns = {
    'tipo': fields.char('Tipo', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_material()

class subvenciones_difusion(osv.osv):
  _name = 'subvenciones.difusion'
  _description = 'Difusion'
  _columns = {
    'tipo': fields.char('Tipo', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_difusion()

class subvenciones_personal(osv.osv):
  _name = 'subvenciones.personal'
  _description = 'Personal'
  _columns = {
    'tipo': fields.char('Tipo', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_personal()

class subvenciones_otros(osv.osv):
  _name = 'subvenciones.otros'
  _description = 'Otras'
  _columns = {
    'tipo': fields.char('Tipo', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_otros()

class subvenciones_pedidas(osv.osv):
  _name = 'subvenciones.pedidas'
  _description = 'Pedidas'
  _columns = {
    'tipo': fields.char('Tipo', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_pedidas()

class subvenciones_aceptadaspendientes(osv.osv):
  _name = 'subvenciones.aceptadaspendientes'
  _description = 'Aceptadas pendientes'
  _columns = {
    'tipo': fields.char('Tipo', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_aceptadaspendientes()

class subvenciones_recibidas(osv.osv):
  _name = 'subvenciones.recibidas'
  _description = 'Recibidas'
  _columns = {
    'tipo': fields.char('Tipo', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_recibidas()

class subvenciones_otro(osv.osv):
  _name = 'subvenciones.otro'
  _description = 'Otras'
  _columns = {
    'tipo': fields.char('Tipo', size=200, required=False),
    'lugar': fields.char('Lugar', size=200, required=True),
    'fecha': fields.date('Fecha', size=200, required=False),
    'institucion': fields.char('Institución', size=200, required=False),
    'privada': fields.boolean('¿Privada?', required=False),
    'nboletin': fields.char('Nº boletín', size=200, required=False),
    'nombre': fields.char('Orden/Directiva', size=400, required=False),
    'nombreuno': fields.char('Ord', size=400, required=False),
    'nombredos': fields.char('Ord', size=400, required=False),
    'beneficiarios': fields.text('Información', size=400, required=False),
    'fondostotales': fields.char('Fondos totales', size=400, required=False),
    'fondossubvencionados': fields.char('Fondos subvencionados', size=400, required=False),
    'fondosaportados': fields.char('Fondos aportados', size=400, required=False),
    'fondosgeotermia': fields.char('Fondos a geotermia', size=400, required=False),
    'inversionreal': fields.char('Inversión real', size=400, required=False),
    'otrosimportes': fields.char('Otros importes', size=400, required=False),
    'resumen': fields.text('Resumen', required=False),
  }
  
subvenciones_otro()