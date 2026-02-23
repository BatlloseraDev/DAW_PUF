import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { TableModule } from 'primeng/table';
import { PortadoresService } from '../servicios/portadores-service';

@Component({
  selector: 'app-portadores-component',
  imports: [FormsModule, TableModule],
  templateUrl: './portadores-component.html',
  styleUrl: './portadores-component.css',
})
export class PortadoresComponent implements OnInit {
  constructor(
    private portadoreService: PortadoresService,
    private route: Router,
    private cdr: ChangeDetectorRef,
  ) { }


  portadores: any[] = [];

 

  ngOnInit(): void {
    this.portadores = JSON.parse(localStorage.getItem('portadores') ?? '[]');
    if (this.portadores.length == 0) {
      this.cargarPortadores();
    }
    
  }
  cargarPortadores() {
    this.portadoreService.obtenerPortadores().subscribe({
      next: (data) => {
        this.portadores = data;
        this.cdr.detectChanges();
        localStorage.setItem('portadores', JSON.stringify(this.portadores));
        console.log(data);
      },
      error: (err) => {
        console.log(err);
      }
    })
  }

  guardarDatos() {
    localStorage.setItem('portadores', JSON.stringify(this.portadores));
    alert("Se han guardado los datos correctamente");
  }
}
