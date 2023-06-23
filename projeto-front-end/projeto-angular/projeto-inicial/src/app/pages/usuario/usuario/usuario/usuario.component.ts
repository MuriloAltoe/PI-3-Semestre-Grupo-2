import { Component, OnInit } from '@angular/core';
import { IUsuario } from 'src/app/core/model/interfaces/usuario.interface';
import { UserService } from './../../../../core/services/user/user.service';
import {
  AbstractControl,
  FormBuilder,
  FormGroup,
  ValidationErrors,
  Validators,
} from '@angular/forms';
import { UsuarioService } from 'src/app/core/services/usuario/usuario.service';
import { INovoUsuario } from 'src/app/core/model/interfaces/novo-usuario.interface';
import { ActivatedRoute } from '@angular/router';
import { IItem } from 'src/app/core/model/interfaces/item.interface';
import { INewItem } from 'src/app/core/model/interfaces/novo-item.interface';
import { ProdutoService } from 'src/app/core/services/produto/produto.service';

@Component({
  selector: 'app-usuario',
  templateUrl: './usuario.component.html',
  styleUrls: ['./usuario.component.scss'],
})
export class UsuarioComponent implements OnInit {
  cadastroForm!: FormGroup;
  cadastroProdutoForm!: FormGroup;
  editaProdutoForm!: FormGroup;

  isProdutor = false;
  user: IUsuario | null = null;
  usuarioNome = '';
  entrega = '';
  userId = '';
  produtosList: IItem[] = [];
  produtoDelete: IItem | null = null;
  produtoEditar: IItem | null = null;

  constructor(
    private formBuilder: FormBuilder,
    private usuarioService: UsuarioService,
    private route: ActivatedRoute,
    private produtoService: ProdutoService
  ) {
    this.userId = this.route.snapshot.paramMap.get('id') || '';
  }

  ngOnInit(): void {
    this.getUser();
    this.startForm();
    this.startFormProduto();
    this.startFormProdutoEditar();
  }

  startForm(): void {
    this.cadastroForm = this.formBuilder.group({
      email: [this.user?.email || ''],
      nome: [
        this.user?.nome || '',
        [
          Validators.required,
          Validators.minLength(2),
          Validators.maxLength(50),
        ],
      ],
      tipo: [this.user?.tipo || ''],
      cep: [
        this.user?.cep || '',
        [Validators.required, Validators.minLength(8), Validators.maxLength(9)],
      ],
      rua: [this.user?.rua || '', [Validators.required]],
      numero: [this.user?.numero || '', [Validators.required]],
      bairro: [this.user?.bairro || '', [Validators.required]],
      cidade: [this.user?.cidade || '', [Validators.required]],
      estado: [this.user?.estado || '', [Validators.required]],
      complemento: [this.user?.complemento || ''],
      entrega: [this.user?.entrega || null],
      telefone: [this.user?.telefone || null],
      senha: [
        this.user?.senha.toString() || '',
        [
          Validators.required,
          Validators.minLength(8),
          Validators.maxLength(14),
        ],
      ],
      confirmaSenha: [
        this.user?.senha.toString() || '',
        [
          Validators.required,
          Validators.minLength(8),
          Validators.maxLength(14),
          this.validarSenhasCompativeis,
        ],
      ],
    });
  }

  startFormProduto() {
    this.cadastroProdutoForm = this.formBuilder.group({
      nomeProduto: [
        '',
        [
          Validators.required,
          Validators.minLength(2),
          Validators.maxLength(50),
        ],
      ],
      categoriaProduto: [
        '',
        [
          Validators.required,
          Validators.minLength(2),
          Validators.maxLength(50),
        ],
      ],
      medidaProduto: [
        '',
        [
          Validators.required,
          Validators.minLength(2),
          Validators.maxLength(50),
        ],
      ],
      valorProduto: ['', [Validators.required, Validators.min(0.5)]],
      quantidadeProduto: ['', [Validators.required, Validators.min(1)]],
    });
  }

