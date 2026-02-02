import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { PersonajeService } from '../../servicios/personaje-service';
import { Router } from '@angular/router';
import { ButtonModule } from 'primeng/button';
import { FormsModule } from '@angular/forms';
import { TableModule } from 'primeng/table';
import { RouterLink } from '@angular/router';
import { ConfirmarPopup } from '../../modales/confirmar-popup/confirmar-popup';
import { ConfiguracionPopup } from '../../interfaces/configuracion-popup';

@Component({
  selector: 'app-buscar-personaje',
  imports: [ ButtonModule, FormsModule, TableModule, RouterLink, ConfirmarPopup],
  templateUrl: './buscar-personaje.html',
  styleUrl: './buscar-personaje.css',
})
export class BuscarPersonaje implements OnInit {
  constructor(private personajeService: PersonajeService, private cdr: ChangeDetectorRef , private router: Router) {

  }

  getSoftDeleteConfig(id: number): ConfiguracionPopup {
    return {
      message: "Seguro que quieres borrar logicamente este personaje?",
      header: "Borrado",
      nameButton: `<img src="https://github.com/user-attachments/assets/bbba141b-bebe-40ab-878d-081a4ccfe122" width="25">`,
      severity: 'danger',
      funcion: () => {
        console.log("Borrado lógico de: " + id);
        this.softDelete(id)
      }
    };
  }

  getReactivateConfig(id: number): ConfiguracionPopup {
    return {
      message: "Seguro que quieres reactivar este personaje?",
      header: "Reactivar",
      nameButton: `<img src="https://github.com/user-attachments/assets/a9799ece-ed21-419c-bca2-068f20dd8a91" width="25">`,
      severity: 'success',
      funcion: () => {
        console.log("Reactivar de: " + id);
        this.reactivar(id)
      }
    };
  }

  getDeleteConfig(id: number): ConfiguracionPopup {
    return {
      message: "Seguro que quieres borrar definitivamente este personaje?",
      header: "Borrado Definitivo",
      nameButton: `<img src="https://github.com/user-attachments/assets/c7f978b2-4c39-4d55-ba14-50a2656ee7d7" width="25">`,
      severity: 'danger',
      funcion: () => {
        console.log("Borrado definitivo de: " + id);
        this.eliminar(id)
      }
    };
  }




  // hardDelete: ConfiguracionPopup = {
  //   message : "Seguro que quieres borrar permanentemente este personaje?",
  //   header : "Borrado Permanente",
  //   nameButton: "Borrado Permanente",
  //   severity: 'danger',
  //   funcion: ()=> {
  //     console.log("Borrado permanente");
  //   }
  // }



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

  softDelete(id: number){
    this.personajeService.softDeletePersonaje(id).subscribe({
      next: (data) => {
        this.cargarPersonajes();
        console.log(data);
      },
      error: (err) => {
        this.error = err;
        console.log(err);
      }
    })
  }

  reactivar(id: number){
    this.personajeService.reactivarPersonaje(id).subscribe({
      next: (data) => {
        this.cargarPersonajes();
        console.log(data);
      },
      error: (err) => {
        this.error = err;
        console.log(err);
      }
    })
  }

  eliminar(id: number){
    this.personajeService.eliminarPersonaje(id).subscribe({
      next: (data) => {
        this.cargarPersonajes();
        console.log(data);
      },
      error: (err) => {
        this.error = err;
        console.log(err);
      }
    })
  }

}
