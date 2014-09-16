# -*- coding: utf-8 -*-

from osv import osv, fields

class modulo_exemplo_obxecto(osv.osv):
  _name = 'modulo_exemplo.obxecto'
  _description = 'Obxecto'
  _columns = {
    'image': fields.binary("Imaxe", help="Seleccionar imagen aqui"),
    'cadena': fields.char('Campo char', size=200, required=True),
    'boleano': fields.boolean('Campo bolean', required=False),
    'numerico': fields.integer('Campo integer/número enteiro', required=False),
    'float': fields.float('Campo float, número con decimais', required=False),
    'fecha': fields.date('Data', required=False),
    'fechayhora': fields.datetime('Data e hora', required=False),
    'seleccion': fields.selection((('un','UN'),('dous','DOUS')),'Campo selección', required=False),
    'relacion_id': fields.many2one('modulo_exemplo.obxectorelacion','Campo relación'),
    'archivo': fields.binary("Arquivo ou documento", help="Permite insertar un arquivo"),
    'relacionlista_ids': fields.one2many('modulo_exemplo.obxectorelacionlista','name_id','Exemplo de one2many'),
    'textouno': fields.text('Campo texto un', required=False),
    'textodos': fields.text('campo de texto dous', required=False),
    'texto3': fields.text('Campo de texto 3', required=False),
    'cadenados': fields.char('Campo char', size=200, required=False),
    'texto4': fields.text('Campo de texto 4', required=False),

  }
  
modulo_exemplo_obxecto()

class modulo_exemplo_obxectorelacion(osv.osv):
  _name = 'modulo_exemplo.obxectorelacion'
  _description = 'Obxecto relacion'
  _rac_name='name'
  _columns = {
    'name': fields.char('Campo que se vai  ver ',size=200, required=True),
    'otro': fields.char('Outro campo',size=200, required=False),
    'otrocampomas': fields.text('Outro campo distinto', required=False),

  }
  
modulo_exemplo_obxectorelacion()

class modulo_exemplo_obxectorelacionlista(osv.osv):
  _name = 'modulo_exemplo.obxectorelacionlista'
  _description = 'Obxecto one2many'
  _columns = {
    'image': fields.binary("Imaxe", help="Seleccionar imagen aqui"),
    'name_id': fields.many2one('modulo_exemplo.obxecto','Many2one obligado',help="obligado por one2many, no necesario aparezca en vista"),
    'campouno': fields.char('Campo 1',size=200, required=False),
    'campodos': fields.char('Campo 2',size=200, required=False),
    'campotres': fields.char('Campo 3',size=200, required=False),
    'campocuatro': fields.char('Campo 4',size=200, required=False),
    'otrocampomas': fields.text('Outro campo distinto', required=False),

  }
  
modulo_exemplo_obxectorelacionlista()














