import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment'//'../../environments/environment.ts';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root',
})
export class PaisesService {
  constructor(private http: HttpClient) { }
  
  private baseUrl = environment.baseUrl;

  getAllCountries():Observable<any[]>  {
    // this.http.get(`${this.baseUrl}all`);
    return this.http.get<any[]>(`${this.baseUrl}all?fields=name,capital`);

  }


}
