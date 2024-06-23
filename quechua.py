
## importamos streamlit
import streamlit as st

## Leer archivo

import pandas as pd

verbos = pd.read_excel('verbos.xlsx')

## diccionario

quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

## insertar cuadro con conjugaciones de presente
datos = pd.read_excel('Presente1.xlsx')

## Renombrar primera columna
datos = datos.rename(columns={'Unnamed: 0':'Persona'})


## Diccionario de conjugaciones del presente
D = {}
for i in datos.index:
  f = list(datos.loc[i])
  d = dict(zip(['Singular','Plural'],f[1:]))
  D[f[0]] = d

##### FUNCIONES ######

## Conj presente simple
def CPS(base,persona,numero):
  return base + D[persona][numero]

## Conj presente progresivo
def CPC(base,persona,numero):
  return base + 'chka' + CPS(base,persona,numero)[len(base):]

## Conj presente habitual
def CPH(base,persona,numero):
  if persona == 'Tercera':
    resultado = base + 'q' + 'mi'
  else:
    resultado = base + 'q' + ' ' + CPS('ka',persona,numero)
  return resultado

## Conj pasado experimentado simple:
def C_Pas_Exp(base,persona,numero):
  if persona == 'Tercera':
    if numero == 'Singular':
      r_pas_exp = base + 'rqa'
    if numero == 'Plural':
      r_pas_exp = base + 'rqa' + 'ku'
  else:
   r_pas_exp = base + 'rqa' + CPS(base,persona,numero)[len(base):]

  return r_pas_exp

## Conj pasado experimentado progresivo:
def C_Pas_Exp_Pro(base,persona,numero):
  if persona == 'Tercera' and numero == 'Singular':
    r_pas_exp_pro = base + 'chka' + 'rqa'
  else:
    r_pas_exp_pro = base + 'chka' + 'rqa' + CPS(base,persona,numero)[len(base):]

  return r_pas_exp_pro


## Conj pasado experimentado habitual
def C_Pas_Exp_Hab(base,persona,numero):
  if persona == 'Tercera':
    if numero == 'Singular':
      r_pas_exp_hab = base + 'q' + ' ' + 'karqa'
    if numero == 'Plural':
      r_pas_exp_hab = base + 'q' + ' ' + 'karqaku'
  else:
    r_pas_exp_hab = base + 'q' + ' ' + C_Pas_Exp('ka',persona,numero)
  return r_pas_exp_hab


## Conj pasado no experimentado simple
def C_Pas_NExp(base,persona,numero):
  if persona == 'Tercera':
    if numero == 'Singular':
      r_pas_nexp = base + 'sqa'
    if numero == 'Plural':
      r_pas_nexp = base + 'sqa' + 'k'
  else:
    r_pas_nexp = base + 'sqa' + CPS(base,persona,numero)[len(base):]

  return r_pas_nexp

## Conj pasado no experimentado progresivo
def C_Pas_NExp_Pro(base,persona,numero):
  if persona == 'Tercera':
    if numero == 'Singular':
      r_pas_nexp_pro = base +'chka' + 'sqa'
    if numero == 'Plural':
      r_pas_nexp_pro = base + 'chka' + 'sqa' + 'ku'
  else:
    r_pas_nexp_pro = base + 'chka' + 'sqa' + CPS(base,persona,numero)[len(base):]

  return r_pas_nexp_pro

## Conj pasado no experimentado habitual
def C_Pas_NExp_Hab(base,persona,numero):
  if persona == 'Tercera':
    if numero == 'Singular':
      r_pas_nexp_hab = base + 'q' + ' ' + 'kasqa'
    if numero == 'Plural':
      r_pas_nexp_hab = base + 'q' + ' '+ 'kasqaku'
  else:
    r_pas_nexp_hab = base + 'q' + ' ' +  C_Pas_Exp('ka',persona,numero)

  return r_pas_nexp_hab

##### FIN DE FUNCIONES #####


########## configuracion del tema de la pagina

# Función para cargar el CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#### Cargar el CSS
local_css("styles.css")


#### logo y columna

col1, col2 = st.columns([1, 2])  # Ajusta los valores para cambiar la proporción entre columnas

