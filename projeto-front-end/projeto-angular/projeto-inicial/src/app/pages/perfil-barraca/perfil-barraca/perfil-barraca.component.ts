import { Component, OnInit } from '@angular/core';
import { IUsuario } from 'src/app/core/model/interfaces/usuario.interface';
import { UsuarioService } from 'src/app/core/services/usuario/usuario.service';
import { ActivatedRoute } from '@angular/router';
import { IItem } from 'src/app/core/model/interfaces/item.interface';
import { ProdutoService } from 'src/app/core/services/produto/produto.service';

@Component({
  selector: 'app-perfil-barraca',
  templateUrl: './perfil-barraca.component.html',
  styleUrls: ['./perfil-barraca.component.scss']
})
export class PerfilBarracaComponent implements OnInit {
  user: IUsuario | null = null;
  usuarioNome = '';
  entrega = '';
  userId = '';
  produtosList: IItem[] = [];

  constructor(
    private usuarioService: UsuarioService,
    private route: ActivatedRoute,
    private produtoService: ProdutoService
  ) {
    this.userId = this.route.snapshot.paramMap.get('id') || '';
  }

  ngOnInit(): void {
    this.getUser();
  }


  getUser() {
    this.usuarioService.getUserById(this.userId).subscribe({
      next: (result) => {
        if (result) {
          this.user = result;
          this.produtosList = result.itens;
          if (this.user) {
            this.usuarioNome = result.nome?.split(' ')[0] || '';
          }
          if (result.tipo == 'produtor') {
            if ((result.entrega as unknown as string) == 'true') {
              this.entrega = 'SIM';
            } else {
              this.entrega = 'NÃO';
            }
          }
        }
      },
      error: (err) => console.error(err),
    });
  }

}