  startFormProdutoEditar() {
    this.editaProdutoForm = this.formBuilder.group({
      nome: [
        this.produtoEditar?.nome || '',
        [
          Validators.required,
          Validators.minLength(2),
          Validators.maxLength(50),
        ],
      ],
      categoria: [
        this.produtoEditar?.categoria || '',
        [
          Validators.required,
          Validators.minLength(2),
          Validators.maxLength(50),
        ],
      ],
      medida: [
        this.produtoEditar?.medida || '',
        [
          Validators.required,
          Validators.minLength(2),
          Validators.maxLength(50),
        ],
      ],
      valor: [ this.produtoEditar?.preco || '', [Validators.required, Validators.min(0.5)]],
      quantidade: [ this.produtoEditar?.quantidade || '', [Validators.required, Validators.min(1)]],
    });
  }

  validarSenhasCompativeis(control: AbstractControl): ValidationErrors | null {
    const senha = control.parent?.value.senha;
    const confirmarSenha = control.value;
    if (
      confirmarSenha &&
      confirmarSenha.length >= 8 &&
      confirmarSenha.length <= 14 &&
      senha !== confirmarSenha
    ) {
      return { senhasDiferentes: true };
    }
    return null;
  }

  editar() {
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
      this.usuarioService.updateUser(this.user?._id || '', newUser).subscribe({
        next: () => {
          this.getUser();
          document.getElementById('closeModalUsuario')?.click();
        },
        error: (err) => console.error(err),
      });
    }
  }

  getUser() {
    this.usuarioService.getUserById(this.userId).subscribe({
      next: (result) => {
        if (result) {
          this.user = result;
          this.produtosList = result.itens;
          if (this.user) {
            this.startForm();
            this.usuarioNome = result.nome?.split(' ')[0] || '';
          }
          if (result.tipo == 'produtor') {
            this.isProdutor = true;
            if ((result.entrega as unknown as string) == 'true') {
              this.entrega = 'SIM';
            } else {
              this.entrega = 'NÃO';
            }
          } else {
            this.isProdutor = false;
          }
        }
      },
      error: (err) => console.error(err),
    });
  }

  cadastrarProduto() {
    const itemForm = this.cadastroProdutoForm.getRawValue();
    const item: INewItem = {
      nome: itemForm.nomeProduto,
      preco: itemForm.valorProduto,
      medida: itemForm.medidaProduto,
      categoria: itemForm.categoriaProduto,
      quantidade: itemForm.quantidadeProduto,
      id_barraca: this.userId,
    };

    if (this.cadastroProdutoForm.valid) {
      this.produtoService.creatItem(item).subscribe({
        next: () => {
          this.getUser();
          this.cadastroProdutoForm.reset();
          document.getElementById('fecharCadastroProduto')?.click();
        },
        error: (err) => console.error(err),
      });
    }
  }

  editarProduto() {
    const itemForm = this.editaProdutoForm.getRawValue();
    const item: IItem = {
      _id: this.produtoEditar?._id || '',
      nome: itemForm.nome,
      preco: itemForm.valor,
      medida: itemForm.medida,
      categoria: itemForm.categoria,
      quantidade: itemForm.quantidade,
      id_barraca: this.userId,
    };
    if (this.editaProdutoForm.valid) {
      this.produtoService.updateItem(item._id, item).subscribe({
        next: () => {
          this.getUser();
          this.editaProdutoForm.reset();
          document.getElementById('fecharEditarProduto')?.click();
          this.produtoEditar = null;
        },
        error: (err) => console.error(err),
      });
    }
  }

  deltarProduto() {
    if (this.produtoDelete !== null) {
      this.produtoService.deleteItem(this.produtoDelete._id).subscribe({
        next: () => {
          this.getUser();
          document.getElementById('fecharDeletarModal')?.click();
          this.produtoDelete = null;
        },
        error: (err) => console.error(err),
      });
    }
  }

  setProdutoDeletar(produto: IItem) {
    this.produtoDelete = produto;
  }

  setProdutoEditar(produto: IItem){
    this.produtoEditar = produto;
    this.startFormProdutoEditar();
  }
}