# Colocar el título en la primera columna
## título de la página
with col2:
    st.title('CONJUGADOR DE QUECHUA CHANCA')
## logo de la página
# Colocar la imagen en la segunda columna
with col1:
    st.image('assets/1.png', width=250)



## presentacion

st.header('¡Bienvenido!')



    
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

## texto de presentacion
st.markdown('<p class="caption-custom">Te presentamos el conjugador de quechua de la variedad <b>chanca</b>. Esta variedad es conocida también como variedad <b>ayacuchana</b> y forma parte de la <b>subrama sureña</b> o <b>subrama Quechua II</b>. Es hablada en Huancavelica, Ayacucho y en la parte oeste de Apurímac.</p>', unsafe_allow_html=True)


## Con pronombres y aspecto

P = {'Primera':{'Singular':'ñuqa','Plural':'ñuqayku'},'Segunda':{'Singular':'qam','Plural':'qamkuna'},'Tercera':{'Singular':'pay','Plural':'paykuna'},'Cuarta':{'Singular':'ñuqanchik'}}

## Prototipo con tiempo y aspecto

### opcion de base

base = st.selectbox(
    "Seleccione un verbo en quechua",
    (quechua))
st.write("El verbo en español es", dict_que_esp[base])

### opcion de persona

persona = st.radio(
    'Seleccione la persona',
    ['Primera','Segunda','Tercera','Cuarta'])

### opcion de numero

numero = st.radio(
    'Selecciona el número',
    ['Singular','Plural'])

### boton de tiempo

t = st.selectbox(
    'Selecciona el tiempo',
    ['Presente','Pasado'])

## boton cuando es tiempo presente
if t == 'Presente':
   asp = st.radio(
       'Seleeciona el aspecto',
       ['Simple','Progresivo','Habitual'])

## boton cuando tiempo es pasado
if t == 'Pasado':
  asp = st.radio(
      'Selecciona entre:',
      ['Experimentado','No experimentado'])
  
  if asp == 'Experimentado' or 'No experimentado':
    asp2 = st.radio(
        'Selecciona el aspecto', 
        ['Simple','Progresivo','Habitual'])

## Quitar el sufijo -y de infinitivo
if base[-1] == 'y':
  base = base[:len(base) - 1]

## Eliminar el error de cuarta persona plural
if persona == 'Cuarta' and numero == 'Plural':
  resultado = 'No existe cuarta persona plural'
## Establecer el resultado según tiempo y aspecto
else:
  ## presente simple
  if t == 'Presente' and asp == 'Simple':
    v_conj = CPS(base,persona,numero)
  ## presente progresivo
  if t == 'Presente' and asp == 'Progresivo':
    v_conj = CPC(base,persona,numero)
  ## presente habitual
  if t == 'Presente' and asp == 'Habitual':
    v_conj = CPH(base,persona,numero)
  ## pasado experimentado simple
  if t == 'Pasado' and asp == 'Experimentado' and asp2 == 'Simple':
    v_conj = C_Pas_Exp(base,persona,numero)
  ## pasado experimentado progresivo
  if t == 'Pasado' and asp == 'Experimentado' and asp2 == 'Progresivo':
    v_conj = C_Pas_Exp_Pro(base,persona,numero)
  ## pasado experimentado habitual
  if t == 'Pasado' and asp == 'Experimentado' and asp2 == 'Habitual':
    v_conj = C_Pas_Exp_Hab(base,persona,numero)
  ## pasado no experimentado simple
  if t == 'Pasado' and asp == 'No experimentado' and asp2 == 'Simple':
    v_conj = C_Pas_NExp(base,persona,numero)
  ## pasado no experimentado progresivo
  if t == 'Pasado' and asp == 'No experimentado' and asp2 == 'Progresivo':
    v_conj = C_Pas_NExp_Pro(base,persona,numero)
  ## pasado no experimentado habitual
  if t == 'Pasado' and asp == 'No experimentado' and asp2 == 'Habitual':
    v_conj = C_Pas_NExp_Hab(base,persona,numero)
  resultado = P[persona][numero] + ' ' + v_conj


st.write("**Resultado:**",resultado)


##############################################################################
##############################################################################




