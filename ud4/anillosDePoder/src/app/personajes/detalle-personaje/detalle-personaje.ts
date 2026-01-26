import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { PersonajeService } from '../../servicios/personaje-service';
import { ActivatedRoute } from '@angular/router';
import { FormGroup, ReactiveFormsModule, FormControl, Validators } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { SelectModule } from 'primeng/select';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-detalle-personaje',
  imports: [ReactiveFormsModule, ButtonModule, SelectModule, RouterLink],
  templateUrl: './detalle-personaje.html',
  styleUrl: './detalle-personaje.css',
})
export class DetallePersonaje implements OnInit {

  constructor(private personaService: PersonajeService, private route: ActivatedRoute, private cdr: ChangeDetectorRef) {

  }
  razas = ['HUMANO', 'ELFO', 'ENANO', 'ORCO', 'MAIAR', 'OSCURO']
  modify = false

  formulario: FormGroup = new FormGroup({
    nombre: new FormControl('', [
      Validators.required,
      Validators.minLength(3)
    ]),
    raza: new FormControl('', [
      Validators.required,
      Validators.minLength(3)
    ]),
    fechaNacimiento: new FormControl('', [
      Validators.required,
      Validators.minLength(3)
    ]),
    nivelCorrupcion: new FormControl(0, [
      Validators.required,

    ]),

  });


  ngOnInit(): void {
    //sacar el id de la url
    const id = this.route.snapshot.paramMap.get('id');
    if(id){
      this.cargarPersonaje(parseInt(id));
      this.modify = true;
    }
    // this.route.paramMap.subscribe(params => {
    //   const id = params.get('id');
    //   if (id) {
    //     console.log("Hacer consulta al servicio con id: " + id);
    //     this.cargarPersonaje(parseInt(id));
    //   }
    // });
  }

  cargarPersonaje(id: number) {
    this.personaService.obtenerPersonaje(id).subscribe({
      next: (data) => {
        console.log(data);
        this.formulario.get('nombre')?.setValue(data.nombre);
        this.formulario.get('raza')?.setValue(data.raza);
        this.formulario.get('fechaNacimiento')?.setValue(data.fechaNacimiento);
        this.formulario.get('nivelCorrupcion')?.setValue(data.nivelCorrupcion);
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.log(err);
      }
    })
  }

  enviar() {
    if(this.modify){

      const id = this.route.snapshot.paramMap.get('id');
      if(id){
        this.personaService.modificarPersonaje(parseInt(id), this.formulario.value).subscribe({
          next: (data) => {
            console.log(data);
          },
          error: (err) => {
            console.log(err);
          }
        })
      }
    
    }else{
      this.personaService.crearPersonaje(this.formulario.value).subscribe({
        next: (data) => {
          console.log(data);
        },
        error: (err) => {
          console.log(err);
        }
      })
    }
  }

  limpiar() {
      this.formulario.get('nombre')?.setValue('');
        this.formulario.get('raza')?.setValue('');
        this.formulario.get('fechaNacimiento')?.setValue('');
        this.formulario.get('nivelCorrupcion')?.setValue('');
  }


}
