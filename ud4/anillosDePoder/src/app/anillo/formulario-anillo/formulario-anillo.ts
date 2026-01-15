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
import { SliderModule } from 'primeng/slider';


@Component({
  selector: 'app-formulario-anillo',
  imports: [InputTextModule, FormsModule, ButtonModule, CommonModule, TableModule, RouterLink, ReactiveFormsModule, SelectModule, TextareaModule, SelectButtonModule, SliderModule],
  templateUrl: './formulario-anillo.html',
  styleUrl: './formulario-anillo.css',
})
export class FormularioAnillo {

  razas = ['Elfo','Enano','Humano','Maiar','Oscuro']

  formulario: FormGroup = new FormGroup({
    nombre: new FormControl('', [
      Validators.required,
      Validators.minLength(3)
    ]),
    portador: new FormControl('', [
      Validators.required,
      Validators.minLength(3)
    ]),
    raza: new FormControl('', [
      Validators.required,
      Validators.minLength(3)
    ]),
    poder: new FormControl('', [
      Validators.required,
      Validators.minLength(3)
    ]),
    corrupcion: new FormControl(0, [
      Validators.required,
      Validators.min(0),
      Validators.max(100)
    ])
  })

  enviar() {
    alert('Formulario enviado')
  }

  limpiar(){
    // this.formulario.reset()
    //limpiar el campo nombre
    this.formulario.get('nombre')?.setValue('');

    this.formulario.get('portador')?.setValue('');

    this.formulario.get('raza')?.setValue('');

    this.formulario.get('poder')?.setValue('');

    this.formulario.get('corrupcion')?.setValue(50);




  }

}
