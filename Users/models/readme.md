# Tipos de relaciones

---
---

Es obligatorio que pongamos el null=True y blank=True en los elementos que puedan quedar vacíos.
(Ya sabemos que por defecto están como True, pero django lo exige para no tener errores).

---
---

## Relaciones

### 1:1 -> models.OneToOneField

Se debe de guardar primero el objeto en la base de datos que se quiere relacionar. Luego se vincula ese objeto guardado
con el otro elemento que vamos a guardar. Es importante porque si no no deja guardar el conjunto completo.

--- 

### 1:N -> models.ForeignKey

En este tipo de relación se puede ir creando los objetos y vinculándolos a la vez. Finalmente, se procede a hacer el
save() -> Método usado para guardar en la base de datos.

---

### N:M -> models.ManyToManyField

Se debe de guardar primero el objeto en la base de datos que se quiere relacionar. Luego se vincula ese objeto guardado
con el otro elemento que vamos a guardar. Es importante porque si no no deja guardar el conjunto completo.

---
---

## MÉTODOS: ON_DELETE

### models.SET_NULL

Esto permite que si se borra un elemento ligado a este objeto, este objeto no sea alterado si se actualiza/borra el
objeto ligado a él.

---

### models.CASCADE

Esto borra en cascada el elemento ligado a este y que tenga el método CASCADE.