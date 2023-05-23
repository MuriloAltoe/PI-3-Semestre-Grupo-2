import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, Subject } from 'rxjs';
import jwt_decode from 'jwt-decode';
import { TokenService } from '../token/token.service';
import { IUsuario } from '../../model/interfaces/usuario.interface';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private userSubject = new BehaviorSubject<IUsuario | null>(null);
  private userName: string = '';

  constructor(private tokenService: TokenService) {
    this.tokenService.hasToken() && this.decodeAndNotify();
  }

  setToken(token: string): void {
    this.tokenService.setToken(token);
    this.decodeAndNotify();
  }

  getUser(): Observable<IUsuario | null> {
    return this.userSubject.asObservable();
  }

  logout() {
    this.tokenService.removeToken();
    this.userSubject.next(null);
  }

  isLogged() {
    return this.tokenService.hasToken();
  }

  getUserName() {
    return this.userName;
  }
  
  private decodeAndNotify(): void {
    const token = this.tokenService.getToken() || '';
    const user = jwt_decode(token) as IUsuario;
    this.userName = user.nome;
    this.userSubject.next(user);
  }
}
