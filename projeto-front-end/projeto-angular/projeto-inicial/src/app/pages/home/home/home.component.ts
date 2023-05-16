import { Component, OnInit } from '@angular/core';
import { IUsuario } from 'src/app/core/model/interfaces/usuario.interface';
import { UsuarioService } from 'src/app/core/services/usuario/usuario.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  usuario: IUsuario[] = [];
  usu!: IUsuario;

  constructor(private service: UsuarioService) {}

  ngOnInit(): void {
    /**  this.usu = {id:2,name:'Ester', email:'ester@gmail.com', senha:'123'};
    this.service.creatUser(this.usu).subscribe({
      next: () => console.log('registrou'),
      error: (err) => console.error(err)      
    });
    this.service.deleteUser(2).subscribe({
      next: () => console.log('deletou'),
      error: (err) => console.error(err)      
    });*/
    this.service.getAllUser().subscribe({
      next: (user) => {
        this.usuario = user;
        console.log(this.usuario);
      },
      error: (err) => console.error(err),
    });

    /** 
    this.service.deleteUser(0).subscribe({
      next: (usuario) => {
        console.log(usuario);
      },
      error: (err) => {
        console.error('Exclusão falhou, ', err);
      },
    });*/
  }

}
