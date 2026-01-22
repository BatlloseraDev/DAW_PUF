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
}
