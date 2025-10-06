# Selectores y atributos utilizados en la calculadora retro

| Elemento HTML     | Atributos usados                                  | Selectores CSS aplicables               | Descripción                                                                |
|-------------------|---------------------------------------------------|-----------------------------------------|----------------------------------------------------------------------------|
| `<div>`           | `class="calculadora-retro"`                       | `.calculadora-retro`                    | Contenedor principal de la calculadora.                                    |
| `<h1>`            | —                                                 | `.calculadora-retro h1`                 | Título de la calculadora.                                                  |
| `<div>`           | `class="pantalla-retro"`                          | `.pantalla-retro`                       | Contenedor de los inputs numéricos.                                        |
| `<input>`         | `type="text"`, `class="input-retro"`, `id="num1"` | `.input-retro`, `#num1`                 | Primer número ingresado.                                                   |
| `<input>`         | `type="text"`, `class="input-retro"`, `id="num2"` | `.input-retro`, `#num2`                 | Segundo número ingresado.                                                  |
| `<div>`           | `class="teclado-retro"`                           | `.teclado-retro`                        | Contenedor de los botones de operación.                                    |
| `<button>`        | `id="suma_btn"`, `onclick="sumar()"`              | `#suma_btn`, `.teclado-retro button`    | Botón de suma.                                                             |
| `<button>`        | `id="restar_btn"`, `onclick="restar()"`           | `#restar_btn`                           | Botón de resta.                                                            |
| `<button>`        | `id="multiplicar_btn"`, `onclick="multiplicar()"` | `#multiplicar_btn`                      | Botón de multiplicación.                                                   |
| `<button>`        | `id="dividir_btn"`, `onclick="dividir()"`         | `#dividir_btn`                          | Botón de división.                                                         |
| `<button>`        | `id="modulo_btn"`, `onclick="modulo()"`           | `#modulo_btn`                           | Botón de módulo (resto).                                                   |
| `<button>`        | `id="potencia_btn"`, `onclick="potencia()"`       | `#potencia_btn`                         | Botón de potenciación.                                                     |
| `<button>`        | `id="limpiar_btn"`, `onclick="limpiar()"`         | `#limpiar_btn`                          | Botón de limpiar todo.                                                     |
| `<button>`        | `id="borrar_btn"`, `onclick="borrar()"`           | `#borrar_btn`                           | Botón para borrar último carácter.                                         |
| `<button>`        | `id="resultado_btn"`, `onclick="resultado()"`     | `#resultado_btn`                        | Botón para mostrar el resultado.                                           |
| `<div>`           | `class="resultado-retro"`,`id="resultado_display"`| `.resultado-retro`, `#resultado_display`| Muestra el resultado final.                                                |
| `<audio>`         | `id="tecla-sonido"`, `src`, `preload`             | `#tecla-sonido`                         | Elemento de sonido para el clic retro.                                     |

