import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable, tap } from 'rxjs';
import { IUsuario } from '../../model/interfaces/usuario.interface';
import { UserService } from '../user/user.service';
import { INovoUsuario } from '../../model/interfaces/novo-usuario.interface';

@Injectable({
  providedIn: 'root',
})
export class UsuarioService {
  private readonly url = 'http://localhost:3000/';

  constructor(private httpclient: HttpClient, private userService: UserService) {}

  getAllUser(): Observable<IUsuario[]> {
    return this.httpclient.get<IUsuario[]>(`${this.url}user/all`);
  }

  creatUser(usuaurio: INovoUsuario): Observable<IUsuario>{
    return this.httpclient.post<IUsuario>(`${this.url}user/signup`, usuaurio);
  }

  authenticate(userName: string, password: string): Observable<HttpResponse<IUsuario>> {
    return this.httpclient
      .post<IUsuario>(
        `${this.url}user/login`,
        { userName, password },
        { observe: 'response' }
      )
      .pipe(
        tap((res) => {
          const authToken = res.headers.get('x-access-token') || '';
          this.userService.setToken(authToken);
        })
      );
  }

  checkUserExists(email: string): Observable<IUsuario> {
    return this.httpclient.get<IUsuario>(this.url + 'user/exists/' + email);
  }
}
