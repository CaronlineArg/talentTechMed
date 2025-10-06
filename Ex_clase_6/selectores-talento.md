# Selectores y atributos 

| Elemento HTML     | tipo                                              | Selectores  aplicables                  | Selectores  aplicables                  | Descripción                       | Razón                                       |
|-------------------|---------------------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------|---------------------------------------------|
| `<input>`         | `css`                                             | `id="user-name"`                        | `#user-name`                            | input de usuario                  | preferente                                  |
| `<input>`         | `css`                                             | `id="password"`                         | `#password`                             | input de usuario de password      | preferente                                  |
| `<input>`         | `xpath`                                           | `id="user-name`                         | `//*[@id="user-name"]`                  | input de usuario                  | para probar, se usa cuando no hay opciones. |
| `<input>`         | `xpath`                                           | `id="password`                          | `//*[@id="password"]`                   | input de usuario de password      | para probar, se usa cuando no hay opciones. |
| `<button>`        | `css`                                             | `id="login-button"`                     | `#login-button`                         | Botón login                       | preferente                                  |
| `<button>`        | `xpath`                                           | `id="login-button"`                     | `//*[@id="login-button"]`               | Botón login                       | para probar, se usa cuando no hay opciones. |

document.querySelector('#login-button').style.outline = '2px solid red';
document.querySelector('#user-name').style.background = '2 px solid red';
['#user-name', 'input[type="password"]'].forEach(sel => {
  const el = document.querySelector(sel);
  if (el) el.style.background = "khaki";
});
