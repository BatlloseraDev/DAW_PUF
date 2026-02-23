import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PortadoresService {
  constructor(private http: HttpClient){}

  private baseURL = environment.apiESDLA;

  obtenerPortadores():Observable<any[]>  {
    return this.http.get<any[]>(`${this.baseURL}listaPortadores`);
  }

}
