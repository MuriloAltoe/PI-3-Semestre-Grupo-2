import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { EMPTY, catchError, debounceTime, distinctUntilChanged, filter, map, switchMap, tap } from 'rxjs';
import { IUsuario } from 'src/app/core/model/interfaces/usuario.interface';
import { UsuarioService } from 'src/app/core/services/usuario/usuario.service';

const PAUSA = 300;

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {

  listProdutores: IUsuario[] = []
  campoBusca = new FormControl();
  campoBuscaCidade = new FormControl();
  campoBuscaProduto = new FormControl();

  cidade = '';
  produto = '';

  constructor(private service: UsuarioService) {}

  ngOnInit(): void {
    this.getProdutores();

    this.campoBusca.valueChanges.subscribe({
      next: (value: string) => {
        if(value !== null){
          if(value.length === 0){
            this.getProdutores();
          }
          if(value.length >= 3){
            this.getByFilter(`cidade=${value}`);
          }
        } else {
          this.getProdutores();
        }
      }
    })
    
    this.campoBuscaCidade.valueChanges.subscribe({
      next: (value: string) => {
        if(value !== null){
          this.cidade = '';
          if(value.length === 0 && this.produto == ''){
            this.getProdutores();
            return;
          }
          if(value.length >= 3){
            this.cidade = value;
            if(this.produto !== ''){
              this.getByFilter(`cidade=${value}&item=${this.produto}`);
            } else {
              this.getByFilter(`cidade=${value}`);
            }
          }
        } else {
          this.cidade = '';
          this.getProdutores();
        }
      }
    })

    this.campoBuscaProduto.valueChanges.subscribe({
      next: (value: string) => {
        if(value !== null){
          this.produto = ''
          if(value.length === 0 && this.cidade == ''){
            this.getProdutores();
            return;
          }
          if(value.length >= 3){
            this.produto = value;
            if(this.cidade !== ''){
              this.getByFilter(`cidade=${this.cidade}&item=${this.produto}`);
            } else {
              this.getByFilter(`item=${this.produto}`);
            }
          }
        } else {
          this.produto = '';
          this.getProdutores();
        }
      }
    })
  }

  getProdutores(): void {
    this.service.getAllUser().subscribe({
      next: (produtores) => {
        const pro: IUsuario[] = [];
        produtores.forEach((produtor) => {
          if(produtor.tipo == 'produtor')
          pro.push(produtor)
        })
        this.listProdutores = pro;
      },
      error: (err) => console.error(err),
    });
  }

  getByFilter(filter: string): void{
    this.service.findByFilter(filter).subscribe({
      next: (produtores) => {
        const pro: IUsuario[] = [];
        produtores.forEach((produtor) => {
          if(produtor.tipo == 'produtor')
          pro.push(produtor)
        })
        this.listProdutores = pro;
      },
      error: (err) => console.error(err)
    })
  }
}
