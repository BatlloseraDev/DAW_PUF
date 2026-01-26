import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PersonajeService {
  constructor(private http: HttpClient){}

  private baseUrl = environment.apiESDLA;

  obtenerPersonajes():Observable<any[]>  {
    // this.http.get(`${this.baseUrl}all`);
    return this.http.get<any[]>(`${this.baseUrl}listaPersonajes`);

  }

  obtenerPersonaje(id: number):Observable<any>  {
    // this.http.get(`${this.baseUrl}all`);
    return this.http.get<any>(`${this.baseUrl}obtenerPersonaje/${id}`);
  }
  crearPersonaje(personaje: any):Observable<any>  {
    
    return this.http.post<any>(`${this.baseUrl}insertarPersonaje`, personaje);
  }
  modificarPersonaje(id: number, personaje: any):Observable<any>  {
    
    return this.http.put<any>(`${this.baseUrl}actualizarPersonaje/${id}`, personaje);
  }
}
