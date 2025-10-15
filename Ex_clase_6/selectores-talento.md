# 4. Selectores y atributos 

| Elemento HTML     | tipo                                              | Selectores  css                         | Selectores  xpath                       | Descripción                       | Razón                                       |
|-------------------|---------------------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------|---------------------------------------------|
| `<input>`         | `css`                                             | `id="user-name"`                        | `#user-name`                            | input de usuario                  | simple y rapido                             |
| `<input>`         | `css`                                             | `id="password"`                         | `#password`                             | input de usuario de password      | simple y rapido                             |
| `<input>`         | `xpath`                                           | `id="user-name`                         | `//*[@id="user-name"]`                  | input de usuario                  | para probar, se usa cuando no hay opciones. |
| `<input>`         | `xpath`                                           | `id="password`                          | `//*[@id="password"]`                   | input de usuario de password      | para probar, se usa cuando no hay opciones. |
| `<button>`        | `css`                                             | `id="login-button"`                     | `#login-button`                         | Botón login                       | Accesible y directo por ID                  |
| `<button>`        | `xpath`                                           | `id="login-button"`                     | `//*[@id="login-button"]`               | Botón login                       | para probar, se usa cuando no hay opciones. |
# 2.
const nombre = document.getElementById("user-name")
nombre.style.backgroundColor = "#bf34f5ff"
const inputsClaseVarios = document.getElementsByClassName("input_error");
for (let input of inputsClaseVarios) {
  input.value = "¡clase!";
}
const porNombre = document.getElementsByName("user-name");
for(let elemento of porNombre) {
  elemento.style.fontWeight = 'bold';
}
document.querySelector('#user-name').style.outline = '2px solid red';
document.querySelector('#password').style.outline = '2px solid red';
document.querySelector('#login-button').style.outline = '2px solid red';
$x('//*[@id="user-name"]')[0].style.backgroundColor = 'lightblue';

# 3.
document.querySelector('#user-name') 
$x('//*[@id="user-name"]')

# 5.
['#user-name', 'input[type="password"]'].forEach(sel => {
  const el = document.querySelector(sel);
  if (el) el.style.background = "khaki";
});
# 6.
['#user-name', '#password', '#login-button'].forEach(sel => {
  const el = document.querySelector(sel);
  if (el) {
    el.style.backgroundColor = 'lightgreen';
    el.style.border = '2px dashed green';
  }
});