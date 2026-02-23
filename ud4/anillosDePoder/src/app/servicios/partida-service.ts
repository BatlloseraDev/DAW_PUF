import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root',
})
export class PartidaService {
  constructor(private http: HttpClient){}

  private baseUrl = environment.apiESDLA;

  //centralizo todo el service de lo relacionado a una partida en un archivo service
  //es decir, junto el service de partida y del juego

  empezarPartida():Observable<any>  {
    return this.http.get<any>(`${this.baseUrl}empezarPartida/`);// devuelve una partidaDTO con id
  }

  obtenerPartida(id: number):Observable<any>  {
    return this.http.get<any>(`${this.baseUrl}obtenerPartida/${id}`);
  }

  obtenerPregunta(id: number):Observable<any>  {
    return this.http.get<any>(`${this.baseUrl}obtenerPregunta/${id}`);//busco una pregunta por id de la pregunta...
  }

  obtenerRespuestaPro(id:number, idPartida: number, nRespuesta: number ):Observable<any>  {
    const url = `${this.baseUrl}respuestaMejorada/${id}/${idPartida}`;
    const params = new HttpParams().set('respuestaUsuario',nRespuesta.toString())
    
    return this.http.get<any>(url, { params: params });
  }

  finalizarPartida(id: number):Observable<any>  {
    return this.http.put<any>(`${this.baseUrl}finalizar/${id}/`, {});
  }






  
}
