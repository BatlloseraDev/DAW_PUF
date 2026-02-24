import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { PartidaService } from '../../servicios/partida-service';
import { Partida, PartidaDTO, RespuestaDTO } from '../../interfaces/partida';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';


@Component({
  selector: 'app-jugar-partida',
  imports: [RouterLink, ButtonModule, CardModule],
  templateUrl: './jugar-partida.html',
  styleUrl: './jugar-partida.css',
})
export class JugarPartida implements OnInit {
  constructor(
    private partidaService: PartidaService,
    private cdr: ChangeDetectorRef,
  ) { }

  partidas: Partida[] = [];
  partidaActual: Partida | null = null;
  nuevaPartida: boolean = false;
  preguntasDisponibles: number[] = [];
  readonly TOTAL_PREGUNTAS = 30;

  pregunta: RespuestaDTO | null = null;







  ngOnInit(): void {
    this.partidas = JSON.parse(localStorage.getItem('partidas') ?? '[]') as Partida[];
    if (this.partidas.length == 0) {
      this.nuevaPartida = true;
    } else {
      this.partidaActual = this.partidas.find(p => !p.acabada) || null;
      if (!this.partidaActual) {
        this.nuevaPartida = true;
      } else {
        const todasLasPreguntas = Array.from({ length: this.TOTAL_PREGUNTAS }, (_, i) => i + 1);
        const preguntasRespondidas = this.partidaActual.preguntas.map(p => p.id);
        this.preguntasDisponibles = todasLasPreguntas.filter(id => !preguntasRespondidas.includes(id));
        const ultimaPregunta = this.partidaActual.preguntas[this.partidaActual.preguntas.length - 1]
        if (ultimaPregunta.respuesta == null) {
          this.cargarPregunta(ultimaPregunta.id);
        }

      }
    }
  }

  guardarPartidaEnLocalStorage() {
    localStorage.setItem('partidas', JSON.stringify(this.partidas));
  }

  empezarPartida() {
    this.partidaService.empezarPartida().subscribe({
      next: (data: PartidaDTO) => {
        const nuevaPartida: Partida = {
          id: data.id,
          preguntas: [],
          numeroCorrectas: data.numeroCorrectas,
          acabada: false,
          perdida: false
        };

        this.partidas.push(nuevaPartida);
        this.partidaActual = nuevaPartida;
        this.nuevaPartida = false;
        this.guardarPartidaEnLocalStorage();

        this.inicializarPreguntasDisponibles();

        this.cargarPregunta();
      },
      error: (err) => {
        console.log('Error al crear la partida:', err);
      }
    })

  }// llama al servicio de crear una nueva partida
  //llama al servicio de cargar una pregunta




  cargarPregunta(id?: number) {
    const idPregunta = this.obtenerIdPreguntaAleatoria();
    if (!idPregunta) return;



    this.partidaService.obtenerPregunta(id ?? idPregunta).subscribe({
      next: (preguntaBackend) => {
        console.log('La pregunta recibida es: ', preguntaBackend);
        if(!id) this.partidaActual?.preguntas.push({ id: preguntaBackend.id, respuesta: null });
        this.pregunta = preguntaBackend;
        this.guardarPartidaEnLocalStorage();

        this.cdr.detectChanges();
      },
      error: (err) => {
        console.log('Error al cargar la pregunta:', err);
      }
    });
  }





  inicializarPreguntasDisponibles() {
    this.preguntasDisponibles = Array.from({ length: this.TOTAL_PREGUNTAS }, (_, i) => i + 1);

  }

  obtenerIdPreguntaAleatoria(): number | null {
    if (this.preguntasDisponibles.length == 0) {
      return null;
    }
    const indiceAleatorio = Math.floor(Math.random() * this.preguntasDisponibles.length);
    const idElegido = this.preguntasDisponibles[indiceAleatorio];
    this.preguntasDisponibles.splice(indiceAleatorio, 1);
    return idElegido;
  }

  comprobarRespuesta(respuestaUsuario: number) {

    if (!this.partidaActual) return;

    const preguntaActual = this.partidaActual.preguntas.find(p => p.respuesta === null);

    if (!preguntaActual) {
      console.error("No hay preguntas por responder");
      return;
    }

    this.partidaService.obtenerRespuestaPro(preguntaActual.id, this.partidaActual.id, respuestaUsuario).subscribe({
      next: (respuestaBackend) => {

        preguntaActual.respuesta = respuestaUsuario;
         if (this.partidaActual)this.partidaActual.numeroCorrectas = respuestaBackend.numeroCorrectas;
        this.partidaActual!.acabada = respuestaBackend.finPartida;

        this.guardarPartidaEnLocalStorage();

        if (respuestaBackend.finPartida) {
          console.log(`Partida finalizada con ${respuestaBackend.numeroCorrectas} preguntas correctas`)
          // this.partidaActual!.perdida = respuestaBackend.numeroCorrectas < 5;
          // this.partidaActual!.numeroCorrectas = respuestaBackend.numeroCorrectas;
          this.finalizarPartida();
        } else {
         
          this.cargarPregunta();
           this.cdr.detectChanges();
        }
        this.guardarPartidaEnLocalStorage();
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.log('Error al comprobar la respuesta:', err);
      }
    });
  }
  finalizarPartida() {
    if (!this.partidaActual) return;

    this.partidaService.finalizarPartida(this.partidaActual.id).subscribe({
      next: (data: PartidaDTO) => {
        if (this.partidaActual) {
          this.partidaActual.acabada = true;
          this.partidaActual.perdida = data.numeroCorrectas < 5;
          this.guardarPartidaEnLocalStorage();
          this.cdr.detectChanges();
        }
      },
      error: (err) => {
        console.log('Error al finalizar la partida:', err);
      }
    });
  }
}
