import { Component, Input } from '@angular/core';
import { IItem } from 'src/app/core/model/interfaces/item.interface';
import { IUsuario } from 'src/app/core/model/interfaces/usuario.interface';

@Component({
  selector: 'app-barraca',
  templateUrl: './barraca.component.html',
  styleUrls: ['./barraca.component.scss']
})
export class BarracaComponent {
  nome = '';
  item1: IItem | null = null;
  item2: IItem | null = null;
  item3: IItem | null = null;
  id=''

  @Input() set produtor(value: IUsuario){
    if(value){
      this.id = value._id;
      this.nome = value.nome.split(' ')[0] || '';
      this.item1 = value.itens[0] || null;
      this.item2 = value.itens[1] || null;
      this.item3 = value.itens[2] || null;
    }
  }
 
}