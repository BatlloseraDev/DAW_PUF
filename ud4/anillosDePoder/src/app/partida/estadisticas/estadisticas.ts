import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { Partida } from '../../interfaces/partida';

import { CardModule } from 'primeng/card';
import { DividerModule } from 'primeng/divider';

@Component({
  selector: 'app-estadisticas',
  imports: [RouterLink,  CardModule, DividerModule],
  templateUrl: './estadisticas.html',
  styleUrl: './estadisticas.css',
})
export class Estadisticas implements OnInit{
    constructor(
        private cdr: ChangeDetectorRef,
    ){}

    ganadas: number = 0;
    perdidas: number = 0;
    total: number = 0;

    partidas: Partida[] = [];
    ngOnInit(): void {
        this.partidas = JSON.parse(localStorage.getItem('partidas') ?? '[]') as Partida[];
        this.pintarPartidas();
    }

    pintarPartidas(){

        const terminadas = this.partidas.filter(p => p.acabada);
        this.ganadas = terminadas.filter(p => !p.perdida).length;
        this.perdidas = terminadas.filter(p => p.perdida).length;
        this.total = terminadas.length;
        this.cdr.detectChanges();
    }

}
