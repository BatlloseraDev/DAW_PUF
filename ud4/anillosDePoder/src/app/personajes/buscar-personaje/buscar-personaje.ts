import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { PersonajeService } from '../../servicios/personaje-service';
import { Router } from '@angular/router';
import { ButtonModule } from 'primeng/button';

@Component({
  selector: 'app-buscar-personaje',
  imports: [ ButtonModule],
  templateUrl: './buscar-personaje.html',
  styleUrl: './buscar-personaje.css',
})
export class BuscarPersonaje implements OnInit {
  constructor(private personajeService: PersonajeService, private cdr: ChangeDetectorRef , private router: Router) {

  }

  personajes: any[] = [];
  error = ''

  ngOnInit(): void {

    this.cargarPersonajes();
  }

  cargarPersonajes() {
    this.personajeService.obtenerPersonajes().subscribe({
      next: (data) => {
        this.personajes = data;
        this.cdr.detectChanges();
        console.log(data);
      },
      error: (err) => {
        this.error = err;
        console.log(err);
      }
    })
  }

  editar(id: number){
    this.router.navigate(['/editar', id]);
  }
  aniadir(){
    this.router.navigate(['/crear-personaje']);
  }
}
