import { Component } from '@angular/core';
import { Raza } from '../../interfaces/raza';
import { Razas } from '../../clases/razas';
import { InputTextModule } from 'primeng/inputtext';
import { FormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { CommonModule } from '@angular/common';
import { TableModule } from 'primeng/table';
import { RouterLink } from '@angular/router';


@Component({
  selector: 'app-busqueda-raza',
  imports: [InputTextModule, FormsModule, ButtonModule, CommonModule, TableModule, RouterLink],
  templateUrl: './busqueda-raza.html',
  styleUrl: './busqueda-raza.css',
})
export class BusquedaRaza {
  raza = new Razas();

  razasFiltradas: Raza[] = this.raza.razas;
  campoBusqueda: string = '';

  buscar(): void {
    const termino = this.campoBusqueda.toLowerCase();
    this.razasFiltradas = this.raza.razas.filter(r =>
      r.nombre.toLowerCase().includes(termino) ||
      r.descripcion.toLowerCase().includes(termino) ||
      r.regionPrincipal.toLowerCase().includes(termino)
    );
  }

}
