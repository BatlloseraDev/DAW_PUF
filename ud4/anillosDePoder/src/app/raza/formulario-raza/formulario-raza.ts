import { Component } from '@angular/core';
import { InputTextModule } from 'primeng/inputtext';
import { FormsModule, ReactiveFormsModule, FormControl, FormGroup, Validators} from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { CommonModule } from '@angular/common';
import { TableModule } from 'primeng/table';
import { RouterLink } from '@angular/router';
import { SelectModule } from 'primeng/select';
import { TextareaModule } from 'primeng/textarea';
import { SelectButtonModule } from 'primeng/selectbutton';

@Component({
  selector: 'app-formulario-raza',
  imports: [InputTextModule, FormsModule, ButtonModule, CommonModule, TableModule, RouterLink, ReactiveFormsModule, SelectModule, TextareaModule, SelectButtonModule],
  templateUrl: './formulario-raza.html',
  styleUrl: './formulario-raza.css',
})
export class FormularioRaza {
  regiones = ['Mordor', 'Rivendel', 'La Comarca']
  afinidades = ['Tiene', 'No tiene']



  formulario: FormGroup = new FormGroup({
    nombre: new FormControl('', [
      Validators.required,
      Validators.minLength(3)
    ]),
    descripcion: new FormControl('', [
      Validators.required,
      Validators.minLength(10)
    ]),
    longevidad: new FormControl('', [
      Validators.required,
      Validators.minLength(3)
    ]),
    nivelCorrupcion: new FormControl(0, [
      Validators.required,

    ]),
    regionPrincipal: new FormControl('', [
      Validators.required,
      Validators.minLength(3)
    ]),
    afinidadMagica: new FormControl('', [
      Validators.required
    ])

  })

  enviar() {
    alert
  }
  limpiar() {
    this.formulario.get('nombre')?.setValue('');
    this.formulario.get('descripcion')?.setValue('');
    this.formulario.get('longevidad')?.setValue('');
    this.formulario.get('nivelCorrupcion')?.setValue(0);
    this.formulario.get('regionPrincipal')?.setValue('');
    this.formulario.get('afinidadMagica')?.setValue('');
  }

}
