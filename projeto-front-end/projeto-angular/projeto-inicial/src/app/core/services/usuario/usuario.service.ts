import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable, tap, timer } from 'rxjs';
import { IUsuario } from '../../model/interfaces/usuario.interface';
import { UserService } from '../user/user.service';
import { INovoUsuario } from '../../model/interfaces/novo-usuario.interface';
import { environment } from 'src/environments/environment';
import jwtDecode from 'jwt-decode';

@Injectable({
  providedIn: 'root',
})
export class UsuarioService {
  private readonly url = environment.urlApi;

  constructor(private httpclient: HttpClient, private userService: UserService) {}

  getAllUser(): Observable<IUsuario[]> {
    return this.httpclient.get<IUsuario[]>(`${this.url}allUsers`);
  }

  getUserById(id: string): Observable<IUsuario> {
    return this.httpclient.get<IUsuario>(`${this.url}user/${id}`);
  }

  creatUser(usuaurio: INovoUsuario): Observable<IUsuario>{
    return this.httpclient.post<IUsuario>(`${this.url}user`, usuaurio);
  }

  updateUser(id: string, usuaurio: INovoUsuario): Observable<IUsuario>{
    return this.httpclient.put<IUsuario>(`${this.url}user/${id}`, usuaurio);
  }

  authenticate(userName: string, password: string): Observable<HttpResponse<any>> {
    return this.httpclient
      .post<any>(
        `${this.url}login`,
        { email: userName, senha: password},
        { observe: 'response' }
      )
      .pipe(
        tap((res) => {
          if(res.body.token){ 
            const decodedToken: any = jwtDecode(res.body.token);
            const expirationDate = new Date(decodedToken.exp * 1000); 
            console.log(expirationDate)
            this.userService.setToken(res.body.token);
          }
        })
      );
  }

  checkUserExists(email: string): Observable<IUsuario> {
    return this.httpclient.get<IUsuario>(`${this.url}userByEmail/${email}`);
  }

}
