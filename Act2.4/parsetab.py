
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMILLA CORCHETE_APERTURA CORCHETE_CIERRE IDENTIFICADOR MAYOR_QUE NUMERO PARENTESIS_APERTURA PARENTESIS_CIERRE PUNTO_Y_COMA RESERVADAciclo_while : RESERVADA PARENTESIS_APERTURA RESERVADA MAYOR_QUE NUMERO PARENTESIS_CIERRE CORCHETE_APERTURA instrucciones CORCHETE_CIERREinstrucciones : RESERVADA PARENTESIS_APERTURA COMILLA IDENTIFICADOR COMILLA PARENTESIS_CIERRE PUNTO_Y_COMA'
    
_lr_action_items = {'RESERVADA':([0,3,8,],[2,4,9,]),'$end':([1,12,],[0,-1,]),'PARENTESIS_APERTURA':([2,9,],[3,11,]),'MAYOR_QUE':([4,],[5,]),'NUMERO':([5,],[6,]),'PARENTESIS_CIERRE':([6,15,],[7,16,]),'CORCHETE_APERTURA':([7,],[8,]),'CORCHETE_CIERRE':([10,17,],[12,-2,]),'COMILLA':([11,14,],[13,15,]),'IDENTIFICADOR':([13,],[14,]),'PUNTO_Y_COMA':([16,],[17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ciclo_while':([0,],[1,]),'instrucciones':([8,],[10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ciclo_while","S'",1,None,None,None),
  ('ciclo_while -> RESERVADA PARENTESIS_APERTURA RESERVADA MAYOR_QUE NUMERO PARENTESIS_CIERRE CORCHETE_APERTURA instrucciones CORCHETE_CIERRE','ciclo_while',9,'p_ciclo_while','Sintactico.py',6),
  ('instrucciones -> RESERVADA PARENTESIS_APERTURA COMILLA IDENTIFICADOR COMILLA PARENTESIS_CIERRE PUNTO_Y_COMA','instrucciones',7,'p_instrucciones','Sintactico.py',11),
]
