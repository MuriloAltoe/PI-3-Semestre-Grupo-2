import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IUsuario } from '../../model/interfaces/usuario.interface';

@Injectable({
  providedIn: 'root',
})
export class UsuarioService {
  private readonly url = 'http://localhost:3000/';
  constructor(private httpclient: HttpClient) {}

  getAllUser(): Observable<IUsuario[]> {
    return this.httpclient.get<IUsuario[]>(`${this.url}usuario`);
  }

  creatUser(usuaurio: IUsuario): Observable<IUsuario>{
    return this.httpclient.post<IUsuario>(`${this.url}usuario`, usuaurio);
  }

  deleteUser(id: number): Observable<IUsuario>{
    return this.httpclient.delete<IUsuario>(`${this.url}usuario/${id}`);
  }
}
