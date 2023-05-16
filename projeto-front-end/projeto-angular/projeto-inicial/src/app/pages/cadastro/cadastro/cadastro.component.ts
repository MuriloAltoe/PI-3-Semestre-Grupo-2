import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { IUsuario } from 'src/app/core/model/interfaces/usuario.interface';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.scss'],
})
export class CadastroComponent implements OnInit {
  cadastroForm!: FormGroup;

  constructor(private formBuilder: FormBuilder) {}

  ngOnInit(): void {
    this.cadastroForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      nome: [
        '',
        [
          Validators.required,
          Validators.minLength(2),
          Validators.maxLength(40),
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
      estado: [
        '',
        [Validators.required, Validators.minLength(2), Validators.maxLength(2)],
      ],
      complemento: [''],
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
        ],
      ],
    });
  }

  cadastrar() {
    const newUser = this.cadastroForm.getRawValue() as IUsuario;
    console.log(this.cadastroForm.valid)
    if(this.cadastroForm.valid){
          console.log(newUser);
    }
  }
}
