import { UsuarioService } from './../../../core/services/usuario/usuario.service';
import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormBuilder, FormGroup, ValidationErrors, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { INovoUsuario } from 'src/app/core/model/interfaces/novo-usuario.interface';
import { IUsuario } from 'src/app/core/model/interfaces/usuario.interface';
import { UserNotTakenValidatorService } from 'src/app/core/validators/user-not-taken.validator.service';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.scss'],
})
export class CadastroComponent implements OnInit {
  cadastroForm!: FormGroup;
  isProdutor = false;

  constructor(
    private formBuilder: FormBuilder,
    private usuarioService: UsuarioService,
    private router: Router,
    private userNotTakenValidatorService: UserNotTakenValidatorService,
  ) {}

  ngOnInit(): void {
    this.cadastroForm = this.formBuilder.group({
      email: [
        '',
        [Validators.required, Validators.email],
        this.userNotTakenValidatorService.checkUserNameTaken(),
      ],
      nome: [
        '',
        [
          Validators.required,
          Validators.minLength(2),
          Validators.maxLength(50),
        ],
      ],
      tipo: ['', [Validators.required]],
      cep: [
        '',
        [Validators.required, Validators.minLength(8), Validators.maxLength(9)],
      ],
      rua: ['', [Validators.required]],
      numero: ['', [Validators.required]],
      bairro: ['', [Validators.required]],
      cidade: ['', [Validators.required]],
      estado: ['', [Validators.required]],
      complemento: [''],
      entrega: [null],
      telefone: [null],
      senha: [
        '',
        [
          Validators.required,
          Validators.minLength(8),
          Validators.maxLength(14),
        ],
      ],
      confirmaSenha: [
        '',
        [
          Validators.required,
          Validators.minLength(8),
          Validators.maxLength(14),
          this.validarSenhasCompativeis
        ]
      ],
    });
  }

  validarSenhasCompativeis(control: AbstractControl): ValidationErrors | null {
    const senha = control.parent?.value.senha;
    const confirmarSenha = control.value;

    if (confirmarSenha && confirmarSenha.length >= 8  && confirmarSenha.length <= 14 && senha !== confirmarSenha) {
      return { senhasDiferentes: true };
    }
    return null;
  }
  
  changeTipo($event: any) {
    if ($event == 'produtor') {
      this.isProdutor = true;
    } else {
      this.isProdutor = false;
      this.cadastroForm.get('entrega')?.setValue(null);
      this.cadastroForm.get('telefone')?.setValue(null);
    }
  }


  cadastrar() {
    const userForm = this.cadastroForm.getRawValue() as IUsuario;

    const newUser: INovoUsuario = {
      nome: userForm.nome,
      email: userForm.email,
      senha: userForm.senha,
      tipo: userForm.tipo,
      cep: userForm.cep,
      rua: userForm.rua,
      numero: userForm.numero,
      bairro: userForm.bairro,
      cidade: userForm.cidade,
      estado: userForm.estado,
      complemento: userForm.complemento,
      entrega: userForm.entrega,
      telefone: userForm.telefone,
    };

    if (this.cadastroForm.valid) {
      this.usuarioService.creatUser(newUser).subscribe({
        next: () => this.router.navigate(['']),
        error: (err) => {
          console.error(err);
        },
      });
    }
  }
}
