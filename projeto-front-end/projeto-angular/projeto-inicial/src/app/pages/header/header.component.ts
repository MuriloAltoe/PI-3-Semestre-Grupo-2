import { UsuarioService } from './../../core/services/usuario/usuario.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UserService } from 'src/app/core/services/user/user.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent implements OnInit {
  logado = false;
  tipoUsuario = '';
  loginFalha = false;
  loginForm!: FormGroup;
  
  constructor(
    private formBuilder: FormBuilder,
    private usuarioService: UsuarioService,
    private router: Router,
    private userService: UserService,
  ) {}

  ngOnInit(): void {
    this.logado = this.userService.isLogged();
    this.userService.getUser().subscribe({
      next: (res) => {
        if(res?.tipo === 'produtor'){
          this.tipoUsuario = 'Area do Produtor';
        } else{
          this.tipoUsuario = 'Area do Usuário';
        }
      }
    });

    this.loginForm = this.formBuilder.group({
      email: ['', Validators.required],
      senha: ['', Validators.required],
    });
  }

  entrar() {
    const email = this.loginForm.get('email')?.value;
    const senha = this.loginForm.get('senha')?.value;

    this.usuarioService.authenticate(email, senha).subscribe({
      next: (res) => {
        this.logado = true;
        this.router.navigate(['home']);
        document.getElementById('closeModal')?.click();
       
      },
      error: (err) => {
        this.loginForm.reset();
        this.logado = false;
        this.loginFalha = true;
        this.tipoUsuario = '';
        console.error(err);
      },
    });
  }

  logout(){
    this.userService.logout();
    this.router.navigate(['']);
    this.logado = false;
  }

  closeModal(){
    this.loginForm.reset();
    this.loginFalha = false;
  }

  changeInput(){
    this.loginFalha = false;
  }
}
