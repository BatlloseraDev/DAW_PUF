import { Component } from '@angular/core';
import { ConfirmarPopup } from '../confirmar-popup/confirmar-popup';
import { BuscarPersonaje } from '../../personajes/buscar-personaje/buscar-personaje';
import { ConfiguracionPopup } from '../../interfaces/configuracion-popup';



@Component({
  selector: 'app-padre',
  imports: [ConfirmarPopup],
  templateUrl: './padre.html',
  styleUrl: './padre.css',
})
export class Padre {
  parametrosModal: ConfiguracionPopup = {
    message : '<strong>Francisco</strong>',
    header : "Personaje",
    nameButton: "Borrar",
    severity: 'danger',
    funcion: ()=> {}
  }
}
